from django.db import models

# Create your models here.


class Recomender(models.Model):
    title = models.CharField(max_length=255, null=False) # CharField 글 제목 같이 짧은 문자열 정보를 저장할때 사용
    author = models.CharField(max_length=255, null=False)
    answer = models.IntegerField()
    
