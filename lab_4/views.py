from django.shortcuts import render
from lab_2.views import landing_page_content
from django.http import HttpResponseRedirect
from .forms import Message_Form
from .models import Message

# Create your views here.
response = {'author': "Anisha Inas Izdihar"} #TODO Implement yourname
about_me = ['hard-work', 'dedication', 'patience', 'loyalty', 'fair-play','wisdom']
def index(request):
    response['content'] = landing_page_content
    html = 'lab_4/lab_4.html'
    #TODO Implement, isilah dengan 6 kata yang mendeskripsikan anda
    response['about_me'] = about_me
    response['message_form'] = Message_Form
    return render(request, html, response)

def message_post(request):
    form = Message_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['name'] = request.POST['name'] if request.POST['name'] != "" else "Anonymous"
        response['email'] = request.POST['email'] if request.POST['email'] != "" else "Anonymous"
        response['message'] = request.POST['message']
        message = Message(name=response['name'], email=response['email'],
                          message=response['message'])
        message.save()
        html ='lab_4/form_result.html'
        return render(request, html, response)
    else:
        #alert("What are you trying to say?")  
        return HttpResponseRedirect('/lab-4/')

def message_table(request):
    message = Message.objects.all()
    response['message'] = message
    html = 'lab_4/table.html'
    return render(request, html , response)
