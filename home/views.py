from django.shortcuts import render, HttpResponse
from django.contrib import messages
from ExeDB import *
from mail_function import *

# Create your views here.
def home(request):
    return render(request, 'home/main.html')

def rollcall(request):
    db = ExeDB()
    student = db.get()
    returnList = list()
    i = 0
    for ele in student:
        temp = {'name': ele[0], 'number': i}
        returnList.append(temp)
        i+=1
    return render(request, 'home/rollcall.html', {'student': returnList})

def sendRollcall(request):
    db = ExeDB()
    student = db.get()

    sendList = list()
    if request.POST:
        for i in range(len(student)):
            try:
                print(request.POST[str(i)], student[i][0])
                sendList.append(student[i][0])
                db.addRC(student[i][0])
            except:
                print('off')
    
    account = 'eric23244@gmail.com'
    password = 'jipdqxwqrnrheqsm'
    smtp = prepare(account, password)
    # roll_call(sendList, account, smtp)
    shutdown(smtp)

def test(request):
    messages.info(request, "Test")
    return HttpResponse