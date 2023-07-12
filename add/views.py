from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import Users
# Create your views here.
def addExpense(request):
    return render(request, 'add/addExpense.html')

def saveExpense(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(name)
        


        return redirect('addExpense')
    else:
        return redirect('addExpense')
    

