from django.shortcuts import render


def main(request):
    return render(request, 'posts/main.html')


def show(request):
    return render(request, 'posts/show.html')