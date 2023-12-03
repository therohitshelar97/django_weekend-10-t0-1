from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'index.html')


def Home(request):
    return render(request, 'home.html')
