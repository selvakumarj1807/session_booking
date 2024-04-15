from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login_view"),
    path('user_dashboard/<str:username>/', views.user_dashboard, name='user_dashboard'),
    path('book_session', views.book_session, name='book_session'),
    
]
