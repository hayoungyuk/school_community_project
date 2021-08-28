from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Schoolapp,Tag
from .forms import SchoolappForm
from django.contrib.auth import get_user_model
from django.views.generic import ListView

# Create your views here.

def home(request):
    schoolapps = Schoolapp.objects.all()
    tag = Tag.objects.all()
    return render(request,'home.html',{'schoolapps':schoolapps, 'tag':tag})

def detail(request,id):
    schoolapp = get_object_or_404(Schoolapp, pk = id)
    return render (request, 'detail.html', {'schoolapp':schoolapp})

def new(request):
    if request.method == 'POST':
        form = SchoolappForm(request.POST,request.FILES)
        if form.is_valid():
            new_schoolapp = form.save (commit = False)
            new_schoolapp.pub_date = timezone.now()
            new_schoolapp.save()
            return redirect ('home')
    else:
        form = SchoolappForm()
        return render(request,'new.html',{'form':form})

def create(request):
    form = SchoolappForm(request.POST, request.FILES)
    if form.is_valid():
        new_schoolapp = form.save(commit=False, blank=True, null=True)
        new_schoolapp.pub_date = timezone.now()
        new_schoolapp.save()
        return redirect('detail',new_schoolapp.id)
    return redirect('home')

def edit(request,id):
    edit_schoolapp = get_object_or_404(Schoolapp, pk = id)
    if request.method == 'GET':
        form = SchoolappForm(instance = edit_schoolapp)
        return render(request,'edit.html', {'form':form})
    else:
        form = SchoolappForm(request.POST, request.FILES, instance = edit_schoolapp)
        if form.is_valid():
            edit_schoolapp = form.save(commit = False)
            edit_schoolapp.pub_date = timezone.now()
            edit_schoolapp.save()
        return redirect('home')

def delete(request,id):
    delete_ideaapp = Schoolapp.objects.get(id=id)
    delete_ideaapp.delete()
    return redirect('home')


