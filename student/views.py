from django.shortcuts import render

from admin_app.models import AddStudent
from django.shortcuts import redirect,render

# Create your views here.

def student_login (request):
    error_msg=''
    if request.method == 'POST':
        user_name = request.POST['user_std']
        std_password = request.POST['pass_std']
        seller_data = AddStudent.objects.filter(
            username=user_name, password=std_password).exists()
        if seller_data:
            seller=AddStudent.objects.get(username=user_name,password=std_password)
            request.session['student_id']=seller.id
            return redirect('update_profile')
        else:
            error_msg = "Invalid user name and password"
    return render (request,'student_app/student_login.html',{'error':error_msg})

def update_profile (request):
    current_user=request.session['student_id']
    profile=AddStudent.objects.get(id=current_user)
    return render (request,'student_app/update_profile.html',{'prof':profile})

