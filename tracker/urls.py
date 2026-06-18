from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('setup/', views.setup_profile, name='setup_profile'),
    path('add-water/', views.add_water, name='add_water'),
    path('delete-water/<int:intake_id>/', views.delete_water, name='delete_water'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),  # ← НОВАЯ СТРОЧКА
]