from django.shortcuts import render


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        
        return render(request, 'register.html')
