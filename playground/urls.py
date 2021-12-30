from django.urls import path
from . import views

# url configuration for this app
# you need to import this to main url configuration of the project (/storefront/urls.py)
urlpatterns = [
    path('hello/', views.say_hello)
]
