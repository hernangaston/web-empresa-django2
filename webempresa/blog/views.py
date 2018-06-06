from django.shortcuts import render, get_object_or_404

from .models import Category, Post

# Create your views here.
def blog(request):
	posts = Post.objects.all()
	title = "Blog"
	d = dict(title=title, posts=posts)
	return render(request, "blog/blog.html", d)


def category(request, category_id):
	category = get_object_or_404(Category, id=category_id)
	title = "Categoria"
	d = dict(title=title, category=category)
	return render(request, "blog/category.html", d)