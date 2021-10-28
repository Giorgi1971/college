from django.urls import path
from user import forms
from . import views
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('createteacher/', TeacherCreateView.as_view(), name='createteacher'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher'),
    path('updateteacher/<int:pk>/', TeacherUpdateView.as_view(), name='updateteacher'),
    path('deleteteacher/<int:pk>/', TeacherDeleteView.as_view(), name='deleteteacher'),
    path('groups/', GroupListView.as_view(), name='groups'),
    path('group/<int:pk>/', GroupDetailView.as_view(), name='group'),
    path('pupils/', PupilListView.as_view(), name='pupils'),
    path('pupil/<int:pk>/', PupilDetailView.as_view(), name='pupil'),
    path('login/', auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view() , name='signup'),
]