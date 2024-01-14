from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import Table
from django.contrib import messages
from .forms import TableForm
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
    

class DataDelete(View):
    def get(self,request,id):
        Table.objects.get(pk=id).delete()
        messages.success(request,"Data Deleted Succesfully........")
        return HttpResponseRedirect('/data/')
    
    def post(self,request,id):
        Table.objects.get(pk=id).delete()
        messages.success(request,"Data Deleted Succesfully........")
        return HttpResponseRedirect('/data/')
    

class DataUpdate(View):
    def get(self,request,id):
        data = Table.objects.get(pk=id)
        fm = TableForm(instance=data)
        print(fm)
        return render(request,'update.html',{'data':fm})
    
    def post(self,request,id):
        data = Table.objects.get(pk=int(id))
        print(request.method)
        fm = TableForm(request.POST,instance=data)
        print(fm)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Data Updated Successfully.....")
        return HttpResponseRedirect('/data/')