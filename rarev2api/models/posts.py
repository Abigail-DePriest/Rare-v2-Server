from django.db import models
from .users import Users

class Posts(models.Model):

  rare_user = models.ForeignKey(Users, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  publication_date = models.DateField()
  image_url = models.CharField(max_length=50)
  content = models.CharField(max_length=50)
  approved = models.BooleanField(default=False)
