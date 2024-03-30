from django.shortcuts import render,redirect
from . models import Movies
from . forms import MovieForm

# Create your views here.
def home(request):
    movies=Movies.objects.all()
    context={ 
             'movie_list':movies
             }
    return render(request,'home.html',context)

def detail(request,movie_id):
    movies=Movies.objects.get(id=movie_id)
    return render(request,'detail.html' ,{'movies':movies})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movies=Movies(name=name,desc=desc,year=year,img=img)
        movies.save()
    return render(request,'add.html')

def update(request,id):
    movies=Movies.objects.get(id=id)
    form= MovieForm(request.POST or None,request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movies':movies})

def  delete(request,id):
    if request.method=='POST':
        movies=Movies.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')


