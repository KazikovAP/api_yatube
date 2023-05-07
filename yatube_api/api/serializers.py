from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only='True')

    class Meta:
        model = Post
        fields = ('id', 'author', 'group', 'text', 'image', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'slug', 'title', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only='True')
    # post = serializers.PrimaryKeyRelatedField(read_only=True)
    '''
    Роман, исправил как ты предложил, всё работает.
    Но наставник предложил вообще убрать эту строчку,
    и заменить на третью строчку в классе Meta,
    не знаю, какой вариант лучше, но всё вроде работает.
    '''

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post', 'author')
