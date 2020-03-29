from django.shortcuts import render
from .forms import UserProfileForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:home'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserProfileForm()
        profile_form = UserProfileInfoForm()

    dict = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    }
    return render(request, 'user_profile/register.html', dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('first_app:home'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone try to login and failed!')
            print('Username : {} and password {}'.format(username, password))
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request, 'user_profile/login.html')
