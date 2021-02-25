from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings
from . import views

app_name="Harshit"

urlpatterns = [
    path("",views.home,name="home"),
    path("blog/<str:a>",views.data,name="blogs"),
    path('create',views.create_article,name="create")

]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
