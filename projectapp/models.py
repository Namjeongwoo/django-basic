from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    # 작성자
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)

    # 타이틀
    title = models.CharField(max_length=200, null=True)

    # 설명
    description = models.TextField(null=True)

    # 이미지
    image = models.ImageField(upload_to='project/', null=False)

    # 생성 일시
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):

        return f'{self.pk} : {self.title}'

