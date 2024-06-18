from django.db import models

class Posts(models.Model):
  first_name = models.CharField(max_length=50) 
  last_name = models.CharField(max_length=50)
  bio = models.CharField(max_length=50)
  profile_image_url = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  created_on = models.DateField()
  active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  uid = models.CharField(max_length=50)
