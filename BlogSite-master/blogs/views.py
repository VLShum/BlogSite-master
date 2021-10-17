from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogModelForm
from django.contrib.admin.views.decorators import staff_member_required

def homepage(request):
        qs = Blog.objects.all()[:5]
        template = 'homepage.html'
        context = {'object_list':qs}
        return render(request, template, context)

def blog_post_list_view(request):
    qs = Blog.objects.all()
    template = 'blog_post_list.html'
    context = {'object_list':qs}
    return render(request, template, context)

@staff_member_required
def blog_post_create_view(request):
    form = BlogModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogModelForm()
    template = 'forms.html'
    context = {'form': form}
    return render(request, template, context)

def blog_post_detail_view(request,slug):
    obj = get_object_or_404(Blog,slug=slug)
    template = 'blog_post_detail.html'
    context = {'object':obj}
    return render(request, template, context)

@staff_member_required
def blog_post_update_view(request,slug):
    obj = get_object_or_404(Blog,slug=slug)
    form = BlogModelForm(request.POST or None , instance = obj)
    if form.is_valid():
        form.save()
    template = 'forms-update.html'
    context = {'form':form, 'title': f"Update {obj.title}"}
    return render(request, template, context)

@staff_member_required
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(Blog,slug=slug)
    template = 'blog_post_delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    context = {'object':obj}
    return render(request, template, context)
