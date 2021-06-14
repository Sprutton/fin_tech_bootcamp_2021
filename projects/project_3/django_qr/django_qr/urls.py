
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from apps.qr import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
]
