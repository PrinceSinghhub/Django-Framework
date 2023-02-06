# this file created by me
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello Prince Singh")

def about(request):
    return HttpResponse("<h1>Prince Singh is a Software Engineare</h1>")

def table(request):
    ans = []
    for i in range(1,11):
        ans.append(2*i)
    return HttpResponse(f"<h1> Table of 2: {ans}</h1>")

def website(request):
    s = ''' <h1>Prince Singh URL List</h1><br>
            <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
            <a href="https://www.youtube.com/playlist?list=PLxCzCOWd7aiHcmS4i14bI0VrMbZTUvlTa"> ADA Playlist </a> <br>
            <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)
