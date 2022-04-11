from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("giris/",views.giris_islemleri,name="Giris"),
    path("kayit/",views.kayit,name="kayit"),
    path("cikis/",views.cikis,name="cikis"),
]