from django.shortcuts import render
from databasestore.models import Customer
# Create your views here.
def show(request):
    records = Customer.objects.all()
    context = {'records':records}
    return render(request,'show.html',context)
