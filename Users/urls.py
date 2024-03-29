from django.urls import include, path

from . import views

urlpatterns = [
    path("logout/", views.logoutUser, name="logout"),
    path("login/", views.loginUser, name="login"),
    path("register/", views.registerUser, name="register"),
    path("account/", views.userAccount, name="account"),
    path("edit_account/", views.editAccount, name="edit_account"),
    path("api/", include("Users.api.urls")),
]
