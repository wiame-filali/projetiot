from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#def home(request):
 #return HttpResponse('bonjour à tous')
# Create your views here.
from django.shortcuts import render
# Create your views here.
from .models import Dht
def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'Tables.html', s)
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def charts(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request,'charts.html',s)

