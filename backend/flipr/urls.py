from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]