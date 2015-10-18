class AppConstants(object):
    DEFAULT_USER_PASSWORD = "=========="

    REG_EMAIL_LINK = "http://localhost:8000/login/modpass/%s/"

    DEFAULT_REG_EMAIL_INFO_DICT = {
        "subject": "Complete Registration | Email Verification",
        "message": "<a href='%s'>Click Here</a> to complete registration process." % REG_EMAIL_LINK,
        "from_email": "hihello2287@gmail.com"
    }

    SESSION_EXPIRY_SECONDS = 30
