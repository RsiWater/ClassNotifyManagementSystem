from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/main.html')

def rollcall(request):
    student = ['123','456','789','123','456']
    return render(request, 'home/rollcall.html', {'student': student})