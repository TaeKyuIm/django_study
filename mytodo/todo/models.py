from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True) # 생성일 자동 추가
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title # admin 페이지에서 제목으로 객체들이 표시됨.