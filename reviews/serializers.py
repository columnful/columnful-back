from rest_framework import serializers
from .models import Review, Comment

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'username', 'honor', 'movie_title', 'rank' )  
        # username이 있어야 vue에서 review를 통해 username을 가져올 수 있고, username을 가져와야 현재 로그인 한 유저와 일치하는 지 확인 후 update delete 가능


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'user', 'username')