from django.contrib.auth import authenticate
from django.core.mail import send_mail
from .dao import UserDAO
from .constants import AppConstants


class UserAuthenticationService(object):
    def authenticate(self, user_info_dict):
        user = authenticate(
            username = user_info_dict["username"],
            password = user_info_dict["password"]
        )

        if user is not None:
            print "Valid User"
            return user

        else:
            print "Invalid User"
            return False



class UserRegistrationService(object):
    def create_user(self, user_info_dict):
        user_info_dict["password"] = AppConstants.DEFAULT_USER_PASSWORD
        new_user = UserDAO().create_user(user_info_dict)
        return new_user

    def change_password(self, user_info_dict):
        registered_user = UserDAO().change_password(user_info_dict)
        return registered_user



class EmailService(object):
    def send_email(self, email_info_dict):
        send_mail(
            subject = email_info_dict["subject"],
            message = email_info_dict["message"],
            from_email = email_info_dict["from_email"],
            recipient_list = [email_info_dict["to_email"]],
            fail_silently = False
        )

        return True
