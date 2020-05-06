# I have created this file-Vipin
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
 #   return HttpResponse("hello harry bhai")
#def about(request):
 #   return HttpResponse("hello harry")
#def navigation(request):
 #   s = '''<h2>Navigation Bar<br></h2>
  #          <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br>
   #         <a href="https://www.facebook.com/">Facebook</a><br>
    #        <a href="https://www.flipkart.com/">Flipkart</a><br>
     #       <a href="https://www.hindustantimes.com">News</a><br>
      #      <a href="https://www.google.com/">Google</a>'''
    #return HttpResponse(s)﻿
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fulcaps = request.POST.get('fulcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(fulcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Lines Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
    if(removepunc!="on" and extraspaceremover!="on" and newlineremover!="on" and fulcaps!="on"):
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)