from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UserRegisterform

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('Blog-Home')

    else:
        form = UserRegisterform()
    return render(request, 'users/register.html', {'form':form})    