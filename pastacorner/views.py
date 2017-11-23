from django.shortcuts import render
from .models import Menu

# Create your views here.
def index(request):
    return render(request, 'pastacorner/index.html')


def about(request):
    context = {'CompanyInfo':['Address: 2211 S Josephine St, Denver, CO 80210','Hours of Operstion: 7:00am to 9:00pm']}
    return render(request, 'pastacorner/about.html',context)

def menu(request):
    foodmenu = Menu.objects.order_by("id")
    context = {'FoodMenu': foodmenu}
    return render(request, 'pastacorner/menu.html',context)

def gallary(request):
    return render(request, 'pastacorner/gallary.html')

def contact(request):
    return render(request, 'pastacorner/contact.html')
