from django.db import models
from user.models import User

# Create your models here.
class Store(models.Model):
    store_url = models.CharField(max_length=100) # https://map.kakao.com/여기
    store_name = models.TextField() #상호명
    address = models.TextField() # 가게 주소
    star = models.TextField() # 가게 별점
    img = models.TextField(max_length=256, default='', null=True)
    content = models.TextField(null=True)
    class meta:
        db_table = 'store'

class Tags(models.Model):
    class meta:
        db_table = 'tags'
    name = models.ManyToManyField(Store, related_name='store')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="comment_set") # 역으로 참조할 때에는 related_name 사용, related_name="comment_set"은 디폴트 값이어서 작성 안해줘도 있는것으로 인식된다.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.content)

