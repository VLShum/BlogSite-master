from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
class Blog(models.Model):
    user = models.ForeignKey(User, default = 1, null = True , on_delete = models.SET_NULL )
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,null=True)
    content = models.TextField(null=True,blank=True)
    published_date = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['-published_date','-timestamp','-updated']

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"
    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"
