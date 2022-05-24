from django.urls import path
from .import views
urlpatterns=[
   path('',views.student_login,name="student_login"),
   path('update_profile',views.update_profile,name="update_profile")
]