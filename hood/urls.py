from django.urls import re_path,path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns=[
    # re_path('^$',views.welcome,name = 'welcome'),
    path('', views.home, name = 'home'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html')),
    path('profile/', views.profile, name='profile'),
    path('hood/', views.hoods, name='hood'),
    path('single_hood/<hood_id>', views.single_hood, name='single-hood'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('new-hood/', views.new_hood, name='new-hood'),
    path('<hood_id>/news', views.news, name='news'),                    
    path('<hood_id>/business',views.business,name='business'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('businesses/<hood_id>', views.businesses, name='businesses'),
    path('post/<hood_id>', views.post, name='post'),
    path('search/',views.search_results,name='search_results'),

]