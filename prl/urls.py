from django.contrib import admin
from django.urls import path
from prl import views

admin.site.site_header = 'Oziel\'s Portfolio Administration'
admin.site.site_title = 'Oziel\'s Portfolio Administration'

urlpatterns = [
    path('', views.Home, name='Main Homepage'),

    path('home/', views.Home, name='Main Homepage'),
    path('home', views.Home, name='Main Homepage'),


    path('about/', views.About, name='About Page'),
    path('about', views.About, name='About Page'),

    path('projects/', views.Projects, name='Projects Page'),
    path('projects', views.Projects, name='Projects Page'),

    path('contact/', views.ContactMe, name='Contact Page'),
    path('contact', views.ContactMe, name='Contact Page'),

    path('contact/success/', views.Success, name='Success Page'),
    path('contact/success', views.Success, name='Success Page'),
]
