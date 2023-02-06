# this file created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("<h1>Home Page</h1>")
    # using templates
    # param = {'Name':'CODEX CODER','Place':'Mars'}
    return render(request,'index.html')

def analyze(request):
    # get - use for mini info passs
    # post - use for use data pass
    # getthe text from user
    excessText = request.POST.get('text','default')
    remoePunch = request.POST.get('RemovePunch','default')
    uppercase =  request.POST.get('upperCase','default')
    lowercase =  request.POST.get('lowerCase','default')
    CountChar =  request.POST.get('countChar','default')
    print(excessText)
    print(remoePunch)

    multiple_check = [remoePunch,uppercase,lowercase,CountChar]
    # return HttpResponse("remove punch")
    if remoePunch!='on' and uppercase!='on' and lowercase!='on' and CountChar!='on':

        param = {'Variable': 'Ooops Please Select At Least 1 Command to use This Website'}
        return render(request, 'error.html', param)


    # todo for single operation
    if remoePunch == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzedText = ""
        for i in excessText:
            if i not in punctuations:
                analyzedText += i

        String = "After Removining All the Punchunation"
        param = {'Variable': 'Your Text is Analysed', 'answer': analyzedText, 'msg': String}
        return render(request, 'analyze.html', param)

    elif uppercase == 'on':
        ans = ""
        for i in excessText:
            if i.islower() or i.isupper():
                ans += i.upper()
            else:
                ans += " "
        String = "After Convert In UpperCase"
        param = {'Variable': 'Your Text is Analysed', 'answer': ans, 'msg': String}
        return render(request, 'analyze.html', param)

    elif lowercase == "on":
        ans = ""
        for i in excessText:
            if i == " ":
                ans += " "
            ans += i.lower()
        String = "After Convert In LowerCase"
        param = {'Variable': 'Your Text is Analysed', 'answer': ans, 'msg': String}
        return render(request, 'analyze.html', param)


    elif CountChar == "on":
        count = 0
        char = ""
        for i in excessText:
            if i.isalpha():
                count += 1
                char += i
        String = "After Count Char in Given String"
        param = {'Variable': 'Your Text is Analysed', 'answer': count, 'msg': String, 'Char': char}
        return render(request, 'analyze.html', param)




def newline(request):
    return HttpResponse("new_line")

def spaceremove(request):
    return HttpResponse("space remover <a href ='/'>back</a> ")
