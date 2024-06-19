from django.db import models
from .rare_users import RareUsers

class Posts(models.Model):

  rare_user = models.ForeignKey(RareUsers, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  publication_date = models.DateField()
  image_url = models.CharField(max_length=50)
  content = models.CharField(max_length=50)
  approved = models.BooleanField(default=False)
