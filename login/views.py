from home.forms import edituser
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# def login(request):
#     return render(request,"login/login.html")
# @login_required(login_url='../login/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username , password = password)
        print(password)
        if user is not None:
            auth.login(request,user)
            return redirect('../tours/')
        else:
            print('invalid')
    return render(request,'login/login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if len(username)>10:
            print("chota username dalo")
            return redirect('signup')
        if len(password)<8:
            print("bada password daal le ")
            return redirect('/')

        if not username.isalnum():
            print("dollar mat likh")
            return redirect('/')

        if password != password1:
            print("password doesnt match")
            return redirect('/')

        if User.objects.filter(username=username).exists():
            print('sorry')
        else:
            user = User.objects.create_user( username = username, first_name = first_name,last_name = last_name , email=email , password = password)
            user.save()
            return redirect('/login/')




    return render(request,'login/signup.html')

@login_required(login_url='../login/')
def profile(request):
    return render(request , "login/profile.html")


@login_required(login_url='../login/')
def edit(request):
    if request.method == 'POST':
        form = edituser(request.POST , instance=request.user)

        if form.is_valid():
            form.save()
            return(redirect('/'))
    else:
        form = edituser(instance = request.user)
        args = {'form':form}
        return render(request ,"login/editprofile.html",args)

def logout(request):
    auth.logout(request)
    return redirect('/')