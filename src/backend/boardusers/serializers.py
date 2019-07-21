from rest_framework import serializers
from .models import Users
class BoardUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'account','password','created_at','updated_at')