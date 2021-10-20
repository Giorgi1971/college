from django.urls import path
from user import forms
from . import views
from django.contrib.auth import views as auth_views


app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.TeacherListView.as_view(), name='teachers'),
    path('teacher/<int:pk>', views.TeacherDetailView.as_view(), name='teacher'),
    path('groups', views.GroupListView.as_view(), name='groups'),
    path('group/<int:pk>', views.GroupDetailView.as_view(), name='group'),
    path('pupils', views.PupilListView.as_view(), name='pupils'),
    path('pupil/<int:pk>', views.PupilDetailView.as_view(), name='pupil'),
    path('login/', auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view() , name='signup'),
]