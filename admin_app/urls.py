from django.urls import path
from .import views
urlpatterns=[
   path('',views.login,name="login"),
   path('register_student',views.register_student,name="register_student"),
   path('dashboard',views.dashboard,name="dashboard"),
   path('student_listing',views.student_listing,name="student_listing")
]
