from django.urls import path, include

from guestbooksapp.views import index, record_add

urlpatterns = [
    path('', index, name='index'),
    path('records/add/', record_add, name='record_add')
]
