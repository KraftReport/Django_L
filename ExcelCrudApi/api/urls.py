from django.urls import path

from api.views import get_user, create_user, get_all_user, get_user_by_id, update_user, delete_user

urlpatterns = [
    path('user',get_user,name='get_user'),
    path('create',create_user,name='create_user'),
    path('get-all',get_all_user,name='get_all_user'),
    path('get-by-id/<int:pk>',get_user_by_id,name='get_user_by_id'),
    path('update-by-id/<int:pk>',update_user,name='update_user'),
    path('delete-by-id/<int:pk>',delete_user,name='delete_user')
]