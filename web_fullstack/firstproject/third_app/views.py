from django.shortcuts import render
from third_app.models import Users
from . import forms
from first_app import views


# Create your views here.

def users(request):
    obj = Users.objects.all()
    form = forms.UserForm()

    dict = {
        'users': obj,
        'form': form
    }

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return views.homepage(request)
            # fn = form.cleaned_data['first_name']
            # ln = form.cleaned_data['last_name']
            # em = form.cleaned_data['email']
            # t = Users.objects.get_or_create(first_name=fn, last_name=ln, email=em)[0]
            # t.save()

    return render(request, 'third_app/users.html', context=dict)
