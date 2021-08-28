from django.db import models
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, null = True, allow_unicode=True)

    def __str__(self):
        return self.name

class Schoolapp(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200, default="익명의 사자")
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to = "schoolapp/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(250, 230)])
    tags = models.ManyToManyField(Tag, blank=True)
    
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]



