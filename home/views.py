from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import django
from ExeDB import *
from mail_function import *

# Create your views here.
def home(request):
    if request.POST:
        message = dict()
        if request.POST['postType'] == 'rc':
            sendRollcall(request)
            message['notify'] = 'rc'
        elif request.POST['postType'] == 'hw':
            sendHW(request)
            message['notify'] = 'hw'
        elif request.POST['postType'] == 'grade':
            try :
                print(request.POST['rcButton'])    
                send_RC_total(request)
                message['notify'] = 'grade_rc'
            except:
                send_HW_total(request)
                message['notify'] = 'grade_hw'
        elif request.POST['postType'] == 'stuManage':
            try:
                print(request.POST['insert'])
                db = ExeDB()
                db.insert(request.POST['stuName'], 0, 0)
                message['notify'] = 'insert'
            except django.utils.datastructures.MultiValueDictKeyError as e:
                db = ExeDB()
                student = db.get()
                for i in range(len(student)):
                    try:
                        print(request.POST[str(i)])
                        print(student[i][0])
                        db.delete(student[i][0])
                    except:
                        pass
                message['notify'] = 'delete'
            except Exception as e:
                print(e)

        return render(request, 'home/main.html', {'message': message})
    else:
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
    roll_call(sendList, account, smtp)
    shutdown(smtp)

def sendHW(request):
    db = ExeDB()
    student = db.get()

    scoreList = list()
    nameList=list()
    if request.POST:
        for i in range(len(student)):
            try:
                print(request.POST[str(i)], student[i][0])
                scoreList.append(request.POST[str(i)])
                nameList.append(student[i][0])
                db.addH(student[i][0],int(request.POST[str(i)]))
            except Exception as e:
                print('off')
    
    testList, testList2 = getTestList(nameList, scoreList)

    account = 'eric23244@gmail.com'
    password = 'jipdqxwqrnrheqsm'
    smtp = prepare(account, password)
    # hw(nameList,scoreList,account,smtp, request.POST['subject'])
    hw(testList, testList2, account, smtp, request.POST['subject'])
    shutdown(smtp)

def send_RC_total(request):
    db=ExeDB()
    student=db.get()

    scoreList = list()
    nameList=list()
    if request.POST:
        for i in range(len(student)):
            scoreList.append(str(student[i][1]))
            nameList.append(student[i][0])

    account = 'eric23244@gmail.com'
    password = 'jipdqxwqrnrheqsm'

    testList , testList2 = getTestList(nameList, scoreList)
    print(testList, testList2)
    smtp = prepare(account, password)
    # roll_call_total(nameList,scoreList,account,smtp)
    roll_call_total(testList, testList2, account, smtp)
    shutdown(smtp)

def send_HW_total(request):
    db=ExeDB()
    student=db.get()

    scoreList = list()
    nameList=list()
    if request.POST:
        for i in range(len(student)):
            scoreList.append(str(student[i][2]))
            nameList.append(student[i][0])


    testList , testList2 = getTestList(nameList, scoreList)
    account = 'eric23244@gmail.com'
    password = 'jipdqxwqrnrheqsm'
    smtp = prepare(account, password)
    # hw_total(nameList,scoreList,account,smtp)
    hw_total(testList, testList2, account, smtp)
    
    shutdown(smtp)

def getTestList(nameList, scoreList):
    testList = list()
    testList2 = list()
    for i in range(len(nameList)):
        if nameList[i] == 'A1065502' or nameList[i] == 'A1065503':
            testList.append(nameList[i])
            testList2.append(scoreList[i])
    
    return (testList, testList2)

def gradeView(request):
    db = ExeDB()
    student = db.get()
    returnList = list()
    i=0

    for ele in student:
        temp = {'name': ele[0], 'rc': ele[1], 'hw': ele[2], 'number': i}
        returnList.append(temp)
        i+=1

    return render(request, 'home/gradeView.html', {'student': returnList})

def studentManage(request):
    db = ExeDB()
    student = db.get()
    returnList = list()
    i=0

    for ele in student:
        temp = {'name': ele[0], 'rc': ele[1], 'hw': ele[2], 'number': i}
        returnList.append(temp)
        i+=1

    return render(request, 'home/studentManage.html', {'student': returnList})


def homework(request):
    db = ExeDB()
    student = db.get()
    returnList = list()
    i = 0
    for ele in student:
        temp = {'name': ele[0], 'number': i}
        returnList.append(temp)
        i+=1
    return render(request, 'home/homework.html', {'student': returnList})


def test(request):
    messages.info(request, "Test")
    return HttpResponse