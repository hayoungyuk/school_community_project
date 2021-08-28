from django.urls import path
from .views import * #views.py ,다음에 추가시켜주는

urlpatterns = [
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('register/',register_view,name="signup")
]