from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout 
# Create your views here.

def signups(request):

    if request.method=='POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('Harshit:home')

    form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


def logins(request):


    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:    
                return redirect('Harshit:home')

    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})    


def logouts(request):
    if request.method=='POST':
        logout(request)
        return redirect('Harshit:home')