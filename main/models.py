from django.db import models
from user.models import User

# Create your models here.
class Store(models.Model):
    store_url = models.CharField(max_length=100) 
    store_name = models.TextField() 
    address = models.TextField() 
    star = models.TextField() 
    img = models.TextField(max_length=256, default='', null=True)
    content = models.TextField(null=True)
    class meta:
        db_table = 'store'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="comment_set")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.content)

