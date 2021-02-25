from django.shortcuts import render,redirect
from .models import Blog
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def home(request):
    blogs=Blog.objects.all().order_by('date')
    return render (request,'index.html',{'blogs':blogs})


def data(request,a):
    a=Blog.objects.get(title=a)
    return render(request,'blog_detail.html',{'b':a})


@login_required(login_url="/accounts/login/")
def create_article(request):
    if request.method=='POST':
        form=forms.CreateBlog(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('Harshit:home')
    else:
        form=forms.CreateBlog()
        return render(request,'article_create.html',{'form':form})


