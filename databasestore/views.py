from django.shortcuts import render
from .models import Customer
# Create your views here.
def main(request):
    return render(request,'main.html')

def savedata(request):
    name=request.POST['name']
    password=request.POST['password']
    phone = request.POST['phone']
    address= request.POST['address']

    Customer(name=name, password=password, phone=phone, address=address).save()

    return render(request, 'final.html')