# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Subcategory
from .forms import PostForm
from .models import Page


def home(request):
    pages = Page.objects.all()  
    posts = Post.objects.all().order_by('-created_at')         
    return render(request, 'blog/home.html', {'posts': posts,'page': pages})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')

def blog_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'categories': categories
    })
def posts_by_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    return render(request, 'blog/posts_by_category.html', {'posts': posts})


