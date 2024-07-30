from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse


# def header(request):
#     return render(request, 'header2.html')
def homePage(request):
    # return render(request, 'main/index.html')
    return render(request, 'index.html')



def news(request):
    return render(request, 'news.html')



def management(request):
    return render(request, 'management.html')


def facts(request):
    return render(request, 'facts.html')



def contacts(request):
    return render(request, 'contacts.html')

def history(request):
    return render(request, 'history.html')
def historyPeople(request):
    return render(request, 'hpeople.html')

def historyPhoto(request):
    return render(request, 'hphoto.html')

def newsNotFound(request, text):
    return HttpResponse(f'<meta http-equiv="refresh" content="0;URL=http://127.0.0.1:8000/news"/>')
def factsNotFound(request, text):
    return HttpResponse(f'<meta http-equiv="refresh" content="0;URL=http://127.0.0.1:8000/facts"/>')
def managementNotFound(request, text):
    return HttpResponse(f'<meta http-equiv="refresh" content="0;URL=http://127.0.0.1:8000/management"/>')
def contactsNotFound(request, text):
    return HttpResponse(f'<meta http-equiv="refresh" content="0;URL=http://127.0.0.1:8000/contacts"/>')
def homeNotFound(request, text):
    return HttpResponse(f'<meta http-equiv="refresh" content="0;URL=http://127.0.0.1:8000"/>')

def historyNotFound(request, text):
    if text=='people':
        return HttpResponse(f'<meta http-equiv="refresh" content="0;URL=http://127.0.0.1:8000/history/people"/>')
    if text=='photos':
        return HttpResponse(f'<meta http-equiv="refresh" content="0;URL=http://127.0.0.1:8000/history/photos"/>')
    else:
        return HttpResponse(f'<meta http-equiv="refresh" content="0;URL=http://127.0.0.1:8000/history"/>')