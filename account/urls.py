from django.urls import path, include

urlpatterns = [
    # path("login",Login.as_view())
    path("accounts/", include("django.contrib.auth.urls")),
]
