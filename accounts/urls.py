from django.urls import path
from .views import register_user, user_login, user_logout
from accounts import views
from .views import CustomUserListCreate, CustomUserRetrieveUpdateDestroy
from .views import hello_brother

from .views import database_name

urlpatterns = [
    path('register/', register_user, name='register'),
      path('hello/', hello_brother, name='hello'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_role/', views.add_role),
    path('fetch_all_roles/', views.fetch_all_roles),
    path('fetch_single_role/<int:role_id>/', views.fetch_single_role),
    path('update_role/<int:role_id>/', views.update_role),
    path('delete_role/<int:role_id>/', views.delete_role),
        path('database-name/', database_name, name='database-name'),
    path('users/', CustomUserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroy.as_view(), name='user-detail'),
   
]