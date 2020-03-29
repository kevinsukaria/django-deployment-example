from django.shortcuts import render


# Create your views here.
def fork(request):
    return render(request, 'fourth_app/fork.html')


def path1(request):
    return render(request, 'fourth_app/path1.html')


def path2(request):
    return render(request, 'fourth_app/path2.html')
