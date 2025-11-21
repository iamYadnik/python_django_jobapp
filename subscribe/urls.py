
from django.urls import path, include
from . import views


# def hello(request):
#     return HttpResponse('Hello World')


urlpatterns = [path('subscribe/', views.subscribe, name='subscribe'),
               path('thankyou/', views.thankyou, name='thankyou')
     
]