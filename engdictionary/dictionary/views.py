from re import search
from django.shortcuts import render
from PyDictionary import PyDictionary as pyd
# Create your views here.
def index(request):
    return render(request,'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = pyd()
    meaning = dictionary.meaning(search)
    synonmys = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    context = {
        'meaning': meaning,
        'synonmys' : synonmys,
        'antonyms' : antonyms
    }
    return render(request,'word.html',context)