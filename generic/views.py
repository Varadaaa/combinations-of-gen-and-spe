from django.shortcuts import render

# Create your views here.


def gen(request):
    return render(request, 'gen.html')




def gen2(request):
    return render(request, 'gen2.html')

