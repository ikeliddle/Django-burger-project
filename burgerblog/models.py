from django.db import models

# Create your models here.
class Quote(models.Model):
    blog_name = models.CharField(max_length=30)
    quote_text = models.CharField(max_length=140)
    def __str__(self):
        return self.blog_name + ' ' + self.quote_text