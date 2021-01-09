from django.shortcuts import render, redirect
from . forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    form_1 = UserCreationForm(request.POST)
    context = {
        'title': 'التسجيل',
        'form': form_1,
    }
    return render(request,'user/register.html',context)
"""
if request.method == 'POST':
        form_1 = UserCreationForm(request.POST)
        if form_1.is_valid():
            form_1.save()
            username = form_1.cleaned_data['username']
            messages.success(request, f'تهانينا {username} لقد تم تسجيل الدخول بنجاح.')
            return redirect()
"""