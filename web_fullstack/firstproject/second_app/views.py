from django.shortcuts import render


def help(request):
    my_dict = {
        'help_needed': 10
    }
    return render(request, 'second_app/help.html', context=my_dict)
