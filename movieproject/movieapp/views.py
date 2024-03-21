from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse

from .forms import MovieForm
from .models import Movie, Category, Rating, Review
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import ReviewForm, RatingForm


# Create your views here.

def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render (request,'index.html',context)
    
def details(request,movie_id):
    m=Movie.objects.get(id=movie_id)
    reviews = Review.objects.filter(movie=m)
    ratings = Rating.objects.filter(movie=m)
    return render (request,"details.html",{'movie':m,'reviews': reviews, 'ratings': ratings})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        original_slug = request.POST.get('slug',)
        desc=request.POST.get('desc',)
        release=request.POST.get('release',)
        actors=request.POST.get('actors',)
        trailer_link=request.POST.get('trailer_link',)
        img = request.FILES['img']
        category_name = request.POST.get('category').strip()
        try:
            category = Category.objects.get(category_name__iexact=category_name)
        except Category.DoesNotExist:
            return HttpResponse("The selected category does not exist. Please choose an existing category.")

        slug = original_slug
        count = 1
        while Movie.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{count}"
            count += 1
        movie=Movie(name=name,slug=slug,desc=desc,release=release,img=img,actors=actors,category=category,trailer_link=trailer_link)
        movie.added_by = request.user
        movie.save()
        return redirect('home/')
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    if request.user == movie.added_by:
        form=MovieForm(request.POST or None,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render (request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        if request.user == movie.added_by:
            movie.delete()
            return redirect('/')
    return render (request,'delete.html')

def category(request,c_slug=None):
    c_page = None
    movie_list = None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movie_list=Movie.objects.all().filter(category=c_page)
    else:
        movie_list=Movie.objects.all()
    return render(request,"category.html",{'category':c_page,'movies':movie_list})

def home(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

def post_review(request, movie_id):
    if request.method == "POST":
        movie = Movie.objects.get(id=movie_id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movieapp:details', movie_id=movie_id)
    else:
        form = ReviewForm()
    reviews = Review.objects.all()
    return render(request, 'post_review.html', {'form': form,'reviews':reviews})

def post_rating(request, movie_id):
    if request.method == "POST":
        movie = Movie.objects.get(id=movie_id)
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.movie = movie
            rating.user = request.user
            rating.save()
            return redirect('movieapp:details', movie_id=movie_id)
    else:
        form = RatingForm()
    ratings = Rating.objects.all()
    return render(request, 'post_rating.html', {'form': form,'ratings':ratings})

def search(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.filter(Q(name__icontains=query) | Q(category__category_name__icontains=query))
    return render(request, 'searchresults.html', {'query': query, 'movies': movies})
