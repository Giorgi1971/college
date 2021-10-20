from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

def index(request):
    return render(request, 'user/index.html',context={'index':'from index'})


from django.conf.urls import url
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth
from django.http import request
# Create your views here.
from . models import *
from django.views import generic


def index(request):
    template_name = 'user/index.html'
    groups = Group.objects.all()
    return render(request, template_name,{"groups":groups})


class TeacherListView(generic.ListView):
    # model = Teacher
    # template_name = 'intst/teacher_list.html'
    # context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Teacher.objects.all()


class TeacherDetailView(generic.DetailView):
    model = Teacher


class GroupListView(generic.ListView):
    def get_queryset(self):
        return Group.objects.all()


class GroupDetailView(generic.DetailView):
    model = Group


class PupilListView(generic.ListView):
    def get_queryset(self):
        return Pupil.objects.all()


class PupilDetailView(generic.DetailView):
    model = Pupil


class SignUp(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/signup.html'
