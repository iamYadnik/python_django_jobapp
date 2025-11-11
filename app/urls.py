from django.urls import path
# from app.views import hello, job_details
from app import views

urlpatterns = [
    path('', views.job_list, name='job_home'), 
    path('job/<str:slug>', views.job_details, name='job_details'),
    path('hello/', views.hello, name='hello')
    # path('job/<str:id>', views.job_details),

]