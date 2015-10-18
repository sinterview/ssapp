class LoginUtils(object):
    def add_user_in_session(self, request_obj, user_obj):
        request_obj.session["username"] = user_obj.username
        request_obj.session["first_name"] = user_obj.first_name
        request_obj.session["last_name"] = user_obj.last_name


    def get_user_from_session(self, request_obj):
        user_info_dict = {}

        user_info_dict["username"] = request_obj.session["username"]
        user_info_dict["first_name"] = request_obj.session["first_name"]
        user_info_dict["last_name"] = request_obj.session["last_name"]

        return user_info_dict
