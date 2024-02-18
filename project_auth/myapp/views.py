from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Appointment, Slots, AppointmentHistory
from django.contrib import messages

# Create your views here.
def Index(request):
    username = request.user
    print(username)
    return render(request,'index.html',{'username':username})

def SignUp(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass')
        User.objects.create_user(uname,email,pass1)
    return render(request,'signup.html')

def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/appoint/')
    else:
        if request.method == "POST":
            uname = request.POST.get('uname')
            pass1 = request.POST.get('pass')
            user = authenticate(request,username=uname,password=pass1)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/appoint/')
            else:
                return HttpResponseRedirect('/signup/')
        return render(request,'login.html')

def Appointment1(request):
    if request.user.is_authenticated:
        slots = Slots.objects.all().values_list('slot',flat=True)
        aslots = Appointment.objects.all().values_list('slot',flat=True)
        slots =list(slots)
        aslots = list(aslots)
        if request.method == "POST":

            name = request.POST.get("name")
            contact = request.POST.get('cnumber')
            what = request.POST.get('what')
            slot = request.POST.get('slot')
            if len(aslots)<4:
                Appointment.objects.create(name=name,contact=contact,reason=what,user=request.user,slot=slot)
                messages.success(request,"Your Appointment Confirm See You Soon In...")
        data = Appointment.objects.filter(user_id=request.user)
        msg = len(aslots)
        username = request.user

        history = AppointmentHistory.objects.filter(user=request.user.id)
        return render(request,'appointment.html',{'msg':msg,'data':data,'slots':slots,'aslots':aslots,'username':username,'history':history})
    else:
        return HttpResponseRedirect('/login/')
    
def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def Doctor(request):
    data = Appointment.objects.all()
    datac = AppointmentHistory.objects.all().count()
    print(datac)
    history = AppointmentHistory.objects.all()
    username = request.user
    return render(request,'doctor.html',{'data':data,'history':history})

def Notes(request,id):
    da = Appointment.objects.get(pk=id)
    print(da.user_id)
    if request.method == "POST":
        notes = request.POST.get('note')
        name = da.name
        contact = da.contact
        date = da.date
        time = da.time
        reason = da.reason
        slot = da.slot
        user = da.user_id
        AppointmentHistory.objects.create(doct_notes=notes,name=name,contact=contact,date=date,time=time,reason=reason,slot=slot,user=user)
        Appointment.objects.get(pk=id).delete()
        return HttpResponseRedirect('/doctor/')
    return render(request,'notes.html',{'da':da})

def Cancel(request,id):
    da = Appointment.objects.get(pk=id)
    name = da.name
    contact = da.contact
    date = da.date
    time = da.time
    reason = da.reason
    slot = da.slot
    user = da.user_id
    notes = 'Your Appointment Cancel By You'
    AppointmentHistory.objects.create(doct_notes=notes,name=name,contact=contact,date=date,time=time,reason=reason,slot=slot,user=user)
    messages.success(request,'Your Appointmet Has Been Cancel By You...')
    Appointment.objects.get(pk=id).delete()
    return HttpResponseRedirect('/appoint/')


def CancelDoct(request,id):
    da = Appointment.objects.get(pk=id)
    name = da.name
    contact = da.contact
    date = da.date
    time = da.time
    reason = da.reason
    slot = da.slot
    user = da.user_id
    notes = 'Your Appointment Cancel By Doctor'
    AppointmentHistory.objects.create(doct_notes=notes,name=name,contact=contact,date=date,time=time,reason=reason,slot=slot,user=user)
    messages.success(request,'Your Appointmet Has Been Cancel By You...')
    Appointment.objects.get(pk=id).delete()
    return HttpResponseRedirect('/doctor/')



