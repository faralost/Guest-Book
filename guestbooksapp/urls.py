from django.urls import path, include

from guestbooksapp.views import index, record_add, record_update

urlpatterns = [
    path('', index, name='index'),
    path('records/add/', record_add, name='record_add'),
    path('record/<int:pk>/update/', record_update, name='record_update'),
]
