from django.db import models

# Create your models here.
class Store(models.Model):
    store_id = models.CharField(max_length=100) # https://map.kakao.com/여기
    store_name = models.TextField() #상호명
    address = models.TextField() # 가게 주소
    menu = models.TextField() # 가게 메뉴 카테고리 ex 한식 횟집
    star = models.TextField() # 가게 별점
    content = models.TextField(null=True) #리뷰 내용
    img = models.ImageField(null=True)


