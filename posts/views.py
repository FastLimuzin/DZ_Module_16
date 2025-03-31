from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from users.models import User
from django.contrib import messages

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        author = User.objects.first()  # Берём первого пользователя
        if title and content:
            post = Post.objects.create(title=title, content=content, image=image, author=author)
            messages.success(request, 'Пост успешно создан!')
            return redirect('posts:post_list')
        else:
            messages.error(request, 'Заполните все поля!')
    return render(request, 'posts/post_create.html')

def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
        messages.success(request, 'Пост обновлён!')
        return redirect('posts:post_list')
    return render(request, 'posts/post_update.html', {'post': post})

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Пост удалён!')
        return redirect('posts:post_list')
    return render(request, 'posts/post_delete.html', {'post': post})