from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . forms import SportsForms
from sportsapp.models import Sports

# Create your views here.
def sports(request):
    sports=Sports.objects.all()
    context={
        'sports_list':sports
    }

    return render(request, "sport.html", context)

def details(request, sports_id):
    sports=Sports.objects.get(id=sports_id)

    return render(request, "details.html", {'sports':sports})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES['img']
        desc = request.POST.get('desc')
        country = request.POST.get('country')
        sports=Sports(name=name,img=img,desc=desc,country=country)
        sports.save();
        return redirect('/')
    return render(request, "add.html")

def update(request, sports_id):
    sports=Sports.objects.get(id=sports_id)
    forms=SportsForms(request.POST or None, request.FILES, instance=sports)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request, "update.html",{'forms':forms, 'sports':sports})

def delete(request, sports_id):
    if request.method == 'POST':
        sports=Sports.objects.get(id=sports_id)
        sports.delete()
        return redirect('/')
    return render(request, "delete.html")
