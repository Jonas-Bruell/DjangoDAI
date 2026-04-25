from django.shortcuts import render

# Create your views here.
def bereken_worp(request):
    return render(request, 'BerekenWorp.html')
