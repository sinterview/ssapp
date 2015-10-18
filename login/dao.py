from django.contrib.auth.models import User


class UserDAO(object):
    def create_user(self, user_info_dict):
        user = User.objects.create_user(
            username = user_info_dict["username"],
            email = user_info_dict["email"],
            first_name = user_info_dict["first_name"],
            last_name = user_info_dict["last_name"],
            password = user_info_dict["password"]
        )

        return user

    def change_password(self, user_info_dict):
        user = User.objects.get(username = user_info_dict["username"])

        user.set_password(user_info_dict["password"])
        user.save()

        return user

