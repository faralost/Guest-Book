from django.urls import path, include

from guestbooksapp.views import index

urlpatterns = [
    path('', index, name='index'),
]
