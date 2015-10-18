from django.conf.urls import url
from . import views

urlpatterns = [
# url(r'^(?P<username>\w+)/blog/', include('foo.urls.blog')),
    url("^login/$", views.login, name = "login"),
    url("^register/$", views.register, name = "register"),
    url("^modpass/(?P<username>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)/$", views.modifypassword, name = "modifypassword"),
    url("^home/$", views.home, name = "home"),

    url("^loginapi/$", views.loginapi, name = "loginapi"),
    url("^registerapi/$", views.registerapi, name = "registerapi"),
    url("^modpassapi/$", views.modifypassapi, name = "modifypassapi"),
    url("^logoutapi/$", views.logoutapi, name = "logoutapi"),

    url("^$", views.register, name = "register")
]
