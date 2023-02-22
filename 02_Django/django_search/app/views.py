from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    name = 'MaJHI'
    context = {
        'name': 'MaJHi',
        'age': 71,
        'nationality': 'Bangladeshi',
    }
    return render(request, 'index.html', {'data': context, 'name': name})
