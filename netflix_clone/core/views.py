from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Movie, Originals, TopRatedMovie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)

def home(request):
    movies = Movie.objects.all()
    originals = Originals.objects.all()
    top_rated_movies = TopRatedMovie.objects.all()
    context = {
        'movies': movies,
        'originals': originals,
        'top_rated_movies': top_rated_movies,
    }
    return render(request, 'home.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Invalid Data')
            return redirect('login')
    return render(request, 'login.html')

def movie(request):
    return render(request, 'movie.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == '':
            messages.info(request,'Password cannot be blank. Try again!')
            return redirect('signup')
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exsits')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'A User with the same username already exists. Try a different Username')
                return redirect('signup')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            # log user in
            user_login = auth.authenticate(username=username, password=password)
            auth.login(request, user_login)
            return redirect('/')
        else:
            messages.info(request, 'Passwords Not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
