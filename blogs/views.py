from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Blog,Category



def post_by_category(request,category_id):
    #Fetch the posts that belong to the category with the id category_id
    posts=Blog.objects.filter(status="Published",category=category_id)
    # Use try except when you want to do some custom action when the category doesnt exist
    # try:
    #  category=Category.objects.get(pk=category_id)
    # except:
    #     #redirect user to home page
    #     return redirect('home')
    # use get_object_or_404 when you want to show 404 error page if the category doesnt exist
    category=get_object_or_404(Category, pk=category_id)
    context={
        'posts': posts,
        'category': category,
    }
    return render(request,'post_by_category.html',context)