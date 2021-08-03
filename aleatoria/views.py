from django.shortcuts import render , redirect
from django.utils.crypto import get_random_string

def index(request):
    request.session['contador'] = 1
    contexto = {
        'palabra' :   get_random_string(length=14)
    } 
    return render(request,'aleatoria/index.html', contexto)

def palabra(request):
    if 'contador' in request.session:
        request.session['contador'] = request.session['contador'] +1
    else:
        request.session['contador'] = 1
    contexto = {
        'palabra' :   get_random_string(length=14)
    }     
    return render(request, 'aleatoria/index.html', contexto)

def reset(request):
    if request.session['contador']:
        del request.session['contador']
    return redirect('/index.html')
