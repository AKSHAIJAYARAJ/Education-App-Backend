from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .user import User
from .serializers import UserManagerSerializer
from .models import UserModel
import jwt
import bcrypt
import datetime
from django.conf import settings
from education.utility.redis_manager import RedisManager
from utility.otp_client import OTPGenerator
from utility.email_client import Email
from .notification_manager import EmailNotifications

        

class UserRegistrationViewSet(APIView):

    validator = UserManagerSerializer

    def post(self,request):
        try:
            # Get data from request
            user = self.validator(data=request.data)
            if user.is_valid():
                data = user.validated_data

                # Check in user already exists
                if "user_phone_number" in data.keys():
                    user = User().get(filters={"user_phone_number" :data["user_phone_number"]})
                elif "user_email" in data.keys():
                    user = User().get(filters={"user_email" :data["user_email"]})
                if user:
                    return Response(data={"status":'ERROR',"result":'user already exists','message':"ERROR"},status=status.HTTP_400_BAD_REQUEST)
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(data['user_password'].encode('utf-8'), salt)
                data['user_password'] = hashed_password.decode('utf-8')
                response = User().post(payload = data)
                return Response(data={"status":'OK',"result":'User created','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": user.errors,'message':"Invalid"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        user_id = request.query_params.get("user_id")
        try:
            response = User().get(filters= {'user_id':user_id})
            return Response(data={"status":'OK',"result":response,'message':"SUCCESS"},status=status.HTTP_200_OK)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        user_id = request.query_params.get("user_id")
        try:
            user = self.validator(data=request.data)
            if user.is_valid():
                response = User().put(payload = user.validated_data,user_id=user_id)
                return Response(data={"status":'OK',"result":'User updated','message':"SUCCESS"},status=status.HTTP_200_OK)
            else: 
                return Response(data={"status":'ERROR',"result": user.errors,'message':"Invalid"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        pass

class ResetPasswordViewSet(APIView):
    validator = UserManagerSerializer
    def put(self,request):

        user_id = request.query_params.get("user_id")
        try:
            passwords = request.data
            if passwords['new_password'] == passwords['confirm_password']:
                user = self.validator(data={"user_password":passwords['confirm_password']})
                if user.is_valid():
                    data = user.validated_data
                    salt = bcrypt.gensalt()
                    hashed_password = bcrypt.hashpw(data['user_password'].encode('utf-8'), salt)
                    data['user_password'] = hashed_password.decode('utf-8')
                    response = User().put(payload = data,user_id=user_id)
                    return Response(data={"status":'OK',"result":'Password changed','message':"SUCCESS"},status=status.HTTP_200_OK)
                else: 
                    return Response(data={"status":'ERROR',"result": user.errors,'message':"Invalid"},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={"status":'ERROR',"result": "Passwords are not matching",'message':"ERROR"},status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            print("-----EPTN----",e)
            return Response(data={"status":"ERROR","result":'','message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)
        
class LogInViewSet(APIView):
    validator = UserManagerSerializer
    user_model = UserModel
    def post(self,request):

        print('---------log_in------------',request.data)
        # Validate the request body
        user = self.validator(data=request.data)
        # if valid
        if user.is_valid():
            try:
                data = user.validated_data
                # Check whether the user exists, if not return user do not exists.
                if "user_phone_number" in data.keys():
                    user_data = User().get(filters={"user_phone_number" :data["user_phone_number"]})[0]
                elif "user_email" in data.keys():
                    user_data = User().get(filters={"user_email" :data["user_email"]})[0]

                print("--------user_data-----------",user_data)
                if user_data:
                    if bcrypt.checkpw(data['user_password'].encode('utf-8'), user_data['user_password'].encode('utf-8')):
                        payload ={
                            'id' : user_data["user_id"],
                            'uuid' : str(user_data['uuid']),
                            'expiry' : str(datetime.datetime.now()),
                            'status' : True
                        }
                        # Generate and return token
                        token = jwt.encode(payload,key =settings.SECRET_KEY,algorithm='HS256')
                        #TODO store token in redis
                        user_data.pop('user_password')
                        
                        return Response(data={"status":"OK","result":{'token':token,'user':user_data},'message':'SUCCESS'},status=status.HTTP_200_OK)
                else: 
                    return Response(data={"status":"ERROR","result":"",'message':'user not found'},status=status.HTTP_400_BAD_REQUEST)
                
            except Exception as e:
                print(e)
        else:
            return Response(data={"status":"ERROR","result":"",'message':'Invalid data'},status=status.HTTP_400_BAD_REQUEST)
        
class LogOutViewSet(APIView):

    def post(self,request):
        try :
            # Get tokens from request
            token = request.headers.get("Authorization").split(' ')[1]
            # Get blacklisted tokens
            black_listed= RedisManager().get(key= 'black-listed-tokens')
            # Add current token to blacklisted token.
            if black_listed:
                if black_listed['access']:
                    black_listed['access'].append(token)
                    RedisManager().upsert(value=black_listed,key='black-listed-tokens')
                else:
                    black_listed ={'access':[token]}
                    RedisManager().append(value=black_listed,key='black-listed-tokens')
            else:
                black_listed ={'access':[token]}
                RedisManager().upsert(value=black_listed,key='black-listed-tokens')
            # Return response
            
            return Response(data={"status":"ok","result":"",'message':'Successfully signed out'},status=status.HTTP_200_OK)
        except:
            return Response(data={"status":"ERROR","result":"",'message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

class RequestOTPViewSet(APIView):
    
    def post(self,request):
        try :
            # Get user email id 
            email = request.data.get("user_email")
            # Generate OTP 
            otp = OTPGenerator().ganerate()
            message = """\
            Subject: YOUR OTP

            Your OTP for verification is """+str(otp)+"""."""
            # Send Otp
            Email().send(receiver_email=email,message=message)
            return Response(data={"status":"OK","result":"OTP has been sent",'message':'SUCCESS'},status=status.HTTP_200_OK)
        except:
            return Response(data={"status":"ERROR","result":"",'message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPViewSet(APIView):
    
    def post(self,request):
        try :
            otp = request.data.get("otp")
            result = OTPGenerator().verify(otp=otp)
            if result:
                return Response(data={"status":"OK","result":result,'message':'Verified'},status=status.HTTP_200_OK)
            return Response(data={"status":"ERROR","result":'','message':'Invalid OTP'},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(data={"status":"ERROR","result":"",'message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)

class NotificationViewSet(APIView):
    
    def post(self,request):
        try :
            notification_data = request.data
            EmailNotifications().send(user_ids=notification_data["user_ids"],message=notification_data["message"],subject=notification_data["subject"])
            return Response(data={"status":"OK","result":'Notification sent','message':'SUCCESS'},status=status.HTTP_200_OK)
        except:
            return Response(data={"status":"ERROR","result":"",'message':'ERROR'},status=status.HTTP_400_BAD_REQUEST)
        
