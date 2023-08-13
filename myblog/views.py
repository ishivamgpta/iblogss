from django.shortcuts import render
from django.http import HttpResponse
from myblog.models import Post,Category

# Create your views here.

def home(request):
    #LOAD ALL THE  POST FROM DB
    posts=Post.objects.all()
    cats=Category.objects.all()
    #print(posts)
    data={
        'posts':posts,
        'cats':cats
   }
    return render(request,'home.html',data)


def post(request,url):
    post=Post.objects.get(url=url)
    cats=Category.objects.all()
    #print(post)

    return render(request,'posts.html',{'post':post,'cats':cats})


def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)


    return render(request,'category.html',{'cat':cat,'posts':posts})

def about(request):
    return render(request,'about.html')


