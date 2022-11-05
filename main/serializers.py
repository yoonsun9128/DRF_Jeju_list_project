from rest_framework import serializers
from main.models import Store, Comment

        
class StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__" 
    

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.usernmae
        
    class Meta:
        model = Comment
        exclude = ("store", )


class StoreSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comment_set = CommentSerializer(many=True)
    
    class Meta:
        model = Store
        fields = "__all__"





class CommentCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ("content",)        