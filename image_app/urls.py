from django.urls import path

from .views import index, display_url


urlpatterns = [
     path('', index, name='home'),
     path('get_url/', display_url, name='upload')
]
