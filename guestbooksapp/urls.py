from django.urls import path, include

from guestbooksapp.views import index, record_add, record_update, record_delete

urlpatterns = [
    path('', index, name='index'),
    path('records/add/', record_add, name='record_add'),
    path('record/<int:pk>/update/', record_update, name='record_update'),
    path('record/<int:pk>/delete/', record_delete, name='record_delete'),
]
