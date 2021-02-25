from django.conf.urls import url
from .import views
app_name="accounts"


urlpatterns=[
    url('signup',views.signups,name="signup"),  
    url('login',views.logins,name='login'),
    url('logout',views.logouts,name='logout')
]