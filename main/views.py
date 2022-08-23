from django.shortcuts import render
from .forms import UserForm
from .models import users
def index(request):
    error = ''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Ошибка в заполнении формы'
    form = UserForm
    data = {
        'form': form,
        'error':error
    }
    return render(request, 'main/index.html', data)
