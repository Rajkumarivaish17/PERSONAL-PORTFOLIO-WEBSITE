from django.shortcuts import redirect, render


# Create your views here.

def home(request):
    return render(request,'index.html')

def about_attempt(request):
    return render(request,'about.html')   

def skills_attempt(request):
    return render(request,'skills.html') 

def home_attempt(request):
    return redirect('/') 

def about_attempt_again(request):
    return redirect('/about')

def work_attempt(request):
    return render(request,'work.html')  

def work_attempt_again(request):
    return redirect('/work') 

def home_attempt_again(request):
    return redirect('/')  

def contact_attempt(request):
    return render(request,'contact.html')     

def contact_attempt_again(request):
    return redirect('/contact')    