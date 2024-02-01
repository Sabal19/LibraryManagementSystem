from rest_framework import serializers
from datetime import datetime

from .models import User


class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['name','email','membership_date']

    

    def validate(self,data):
        name = data.get('name')
        if not name:

            raise serializers.ValidationError("Name field cannot be empty")
        
        return data