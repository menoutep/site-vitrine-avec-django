from django.shortcuts import render, redirect
from .models import Images,Portfolio, Service, Team
from .forms import MessageForm
from django.http import HttpResponseRedirect

# Create your views here.

def hello(request):
    teams=Team.objects.all()
    services=Service.objects.all()
    portfolios=Portfolio.objects.all()
    imageAbout=Images.objects.get(title="nav")
    if request.method=='POST':
        
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=MessageForm
    
    context={
        'form':form,
        'image':imageAbout,
        'portfolios':portfolios,
        'services':services,
        'teams':teams
    }
    
    return render(request,'listings/index.html.twig',context)