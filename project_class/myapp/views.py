from django.shortcuts import render
from django.views import View
from .models import Table
# Create your views here.

class IndexClass(View):
    def get(self,request):
        print('Now Get method only get running...')
        get = 'Now get method get Running...'
        return render(request,'index.html',{'data':get})
    
    def post(self,request):
        print('Now post method get running...')
        post = 'Now Post method get Running...'
        return render(request,'index.html',{'data':post})
    
    
class DataFetch(View):
    def get(self,request):
        data = Table.objects.all()
        return render(request,'data.html',{'data':data})
