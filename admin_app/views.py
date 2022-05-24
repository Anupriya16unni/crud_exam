import email
from django.shortcuts import render
from django.shortcuts import redirect,render
from admin_app.models import AddStudent, AdminLogin

# Create your views here.

def login (request):
    error=''
    
    if request.method=='POST':
        admin_name=request.POST['uname']
        admin_pass=request.POST['pass']
        try:
            admin_data=AdminLogin.objects.get(username=admin_name,password=admin_pass)
            request.session['admin_id']=admin_data.id
            return redirect('dashboard')
        except:
            error="invalid username or password"

    return render (request,'adminapp/login.html',{'error': error})

def register_student (request):
    if request.method=="POST":
        s_name=  request.POST["name"]
        s_contact=  request.POST["contact"]
        s_email= request.POST["email"]
        s_username=  request.POST["username"]
        s_password=  request.POST["password"]

        add_student=AddStudent(name=s_name,email=s_email,contact=s_contact,username=s_username,password=s_password)
        add_student.save()
    return render (request,'adminapp/register_student.html')

def dashboard (request):
    return render (request,'adminapp/dashboard.html')

def student_listing (request):
    return render (request,'adminapp/student_listing.html')