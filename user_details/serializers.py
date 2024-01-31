from rest_framework import serializers
from .models import UserDetails
class UserDetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserDetails
    fields = ['id','username','first_name','last_name','email','password'] # the type of data and format we want it deliver to any request to the api