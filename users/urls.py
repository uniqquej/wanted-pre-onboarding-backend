from django.urls import path
from users import views

urlpatterns = [
    path('sign-up/',views.SignUpView.as_view(),name='sign_up')
]
