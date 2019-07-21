from rest_framework import serializers
from .models import User_Message
from .models import Like_And_Dislke
class BoardMessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = User_Message
        fields = ('id', 'title', 'content','created_by','created_at','updated_at','thump_up_count','thump_down_count')

class  Like_And_DisLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Like_And_Dislke
        fields = ('id', 'user_id', 'user_message_id','status','created_at')