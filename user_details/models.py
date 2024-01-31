from django.db import models

class UserDetails(models.Model):
  username = models.CharField(max_length = 200)
  first_name = models.CharField(max_length = 200)
  last_name = models.CharField(max_length = 200)
  email = models.EmailField(max_length = 50)
  password = models.CharField(max_length = 200)


  def __str__(self):#how each object will be presented by default in the admin inside drinks dir 
    return self.username