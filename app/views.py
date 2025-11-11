from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost


job_title = [
    'first job',
    'second job',
    'third job',
]

job_description = [
    'frist job_desc',
    'second job desc',
    'thid job desc',
]

# Create your views here.
class tempclass():
    x = 5

def hello(request):
    # template = loader.get_template('app/hello.html')
    temp = tempclass()
    is_authenticated = False
    lt = ['alpha', 'beta']
    # age = 5
    context = {'name':'Django', 'first_list':lt, 'temp_object':temp, 'age': 30, 'is_authenticated': is_authenticated}
    # return HttpResponse(template.render(context, request))
    return render(request, 'app/hello.html', context)



def job_list(request):
    # text = ''
    # for a in job_title:
    #     text += f'<h3>{a} </h3>' 
    # return HttpResponse(text)
    # list_of_jobs = '<ul>'
    jobs = JobPost.objects.all()
    # lt = []
    
    # for j in job_title:
    #     dt = {}
    #     job_id = job_title.index(j)
    #     detail_url = reverse(('job_details'), args=(job_id,))
    #     dt['job_title'] = j
    #     dt['detail_url'] = detail_url
    #     lt.append(dt)
        
        # list_of_jobs += f"<li><a href='{detail_url}'> {j}</a></li>"
    # list_of_jobs += '</ul>'
    context = {'jobs':jobs}
    return render(request, 'app/job_list.html', context)  


def job_details(request, slug):
    try:
        if id == 0:
            return redirect(reverse('job_home'))
        # return HttpResponse(f'<h1>job details {id}</h1>')
        # return_html = f'<h1> {job_title[id]} </h1> <h3> {job_description[id]}</h3>'
        job = JobPost.objects.get(slug=slug)
        context = {'job': job}
        return render(request, 'app/job_detail.html', context)


    except:
        return HttpResponseNotFound('Not found')
    
    return HttpResponse(return_html)