from django.shortcuts import render
from django.http import HttpResponse, Http404
import os, django
from . import BestSeller
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_recommend_service.settings")# project_name project name
django.setup()
# Create your views here.


# def home(request):
#     return render(request, 'home.html')

def show_bestseller(request):
    BS = BestSeller.bestseller()
    bs_titles = [BS[0][i] for i in range(10)]
    bs_authors = [BS[1][i] for i in range(10)]
    bs_urls = [BS[2][i] for i in range(10)]
    return render(request, 'home.html',
                  {'bs_title1': bs_titles[0], 'bs_title2': bs_titles[1], 'bs_title3': bs_titles[2], 'bs_title4': bs_titles[3], 'bs_title5': bs_titles[4],
                   'bs_title6': bs_titles[5], 'bs_title7': bs_titles[6], 'bs_title8': bs_titles[7], 'bs_title9': bs_titles[8], 'bs_title10': bs_titles[9],
                   'bs_author1': bs_authors[0], 'bs_author2': bs_authors[1], 'bs_author3': bs_authors[2], 'bs_author4': bs_authors[3], 'bs_author5': bs_authors[4],
                   'bs_author6': bs_authors[5], 'bs_author7': bs_authors[6], 'bs_author8': bs_authors[7], 'bs_author9': bs_authors[8], 'bs_author10': bs_authors[9],
                   'bs_url1': bs_urls[0], 'bs_url2': bs_urls[1], 'bs_url3': bs_urls[2], 'bs_url4': bs_urls[3], 'bs_url5': bs_urls[4],
                   'bs_url6': bs_urls[5], 'bs_url7': bs_urls[6], 'bs_url8': bs_urls[7], 'bs_url9': bs_urls[8], 'bs_url10': bs_urls[9]})




