import xml.etree.ElementTree as et
import os
from .models import *

class XmlPr:
    def __init__(self,filename="star_movies.xml"):
        self.filename=filename
        self.root=None
        self.parent=None
        self.found_flag=False
        self.getFile()
    
    def getFile(self):
        try:
            self.xmlObj = et.parse(self.filename)
            self.root=self.xmlObj.getroot()
            return self.xmlObj
        except:
            movie_file=open(self.filename,"w")
            movie_file.write('<movie_data></movie_data>')
            movie_file.close()
            self.xmlObj = et.parse(self.filename)
            self.root=self.xmlObj.getroot()

    def addNewCategory(self,movie_Category):
        self.parent=self.root
        new_category = et.SubElement(self.parent,movie_Category.category_name)

        cat_name = et.SubElement(new_category,"category_name")
        cat_name.text=movie_Category.category_name

        desc_name = et.SubElement(new_category,"category_description")
        desc_name.text=movie_Category.description

        genere_name = et.SubElement(new_category,"category_genere")
        genere_name.text=movie_Category.genere

        et.SubElement(new_category,"movies")

        self.saveXml()
    
    def addNewMovies(self,movie_data,movie_category):
        category=self.root.find(movie_category).find("movies")
        movie=et.SubElement(category,"Movie")

        title=et.SubElement(movie,"movie_title")
        title.text=movie_data.movie_title
        
        desc=et.SubElement(movie,"movie_description")
        desc.text=movie_data.movie_description

        star=et.SubElement(movie,"main_star")
        star.text=movie_data.main_star

        rel_date=et.SubElement(movie,"released_date")
        rel_date.text=movie_data.released_date

        self.saveXml()

    def delete_category(self,category):
        for cat in self.root:
            if cat.tag==category:
                self.root=self.root.remove(cat)
                break
        self.saveXml()

    def delete_movie(self,movie,category_name):
        for mov in self.root.find(category_name).find("movies"):
            if mov.find("movie_title").text==movie:
                self.root.find(category_name).find("movies").remove(mov)
                break
        self.saveXml()

    def edit_movies(self,movie,category_name):
        for mov in self.root.find(category_name).find("movies"):
            if mov.find("movie_title").text==movie.movie_title:
                mov.find("movie_description").text=movie.movie_description
                mov.find("main_star").text=movie.main_star
                mov.find("released_date").text=movie.released_date
                break
        self.saveXml()

    def edit_category(self,category):
        cat=self.root.find(category.category_name)
        cat.find("category_description").text=category.description
        cat.find("category_genere").text=category.genere
        self.saveXml()

    def get_categories(self):
        categories=[]
        for i in self.root:
            categories.append(self.read_category(i.tag))
        return categories

    def get_categories_name(self):
        categories=[]
        for i in self.root:
            categories.append(i.tag)
        return categories

    def read_category(self,category_name):
        cat=self.root.find(category_name)
        movies=[]
        for movie in cat.find("movies"):
            m=Movie(movie.find("movie_title").text,movie.find("movie_description").text,movie.find("main_star").text,
                movie.find("released_date").text)
            movies.append(m)
        category=MovieCategory(cat.tag,cat.find("category_description").text,cat.find("category_genere").text,movies)
        return category

    def read_movie(self,movie_name,category):
        for movie in self.root.find(category).find("movies"):
            if movie.find("movie_title").text==movie_name:
                m=Movie(movie.find("movie_title").text,movie.find("movie_description").text,movie.find("main_star").text,
                    movie.find("released_date").text)
                return m

    def saveXml(self):  
        self.xmlObj.write(self.filename)


# x=XmlPr()
# c=x.get_categories()
# print(c)
# print(x.read_movie("malloc","porn").movie_description)
# c=MovieCategory("porn","amature","starter")
# x.addNewCategory(c)
# x.edit_category(c)
# m=Movie("malloc","beast movie","you are","june 28,2020")
# x.edit_movies(m,"porn")
# x.addNewMovies(m,"porn")
# x.delete_category("porn")
# x.delete_movie(m,"porn")
# x.saveXml()
