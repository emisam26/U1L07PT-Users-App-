from django.shortcuts import render

# Create your views here.
def register(request):
    context = {
        'active_link': 'users'
    }
    return render(request,'users/register.html', context)