from django.shortcuts import redirect, render
from . models import Booking, Contact, Hotels, Image
from django.http.response import HttpResponse
from django.shortcuts import render
from . models import Contact, Image
from django.contrib import messages
from .forms import BookForm
import razorpay
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

@login_required(login_url='../login/')
def hotel(request,myid):
    hott = Hotels.objects.all()
    return render(request, "home/hotel.html",{'hott':hott})

@login_required(login_url='../login/')
def hotel_view(request,myid,myyid):
    hot = Hotels.objects.filter(id=myyid)
    return render(request, "home/hotel_view.html",{'hot':hot[0]})


@login_required(login_url='../login/')
def book(request,myid):
    disc = Image.objects.filter(id=myid)
    if request.method == "POST":
        form=BookForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            print('ret 1')
            return render(request, "home/payment.html",{'disc':disc[0],'obj':obj})
    else:
        form=BookForm()
        print('ret2')
    return render(request, "home/book.html",{'disc':disc[0],"form":form})

@login_required(login_url='../login/')
def discover(request,myid):
    disc = Image.objects.filter(id=myid)
    return render(request, "home/discover.html",{'disc':disc[0]})

@login_required(login_url='../login/')
def payment(request,myid,myyid):
    img = Image.objects.filter(id=myid)
    hot = Hotels.objects.filter(id=myyid)


    # val2 = request.GET['']
    if request.method == 'POST':
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_DGfQjUNUrMSEGh','kFZaSzxkXX0EMDhGMJSA8VHn'))
        payment = client.orders.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        return render(request, "home/payment.html",{'payment_id':payment['id']})
    return render(request, "home/payment.html",{'img':img[0],'hot':hot[0]})


@login_required(login_url='../login/')
def search(request):
    ser = request.GET.get('search').lower()
    dests=[item for item in Image.objects.all() if ser in item.place.lower()] #is list me or laga laga ke aur bhi cheeze add kr skte he jisme search krna ho https://www.youtube.com/watch?v=X7aj5V4kJJ0
    return render(request, "home/search.html",{'dests' : dests})

@login_required(login_url='../login/')
def hotel_search(request):
    ser = request.GET.get('search').lower()
    dests=[item for item in Hotels.objects.all() if ser in item.hotel_name.lower()] #is list me or laga laga ke aur bhi cheeze add kr skte he jisme search krna ho https://www.youtube.com/watch?v=X7aj5V4kJJ0
    return render(request, "home/hotel_search.html",{'dests' : dests})

@login_required(login_url='../login/')
def tour(request):
    tours = Image.objects.all()
    return render(request, "home/tours.html",{'tours':tours})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name",'')
        email = request.POST.get("email",'')
        subject = request.POST.get("name",'')
        message = request.POST.get("name",'')
        cont = Contact(name = name , email = email , subject = subject , message = message)
        cont.save()
        messages.success(request,"Your Form is submitted successfully , we will contact u soon!!!")
    return render(request,"home/contact.html")


