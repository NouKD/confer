from django.shortcuts import render

# Create your views here.

def schedule(request):
    
    data = {
        
    }
    
    return render(request, 'schedule.html', data)


def speakers(request):
    
    data = {
        
    }
    
    return render(request, 'speakers.html', data)

def tickets(request):
    
    data = {
        
    }
    
    return render(request, 'tickets.html', data)
