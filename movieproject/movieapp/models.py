from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)

    class Meta:
        ordering=('category_name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('movieapp:category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.category_name)

class Movie(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    img = models.ImageField(upload_to='gallery')
    desc=models.TextField()
    release=models.DateField()
    actors= models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    trailer_link = models.URLField(blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.name



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_text = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating_value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)