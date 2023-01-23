from django.shortcuts import render
from shop.models import Information
from shop.forms import createform
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    ins = Information.objects.all()
    return render(request, 'home.html', {'ins': ins})

def read(request, id):
    r = Information.object.get(id=id)
    return render(request, 'read.html', {'r': r} )

def create_form(request):
        context ={}
    # if request.method =="POST":
        form =createform(data=request.POST or None, files=request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
        context ={
            'form' : form
             }
        return render(request, 'create.html',context)



