from django import forms
from .models import Blog

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','slug','content']

def clean_title(self, *args , **kwargs):
    instance = self.instance
    title = self.cleaned_data.get('title')
    qs = Blog.objects.filter(title__iexact = title)
    if instance is not None:
        qs = qs.exclude(pk = instance.pk)
    if qs.exists():
        raise forms.ValidationError("This title is already used..!")
    return title
