from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Product, Shopkeeper


def index_view(request):
    template_name = 'app1/index.html'
    if request.method == 'POST':
        val = request.POST.get('product_name', '')
        return render(request, 'app1/search.html',
                      {'form': Search(), 'product': Product.objects.filter(product_name__contains=val)})
    else:
        return render(request, template_name, {'product': Product.objects.all(), 'form': Search()})


def detail_view(request, pk):
    if request.method == 'POST':
        val = request.POST.get('product_name', '')
        return render(request, 'app1/search.html',
                      {'form': Search(), 'product': Product.objects.filter(product_name__contains=val)})
    else:
        return render(request, 'app1/details.html', {'product': Product.objects.get(pk=pk), 'form': Search()})


def search_view(request):
    if request.method == 'POST':
        val = request.POST.get('product_name', '')
        return render(request, 'app1/search.html', {'form': Search(), 'product': Product.objects.filter(product_name__contains=val)})


@login_required
def profile(request):
    user = request.user
    content = {'user': user}
    template = 'app1/profile.html'
    return render(request, template, content)


def signup(request):
    form = UserForms()
    if request.method == 'POST':
        f = UserForms(request.POST)
        if f.is_valid():
            name = request.POST.get('shopkeeper_name', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = Shopkeeper(shopkeeper_name=name, email=email,password=password)
            user.save()
            return HttpResponse('<h1>Save Success</h1>', {'form': form})
        else:
            return render(request, 'app1/index.html', {'product': Product.objects.all(),'form': Search()})
    else:
        return render(request, 'app1/signup.html', {'form': form})


def login(request):
    form = LoginForms()
    if request.method == 'POST':
        f = LoginForms(request.POST)
        if f.is_valid():
            email = f.cleaned_data['email']
            psd = f.cleaned_data['password']
            dbuser = Shopkeeper.objects.filter(email=email)
            dbpassword = Shopkeeper.objects.filter(password=psd)
            if dbuser and dbpassword:
                fm = ShopkeeperData()
                return render(request, 'app1/Profile_shopkeeper.html', {'form': fm, 'db':dbuser,'dbp': dbpassword})
            else:
                return HttpResponse('Login Failed')

        else:
            return render(request, 'app1/login.html', {'form': form})
    else:
        return render(request, 'app1/login.html', {'form': form})
