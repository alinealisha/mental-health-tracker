from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306207921',
        'name': 'Alisha Aline Athiyyah',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
# Create your views here.
