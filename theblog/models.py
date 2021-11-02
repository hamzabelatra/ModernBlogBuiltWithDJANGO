from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import     RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User,null= True,on_delete=models.CASCADE)
    bio =  RichTextField()
    pic= models.ImageField(null=True, blank=True, upload_to="images/profile")
    ig_url = models.CharField(max_length=255,blank=True, null=True)
    fb_url = models.CharField(max_length=255,blank=True, null=True)
    tw_url = models.CharField(max_length=255,blank=True, null=True)
    linkedin_url = models.CharField(max_length=255,blank=True, null=True)

    def get_photo_url(self):
        if self.pic and hasattr(self.pic, 'url'):
            return self.pic.url
        else:
           return "/media/images/profile/user.jpg"


    def __str__(self):
        return str(self.user)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Post (models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    snippet = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    likes= models.ManyToManyField(User,related_name='blog_post')
    header_image= models.ImageField(null=True, blank=True, upload_to="images/")
    @property
    def get_photo_url(self):
        if self.header_image and hasattr(self.header_image, 'url'):
            return self.header_image.url
       # else:
        #    return "/media/images/user.jpg"


    def total_likes(self):
        return self.likes.count()


    

    def __str__(self):
        return self.title +' | '  +  str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

