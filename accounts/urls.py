from django.urls import path
from .views import register_user, user_login, user_logout
from accounts import views
from .views import CustomUserListCreate, CustomUserRetrieveUpdateDestroy


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_role/', views.add_role),
    path('fetch_all_roles/', views.fetch_all_roles),
    path('fetch_single_role/<int:role_id>/', views.fetch_single_role),
    path('update_role/<int:role_id>/', views.update_role),
    path('delete_role/<int:role_id>/', views.delete_role),
    path('users/', CustomUserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroy.as_view(), name='user-detail'),
   
]