from django.shortcuts import render

# Create your views here.


def blogs_list_view(request):
    return render(request, 'blogs/blogs-list.html')