from .user import User
from utility.email_client import Email

class EmailNotifications:

    def send(self,user_ids:list,message:str,subject:str):

        for user in user_ids:
            try:
                # Get the user data
                user_data = User().get(filters={'user_id':user})[0]
                # Set the email content
                content = """\
                Subject:"""+subject+"""\n
                
                """+message+"""."""
                # Send the email
                Email().send(receiver_email=user_data['user_email'],message=content)
                return True
            except Exception as e:
                print('------EmailNotifications-------',e)
                return False


