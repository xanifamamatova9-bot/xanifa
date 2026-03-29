from django.db import models

class Post(models.Model):
  mavzu=models.CharField(max_length=200)
  tana=models.TextField()
  rasm=models.FileField(upload_to="post_rasmi")
  yaratilgan_vaqti=models.DateTimeField(auto_now_add=True)
class Meta:
  app_label='postapp'
  

# from postapp.models import Modellar

# post = Modellar(
#     mavzu="Salom",
#     tana="Bu birinchi post",
# )
# post.save()

