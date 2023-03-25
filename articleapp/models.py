from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Article(models.Model):
    # 작성자
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

    # 타이틀
    title = models.CharField(max_length=200, null=True)

    # 이미지
    image = models.ImageField(upload_to='article/', null=False)

    # 콘텐츠
    content = models.TextField(null=True)

    # 생성 일시
    create_at = models.DateField(auto_now_add=True, null=True)


