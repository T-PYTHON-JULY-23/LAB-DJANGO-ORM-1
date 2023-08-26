from django.shortcuts import render ,redirect
from .models import Post

def home(request):
    return render(request, 'pages/home.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'pages/posts.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        publish_date = request.POST['publish_date']
        post = Post(title=title, content=content, category=category, publish_date=publish_date)
        post.save()
        return redirect('posts')
    return render(request, 'pages/add_post.html')

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts')