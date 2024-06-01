"""
URL configuration for sistemERP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MarketingModule import views;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('marketing/', views.marketing, name='marketing'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('view_contacts/', views.view_contacts, name='view_contacts'),
    path('edit_contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('create_group/', views.create_group, name='create_group'),
    path('view_groups/', views.view_groups, name='view_groups'),
    path('view_group_members/<int:group_id>/', views.view_group_members, name='view_group_members'),
    path('delete_group/<int:group_id>/', views.delete_group, name='delete_group'),
    path('marketing_por_email/', views.marketing_por_email, name='marketing_por_email'),
    path('crear_campaña_marketing/', views.crear_campaña_marketing, name='crear_campaña_marketing'),
]
