from django.urls import path

from account import views as user_view
from account.views import register


urlpatterns = [
   
    path('register/', user_view.register, name='registration-user'),
   
    
    
]
 