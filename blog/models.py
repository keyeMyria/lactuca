from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    create_time = models.TimeField(auto_now_add=True)
    modify_time = models.TimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
