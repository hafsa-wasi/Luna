from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from main.models import post, likedpost, comments
from .models import profile
from django.db.models import Q
from .forms import profileForm



def signin(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                pass
            else:
                login(request,user)
                return redirect('user_home')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'user/login.html', {'login_form' : login_form, 'sign':'0'})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def user_home(request):
    # print(request.user)
    editor2 = post.objects.filter(rating =10).order_by('-updated_at')[:5]
    popular = post.objects.filter(Q(rating__gte=7) | Q(rating__lt=10))[:5]
    recent = post.objects.order_by('-updated_at')[:5]
    comment = comments.objects.order_by('-comment_date')[:3]
    user_liked_listing = likedpost.objects.filter(profile = request.user.profile).values_list('post')
    liked_listings_ids= [l[0] for l in user_liked_listing]
    return render(request, 'main/index.html',{'sign': '1', 'editor2':editor2, 'popular':popular, 'recent':recent, 'liked_listings_ids':liked_listings_ids, 'comment':comment})
    

class register(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'user/signup.html',{'register_form': register_form,'sign':'0'})

    def post(self,request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request,user)
            #messages.success(request, f'User{user.username} registered successfully.')
            return redirect('user_home')
        else:
            #messages.error(request, f'An error occured while registerng')
            return render(request, 'user/signup.html',{'register_form': register_form, 'sign':'0'})
    

def user_profile(request,):
    name = request.user
    check = User.objects.filter(username = name)
    if not check:
        return redirect('signin')
    main = User.objects.get(username = name)
    sub = profile.objects.get(user = name)
    liked_post = likedpost.objects.filter(profile = name.profile)
    my_post = post.objects.filter(author = name.profile)
    # user_liked_listing = likedpost.objects.filter(profile = request.user.profile).values_list('post')           
    # liked_listings_ids= [l[0] for l in user_liked_listing]
    return render(request, 'user/profile.html' ,{'sub': sub, 'main': main, 'liked_post':liked_post, 'my_post':my_post, 'sign':'1'})

def update_profile(request,):
    if request.method == 'POST':
          name = request.user
          person = profile.objects.get(user=name)
          profile_form = profileForm(request.POST,request.FILES, instance=person)
          password_form = PasswordChangeForm(user=request.user, data=request.POST or None)
          if profile_form.is_valid() and password_form.is_valid():
            profile_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            return redirect('profile')
    elif request.method == 'GET':
       name = request.user
       person = profile.objects.get(user=name)
    #    print(person.user.username)
       profile_form = profileForm(instance=person) 
       password_form = PasswordChangeForm(user=request.user)    
    return render(request, 'user/update.html',{'profile_form':profile_form,'password_form':password_form, 'sign':'1'})
    
def delete_profile(request,):
    name = request.user
    person = profile.objects.get(user=name)
    user = User.objects.get(username=name)
    person.delete()
    user.delete()
    return redirect('index')
    




