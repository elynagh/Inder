from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.splash, name='splash'),
    path('reports/', views.reports, name='reports'),
    path('logout/', views.logout, name='logout'),
    path('complete_profile/', views.complete_profile, name='complete_profile'),
]