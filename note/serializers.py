from rest_framework import serializers
from .models import Note


class NoteModel:
    def __init__(self, title, text):
        self.title = title
        self.text = text


class NoteSerializer(serializers.Serializer):
    title = serializers.CharField()
    text = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.created = instance.created
        instance.user_id = instance.user_id
        instance.save()
        return instance
