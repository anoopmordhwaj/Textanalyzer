# i have created this file -Anoop
from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
    return render(request,'index.html')

def about(request):
 
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    charcount=request.POST.get('charcount','off')
    removeapos=request.POST.get('removeapos','off')
    lineremover=request.POST.get('lineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    uppercase=request.POST.get('uppercase','off')


    
    if(removepunc=="on"):
        analyzed=""
        symbols='''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        for char in djtext:
            if char not in symbols:
                analyzed+=char
        params = {'purpose':'Removing Punctuations:  ','analyzed_text':analyzed}
        djtext=analyzed              
        # return render(request,'analyzer.html',params) 


    if(charcount=="on"):
        analyzed=0
        for char in djtext:
            analyzed+=1
        

        params = {'purpose':'characters in text:',"analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,'analyzer.html',params)
    
    if(removeapos=="on"):
        sp=djtext.split()
        analyzed=""
        for word in sp:
           l=0
           l=len(word)
           if not(word.find("'")==l-2):
                word=word.replace("'","") 
                analyzed=analyzed+word+" " 
           else:    
               analyzed=analyzed+word+" "

        params = {'purpose':'Removed Apostrophes :',"analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,'analyzer.html',params)
    
    if(spaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char
        params = {'purpose':'Removed Extra space :',"analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,'analyzer.html',params)
    

    if(lineremover=='on'):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose':'Removed Extra :',"analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,'analyzer.html',params)


    if uppercase=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(removepunc != "on" and lineremover!="on" and spaceremover!="on" and uppercase!="on"and charcount!="on" and removeapos!="on" ):
            return HttpResponse("please select any operation and try again")

    return render(request,'analyzer.html',params)