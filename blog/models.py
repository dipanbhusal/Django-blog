from django.db import models
from django.urls import reverse 
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from .utils import get_read_time
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, default = 1 , on_delete=models.CASCADE )
    title = models.CharField(max_length=100)
    image = models.ImageField(
            upload_to="blog_images/"
            ) 
    content = models.TextField()
    updated = models.DateTimeField(auto_now  = True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now =False, auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    read_time = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)

        if self.content:
            html_string = self.get_markdown()
            read_time = get_read_time(html_string)
            self.read_time  = read_time 
        super(Post, self).save(*args, **kwargs)
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'post_slug': self.slug})  

    
    @property
    def comments(self):
        instance=self 
        qs = Comment.objects.filter_by_instance(instance)
        return qs 
    
    @property
    def get_content_type(self):
        instance = self 
        content_type = ContentType.objects.get_for_model(instance.__class__).model
        return content_type 

