from django.shortcuts import render, redirect
from .forms import studentForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = studentForm()
    return render(request, 'studentapp/registrationform.html', {'form': form})