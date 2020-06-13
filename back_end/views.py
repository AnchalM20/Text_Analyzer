from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    pram={'name':'popo','place':'Dahisar'}
    return render(request,'Baby.html',pram)

def index1(request):
    return render(request,'index.html')    
            
def analyze(request):
    djtext=request.POST.get('text','default')
    removpunc=request.POST.get('removpunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline=request.POST.get('newline','off')
    spaceremove=request.POST.get('spaceremove','off')
    charcount=request.POST.get('charcount','off')
    if removpunc=="on":
        punctuation=''':;'".,!~?_-<>/@#`&%$^*[](){}'''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char
        djtext = analyzed
        # params={'purpose':'Removed punctuation','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        djtext = analyzed
        # params={'purpose':'Changed to uppercase','analyzed_text':analyzed}
        # return render(request,'analyze.html',params) 
    if(newline=="on"):
        analyzed=""
        for char in djtext:
            if (char!="\n" and char!="\r"):
                analyzed=analyzed+char
        djtext = analyzed
        # params={'purpose':'Newline is removed','analyzed_text':analyzed}
        # return render(request,'analyze.html',params) 
    if(spaceremove=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                 analyzed=analyzed+char
        djtext = analyzed
        # params={'purpose':'Extraspaces are removed','analyzed_text':analyzed}
        # return render(request,'analyze.html',params) 
    if(charcount=="on"):
        count=0
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " or djtext[index+1]=="  "):
                 count=count+1
        djtext = analyzed
        # params={'purpose':'character counter','analyzed_text':count}
        # return render(request,'analyze.html',params)
    params={'analyzed_text':djtext} 
    return render(request,'analyze.html',params)

    # else:
    #     return HttpResponse("Error")  
# def Ex(request):
#     return HttpResponse(
#      '''<style>
#         h1,h2{
#             color:gray;
#             underline:none;
#         } body{background-color:cyan}
#         </style>
#     <center><h1>List of Website...</h1></center><br><h2><a href="https://www.coursera.org/">Coursera--Online learning web</a></h2>
#     <br><h2><a href="https://www.youtube.com/">Youtube--Online videos</a></h2>''' )

# def removpunc(request):
#     #get the text
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("remov punctuation")

# def capfirst(request):
#     return HttpResponse('''capitalize first<br> <a style="color:yellow;textstyle:none;"
# href="http://127.0.0.1:8000/"> Go back</a>''')

# def about(request):
#     return HttpResponse('<a href="https://community.simpleisbetterthancomplex.com/t/how-to-display-txt-file-in-django-with-html-and-django-pagination/459/2"> simple better complex</a>')

# def plain_text_view(request):
#     file = open('ujalawa.txt', 'r')
#     content = file.read()
#     file.close()
#     return HttpResponse(content, content_type='text/plain')

# def htmlfile(request):
#     file = open('Baby.html', 'r')
#     content = file.read()
#     file.close()
#     return HttpResponse(content, content_type='html')
 
