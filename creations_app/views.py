from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
import random
from django.core.paginator import Paginator, EmptyPage

# Create your views here.

def index(request):
    context = {
        'user' : User.objects.all()
    }
    return render(request, "default.html", context)

def register_page(request):
    context = {
        'user' : User.objects.all()
    }
    return render(request, "register.html", context)

# renders login page 
def login_page(request):
    context = {
        'user' : User.objects.all()
    }
    return render(request, "login.html", context)

# renders home page
def home_page(request):
    if not 'user_id' in request.session:
        return redirect('/')
    posts = Character.objects.all()

    paginator = Paginator(posts, 1)

    page = request.GET.get('page')

    posts = paginator.get_page(page)

    context = {
        "user": User.objects.get(id = request.session['user_id']),
        'posts': posts
    }
    return render(request, 'main.html', context )

#renders profile page
def profile(request, id):
    context = {
        "characters" : Character.objects.all(),
        'profile' : User.objects.get( id = id)
    }
    return render(request, "profile.html", context)

def creator_profile(request, id):
    context ={
        "profile" : User.objects.get(id=id)
    }
    return render(request, "creator_profile.html", context)

def image_view_page(request, id):
    context= {
        "char":Character.objects.get(id=id)
    }
    return render(request, "image_view.html", context)

# renders characters creation page
def creation(request):
    context = {
        "characters" : Character.objects.all(),
        'user' : User.objects.get(id = request.session['user_id'])
    }
    return render(request, "character_creation.html", context)

# creates users
def create_user(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            users = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], username = request.POST['username'], email = request.POST['email'], password = pw_hash, profile_pic = request.FILES['profile_pic'])
            request.session['user_id']  = users.id
            messages.success(request, "You have Successfully Logged In")
            return redirect('/home')
            print('*'*50)
            print('user made')
        return redirect('/')

def profile_info(request):
    if request.method == "POST":
        profile_stuff = Profile.objects.create(my_profile = User.objects.get(id = request.session['user_id']), profile_banner = request.FILES['profile_banner'], instagram = request.POST['instagram'], facebook = request.POST['facebook'], youtube = request.POST['facebook'])
    return redirect("/home")
# creates characters
def create_character(request):
    if request.method == "POST":
        errors = Character.objects.character_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
        else:
            Character.objects.create(name = request.POST['name'], date_of_birth = request.POST['date_of_birth'], powers = request.POST['powers'], bio = request.POST['bio'], pic = request.FILES['pic'], creator = User.objects.get(id = request.session['user_id']))
        return redirect('/creation')

# render edit page
def edit_profile(request, profile_id):
    context = {
        "profile" : User.objects.get(id = request.session['user_id'])
    }
    return render(request, "edit_profile.html", context)

def edit(request):
    profile = User.objects.get(id = request.session['user_id'])
    context = {
        "profile" : profile
    }
    if request.method == "POST":
        profile.username = request.POST['username']
        profile.email = request.POST['email']
        profile.save()
    return redirect('/home')

def pic_update(request):
    profile = User.objects.get(id = request.session['user_id'])
    context = {
        "profile" : profile
    }
    print('*'*30)
    print('starting update')
    if request.method == "POST":
        profile.profile_pic = request.FILES['profile_pic']
        profile.save()
    print('*'*30)
    print('update saved')
    return redirect('/home')

def view_saved(request):
    context = {
        "user" : User.objects.get(id = request.session['user_id']),
        "characters" : Character.objects.all()
    }
    return render(request, "saved_post.html", context)

def save_art(request, art_id):
    print('*'*30)
    print('grabbing user now')
    print('*'*30)
    user = User.objects.get(id = request.session['user_id'])
    print('*'*30)
    print('grabbing art now')
    print('*'*30)
    art = Character.objects.get(id = art_id)
    print('*'*30)
    print('starting to save ')
    print('*'*30)
    user.save_post.add(art)
    print('*'*30)
    print('successfully saved')
    print('*'*30)
    return redirect('/home')

def unsave_art(request, art_id):
    user = User.objects.get(id = request.session['user_id'])
    print('*'*30)
    print('grabbed user_is')
    print('*'*30)
    art = Character.objects.get(id=art_id)
    print('*'*30)
    print('successfully grabbed art')
    print('*'*30)
    user.save_post.remove(art)
    print('*'*30)
    print('removed from saved')
    print('*'*30)
    return redirect('/home')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(username= request.POST['username'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/home')
            messages.error(request, 'Password Does Not Match')
        else:
            messages.error(request, "Username Does Not Exist")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def delete(request, char_id):
    char = Character.objects.get(id = char_id)
    if request.method == "POST":
        char.delete()
    return redirect("/home")