from django.shortcuts import render


def index(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)


def main(request):
    context_dict = {}
    return render(request, 'main.html', context_dict)
