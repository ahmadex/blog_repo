from django.db import models
from accounts.models import User
from datetime import date
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    descritption = models.TextField()
    author = models.ForeignKey(User, related_name='blog', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    publish_date = models.DateField(auto_now_add=False, blank=True, null=True)

    def publish(self):
        self.publish_date = date.today() 

    def __str__(self):
        return self.title
    