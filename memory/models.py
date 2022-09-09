from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Memory(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=50,verbose_name="Başlık")
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")
    memory_image=models.FileField(blank=True,null=True,verbose_name="Fotoğraf ekleyin")
    def __str__(self):
        return self.title
class Comment(models.Model):
    memory=models.ForeignKey(Memory,on_delete=models.CASCADE,verbose_name="Anı",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content

