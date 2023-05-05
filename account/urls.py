from django.contrib import admin
from django.urls import path, include
from .views import(
    SingUp,
    VerifyOTPview,
    LoginView,
    ProfileView,
    ProfilePictureView,
    VerifiCationOtpSentView,
    my_view
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register(r"profile-picture", ProfilePictureView) 

urlpatterns = [
    path('my-view/', my_view, name='my_view'),
               
    path('sing-up/', SingUp.as_view()),
    path('verify/', VerifyOTPview.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('account-verify-code/', VerifiCationOtpSentView.as_view()),
]+router.urls