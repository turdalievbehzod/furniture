from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=32)
    
    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return f"{self.id} | {self.title}"

class Post(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to='products/')
    info = models.CharField(max_length=128)
        
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        
    def __str__(self):
        return f"{self.id} | {self.title}"
    
class Tag(models.Model):
    title = models.CharField(max_length=128)
    
    class Meta:
        db_table = 'tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        