from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django import forms
from .forms import postForm, commentForm
from user.models import profile
from .models import post, likedpost, comments
from django.db.models import Q
import json
from django.conf import settings
import requests
import google.generativeai as genai 

## Loading gemini_api_key form .env
from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_API = os.getenv("GEMINI_API_key")
genai.configure(api_key=GEMINI_API)
model = genai.GenerativeModel('gemini-1.5-flash')



## Create your views here.
def index(request):
    editor2 = post.objects.filter(rating =10).order_by('-updated_at')[:5]
    popular = post.objects.filter(Q(rating__gte=7) | Q(rating__lt=10))[:5]
    recent = post.objects.order_by('-updated_at')[:5]
    comment = comments.objects.order_by('-comment_date')[:3]
#     user_liked_listing = likedpost.objects.filter(profile = request.user.profile).values_list('post')            'liked_listings_ids':liked_listings_ids
#     liked_listings_ids= [l[0] for l in user_liked_listing]
    return render(request, 'main/index.html' ,{'sign': '0', 'editor2':editor2, 'popular':popular, 'recent':recent, 'comment':comment})


def post_view(request, sign):
    if request.method == 'POST':
            if sign == '0':
                return redirect('signin')
            post_form = postForm(request.POST,request.FILES)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.author = request.user.profile
                post.save()
                return redirect('user_home')
            return render(request, 'main/list.html', {'post_form' : post_form} )
    elif request.method == 'GET':
        post_form = postForm()
    return render(request, 'main/list.html', {'post_form' : post_form, 'sign' : sign} )

def get_view(request, sign, id):
     #print(request.user)
     listing = post.objects.get(id=id)
     comment = comments.objects.filter(post=listing)
     liked_listings_ids=None
     if sign=='1':
        user_liked_listing = likedpost.objects.filter(profile = request.user.profile).values_list('post')
        liked_listings_ids= [l[0] for l in user_liked_listing]
     if request.method == 'POST':
            if sign == '0':
                 return redirect('signin')
            comment_form = commentForm(request.POST,request.FILES)
            if comment_form.is_valid():
                commenti = comment_form.save(commit=False)
                commenti.post = listing
                commenti.commenter_name = request.user.profile
                commenti.save()
                comment_form = commentForm()
                return HttpResponseRedirect("#")
     elif request.method == 'GET':
        comment_form = commentForm()
        return render(request, 'main/get.html',{'listing':listing, 'sign':sign, 'request':request, 'comm':comment,  'liked_listings_ids':liked_listings_ids, 'comment_form' : comment_form})
     
                                  

def edit_view(request, sign, id):
    if request.method == 'POST':
          listing = post.objects.get(id=id)
          post_form = postForm(request.POST,request.FILES, instance=listing)
          if post_form.is_valid:
               post_form.save()
               return redirect('user_home')
    elif request.method == 'GET':
       listing = post.objects.get(id=id)
       post_form = postForm(instance=listing) 
       #print(listing.image.url) 
       #post_form.fields['image'].widget = forms.FileInput(attrs={'accept': 'image/*', 'value': listing.image.url}) 
       return render(request, 'main/edit.html',{'post_form':post_form, 'sign':sign})
    
def delete_view(request, sign, id):
    listing = post.objects.get(id=id)
    listing.delete()
    return redirect('user_home')
    
def recent_more(request, sign):
     more = post.objects.all()
     return render(request, 'main/recents.html', {'more':more, 'sign':sign})


def liked_post_view(request, id):
    listing = post.objects.get(id=id)
    liked_lisiting, created = likedpost.objects.get_or_create(profile= request.user.profile,post=listing )
    if not created:
         liked_lisiting.delete()
    else:
         liked_lisiting.save()
    return JsonResponse({
         "is_liked_by_user":created,

    })

def search_view(request, sign):
     query = request.GET['query']
     params = post.objects.filter(Q(heading__icontains = query) | 
                                  Q(author__user__username__icontains = query) | 
                                  Q(tag__icontains = query) | 
                                  Q(category__icontains = query)
)
     

     return render(request, 'main/search.html', {"params":params, "sign":sign, "query":query})


def tags_view(request,sign, tag):
     topic = post.objects.filter(Q(tag=tag) | Q(category=tag))
     return render(request, 'main/tag.html', {"topic":topic, "sign":sign, "tag":tag})


def chatbot_view(request, id,sign):
    response_text = None
    user_input_instance = post.objects.get(id=id)
    user_input = user_input_instance.article
    prompt = f"summarize this article within 4 bullet points and less than 80 words, just cover the basics of article.Dont add anything beside summary. {user_input}"
    response = model.generate_content(prompt)
    response_text = response.text
    return render(request, 'main/chatbot.html',{"response": response_text})
    




     


