from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'web/index1.html')

def comming_soon(request):
    return render(request, 'web/comming_soon.html')
