from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'inder_site/index.html')

def reports(request):
    return render(request, 'inder_site/reports.html')