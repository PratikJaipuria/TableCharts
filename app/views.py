from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request,'template.html')

def charts(request):
    return render(request,'charts.html')
