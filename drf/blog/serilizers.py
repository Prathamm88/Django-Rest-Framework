from rest_framework import serializers
from .models import Blog,comment





class commentSerializer(serializers.ModelSerializer):
    # comments = commentSerializer(many=True, read_only = True) 
    class Meta :
        model = comment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    comments = commentSerializer(many=True, read_only = True) 
    class Meta :
        model = Blog
        fields = '__all__'
        