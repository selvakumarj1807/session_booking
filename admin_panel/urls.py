from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login_view"),
    path('create_user/', views.create_user, name='create_user'),
    path('create_session/', views.create_session, name='create_session'),
    path('user_edit/<int:id>', views.user_edit, name='user_edit'),
    path('user_delete/<int:id>', views.user_destroy, name='user_destroy'),
    path('session_edit/<int:id>', views.session_edit, name='session_edit'),
    path('session_delete/<int:id>', views.session_delete, name='session_delete'),
]
