from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .service import *
from .constants import AppConstants
from .utils import LoginUtils

# Create your views here.

@require_http_methods(["GET", "POST"])
def login(request):
    return render(request, "login/login.html", None)


@require_http_methods(["GET", "POST"])
def register(request):
    return render(request, "login/register.html", None)


@require_http_methods(["GET", "POST"])
def modifypassword(request, username):
    view_context = {
        "username": username,
        "message": "Hello"
    }

    return render(request, "login/password.html", view_context)


@require_http_methods(["GET", "POST"])
def home(request):
    if not request.user.is_authenticated():
        return redirect("/login/login")

    else:
        view_context = LoginUtils().get_user_from_session(request)
        return render(request, "login/home.html", view_context)


@require_http_methods(["POST"])
def loginapi(request):
    valid_request = True
    user_info_dict = {}

    if request.POST.has_key("username") \
            and request.POST.has_key("password"):
        user_info_dict["username"] = request.POST["username"]
        user_info_dict["password"] = request.POST["password"]

        logged_in_user = UserAuthenticationService().authenticate(user_info_dict)
        if logged_in_user:
            auth.login(request, logged_in_user)
            LoginUtils().add_user_in_session(request, logged_in_user)
            request.session.set_expiry(AppConstants.SESSION_EXPIRY_SECONDS)
            return redirect("/login/home/")

        else:
            return redirect("/login/login/")

    else:
        valid_request = False
        return redirect("/login/login/")


@require_http_methods(["POST"])
def registerapi(request):
    valid_request = True
    user_info_dict = {}

    if request.POST.has_key("email") \
            and request.POST.has_key("first_name") \
            and request.POST.has_key("last_name"):
        user_info_dict["username"] = request.POST["email"]
        user_info_dict["email"] = request.POST["email"]
        user_info_dict["first_name"] = request.POST["first_name"]
        user_info_dict["last_name"] = request.POST["last_name"]

        email_info_dict = AppConstants.DEFAULT_REG_EMAIL_INFO_DICT
        email_info_dict["to_email"] = request.POST["email"]
        email_info_dict["message"] = email_info_dict["message"] % request.POST["email"]

        try:
            UserRegistrationService().create_user(user_info_dict)
            EmailService().send_email(email_info_dict)

        except Exception as exception:
            type(exception).__name__

    else:
        valid_request = False

    return redirect("/login/login/")


@require_http_methods(["POST"])
def modifypassapi(request):
    valid_request = True
    user_info_dict = {}

    if request.POST.has_key("username") \
            and request.POST.has_key("password"):
        user_info_dict["username"] = request.POST["username"]
        user_info_dict["password"] = AppConstants.DEFAULT_USER_PASSWORD

        logged_in_user = UserAuthenticationService().authenticate(user_info_dict)
        if logged_in_user:
            user_info_dict["password"] = request.POST["password"]
            UserRegistrationService().change_password(user_info_dict)

            logged_in_user = UserAuthenticationService().authenticate(user_info_dict)
            auth.login(request, logged_in_user)
            LoginUtils().add_user_in_session(request, logged_in_user)
            request.session.set_expiry(AppConstants.SESSION_EXPIRY_SECONDS)
            return redirect("/login/home/")

        else:
            return redirect("/login/login/")

    else:
        valid_request = False
        return redirect("/login/login/")


@require_http_methods(["GET"])
def logoutapi(request):
    auth.logout(request)
    return redirect("/login/login/")
