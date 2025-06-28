from django.urls import path
from . import views
from dashboard import views as dash_views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),

    path('displayprofile/',views.profile_view,name='displayprofile'),
    path('editprofile/<int:user_id>/',views.profile_edit,name='editprofile'),
    
     path('create/', views.create_task, name='create_task'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/complete/', views.mark_completed, name='mark_completed'),

    ]
