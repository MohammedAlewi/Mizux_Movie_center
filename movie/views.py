from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .xml_database import XmlPr
from .models import Movie
from .models import MovieCategory
from django.views.decorators.csrf import csrf_exempt

def index(request):
    xml=XmlPr()
    categories=xml.get_categories()
    print(categories,"here")
    context={"categories":categories}
    return render(request, 'movie_site_1.html', context)


def list_categories(request,category):
    xml=XmlPr()
    category=xml.read_category(category)
    xml=XmlPr()
    context={"category":category}
    return render(request, 'movie_site_4.html', context)

@csrf_exempt
def del_categories(request,category):
    xml=XmlPr()
    xml.delete_category(category)
    xml=XmlPr()
    category=xml.get_categories()
    context={"categories":category}
    return render(request, 'movie_site_1.html', context)


def edit_categories(request,category):
    xml=XmlPr()
    category=xml.read_category(category)
    context={"category":category}
    return render(request,'movie_site_edit_cat.html',context)

def del_movie(request,movie,category):
    xml=XmlPr()
    xml.delete_movie(movie,category)
    xml=XmlPr()
    category=xml.read_category(category)
    context={"category":category}
    return render(request,'movie_site_4.html',context)

def edit_movie(request,movie,category):
    xml=XmlPr()
    movie=xml.read_movie(movie,category)
    categories=xml.get_categories_name()
    context={"category":category,"movie":movie,"categories":categories}
    return render(request,'movie_site_edit_mov.html',context)

@csrf_exempt
def post_edit_categories(request):
    xml=XmlPr()
    category= MovieCategory(
        category_name=request.POST.get("category_title"),
        movie_genere=request.POST.get("category_genre"),
        description=request.POST.get("category_description"))
    xml.edit_category(category)
    xml.saveXml()
    xml=XmlPr()
    categories=xml.get_categories()
    context={"categories":categories}
    return render(request,'movie_site_1.html',context)

@csrf_exempt
def post_edit_movies(request):
    xml=XmlPr()
    category_name=request.POST.get("category")
    movie= Movie(
        movie_title=request.POST.get("movie_title"),
        movie_description=request.POST.get("description"),
        main_star=request.POST.get("main_star"),
        released_date=request.POST.get("release_date"))
    xml.edit_movies(movie,category_name)
    xml.saveXml()
    xml=XmlPr()
    categories=xml.get_categories()
    context={"categories":categories}
    return render(request,'movie_site_1.html',context)

def add_categories(request):
    context={}
    return render(request,'movie_site_3.html',context)


@csrf_exempt
def post_categories(request):
    xml=XmlPr()
    category= MovieCategory(
        category_name=request.POST.get("category_title"),
        movie_genere=request.POST.get("category_genre"),
        description=request.POST.get("category_description"))
    xml.addNewCategory(category)
    xml=XmlPr()
    categories=xml.get_categories()
    context={"categories":categories}
    return render(request,'movie_site_1.html',context)


def add_movies(request):
    xml=XmlPr()
    categories=xml.get_categories_name()
    context={"categories":categories}
    return render(request,'movie_site_2.html',context)

@csrf_exempt
def post_movies(request):
    xml=XmlPr()
    category_name=request.POST.get("category")
    movie= Movie(
        movie_title=request.POST.get("movie_title"),
        movie_description=request.POST.get("description"),
        main_star=request.POST.get("main_star"),
        released_date=request.POST.get("release_date"))
    xml.addNewMovies(movie,category_name)
    xml=XmlPr()
    category=xml.read_category(category_name)
    context={"category":category}
    return render(request,'movie_site_4.html',context)

