# -*- coding: utf-8 -*-
# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render
from journal import models
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib import auth
from journal.forms import add_task_form
import json
import datetime
from django.views.generic.edit import FormMixin
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def logout(request):
    auth.logout(request)
    return redirect("/")


class TaskList(ListView , FormMixin):

    model = models.Task
    template_name = "task_list.html"
    context_object_name = "tasks"
    form_class = add_task_form

    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context["form"] = self.get_form(form_class)
        return context

def get_ajax_login(request):
    ans = {}
    req = {}
    req['login'] = request.POST['login']
    req['password'] = request.POST['password']
    ans = valid_login(req)
    if(ans['status'] == 'ok'):
        user = auth.authenticate(username=req['login'], password=req['password'])
        if user is not None and user.is_active:
            auth.login(request, user)
            ans['username'] = user.username
        else:
            ans['status'] = 'fail'
    return HttpResponse(json.dumps(ans))

def login(request):
    login = request.POST['Email']
    password = request.POST['password']
    user = auth.authenticate(username=login, password=password)
    if user is not None and user.is_active:
            auth.login(request, user)
            return redirect("/tasks/")
    return redirect("/")

def add_task(request):
    if not(request.user.is_authenticated()):
        return redirect('/')
    tittle = request.POST['tittle']
    user = request.user.id
    body = request.POST['body']
    b2 = models.Task(tittle=tittle, body=body, pub_date=datetime.datetime.now(), user=models.CustomUser.objects.get(pk=user),
                     status_class="info", status_tittle="В обработке")
    b2.save()
    return redirect("/tasks/")

def main(request):
    context = {}
    if request.user.is_authenticated():
        return  redirect('/tasks/')
    form_class = self.get_form_class()
        context["form"] = self.get_form(form_class)
        return context
    return render(request, 'journal/auth.html', context)

