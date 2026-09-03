from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {
        'title':'blog'
    }
    return render(request,'blog/blog.html',context)

def post(request):
    context = {
        'title':'post'
    }
    return render(request,'blog/post.html',context)
