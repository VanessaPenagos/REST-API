from rest_framework import serializers

class HelloSerielizer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

