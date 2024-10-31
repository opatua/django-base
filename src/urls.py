from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from src import views

router = DefaultRouter(trailing_slash=False)
router.register(r"user", views.UserView, "user")

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("sign-in", views.SignInView.as_view(), name="sign-in"),
    re_path(r"^", include(router.urls)),
]
