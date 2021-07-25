# Made by me - Manan Patel
import django.shortcuts
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Getting the text
    textx = request.POST.get('text', 'default')

    #Getting value of radio buttons
    removepuncx = request.POST.get('removepunc','off')
    uppercasex = request.POST.get('uppercase','off')
    extspacex = request.POST.get('extspace','off')
    newlinex = request.POST.get('newline','off')

    #Analyzing text
    job = ""
    analyzed = ""
    numchar = 0
    if removepuncx == 'on':
        punctuations = '''!()-[]{};:'"\/,<>.?@#$%^&*~`'''
        analyzed = ""
        for char in textx:
            if char not in punctuations:
                analyzed += char
        job += '| Removed Puntuations '
        textx = analyzed

    if uppercasex == 'on':
        analyzed = ""
        for char in textx:
            analyzed += char.upper()
        job += "| UPPERCASE "
        textx = analyzed

    if extspacex == 'on':
        analyzed = ""
        for index, char in enumerate(textx):
            if not (textx[index] == " " and textx[index+1] == " "):
                analyzed += char
        job += "| Removed Extra Space "
        textx = analyzed

    if newlinex == 'on':
        analyzed = ""
        for char in textx:
            if char != '\n' and char != '\r':
                analyzed += char
        job += '| Removed New line(s) '
        params = {'job': 'Removed New line(s)', 'analyzed_text': analyzed}
        textx = analyzed

    if(newlinex != 'on' and extspacex != 'on' and uppercasex != 'on' and removepuncx != 'on'):
        return HttpResponse("Please select valid option!")

    count = 0
    for char in textx:
        if not (char == " " and char == '\n'):
            count += 1
    numchar = count

    params = {'job':job , 'analyzed_text':analyzed, 'numchar':numchar}
    return render(request, 'analyze.html', params)