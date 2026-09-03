from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'آرمین دهقان'
    }
    return render(request, 'resume/index.html', context)