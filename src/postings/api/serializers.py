from rest_framework import serializers
from postings.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'url',
            'user',
            'title',
            'content',
            'timestamp',
        ]
        read_only_fields = ['id', 'user']
    
    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Title already exists")
        return value
    
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)