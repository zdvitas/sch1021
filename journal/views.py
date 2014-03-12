from django.shortcuts import render
from journal import  models
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib import  auth
# Create your views here.

def valid_login(data):
    response = {}
    response['status'] = 'ok'
    response['login_err'] = 'ok'
    response['pass_err'] = 'ok'
    if(data['login'] == ''):
        response['status'] = 'bad'
        response['login_err'] = 'not'
    if(data['password'] == ''):
        response['status'] = 'bad'
        response['pass_err'] = 'not'
    return response


def valid_reg(data):
    response = {}
    response['status'] = 'ok'
    response['login_err'] = 'ok'
    response['pass_err'] = 'ok'
    response['email_err'] = 'ok'
    if(data['login'] == ''):
        response['status'] = 'bad'
        response['login_err'] = 'not'
    if(data['password'] == ''):
        response['status'] = 'bad'
        response['pass_err'] = 'not'
    if(data['email'] == ''):
        response['status'] = 'bad'
        response['email_err'] = 'not'
    return response

def logout(request):
    auth.logout(request)
    return redirect("/")


class TaskList(ListView):

    model = models.Task
    template_name = "task_list.html"
    context_object_name = "tasks"


    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        context["form"] = "test"
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



def main(request):
    context = {}
    if request.user.is_authenticated():
        return  redirect('/tasks/')

    return render(request, 'journal/auth.html', context)

