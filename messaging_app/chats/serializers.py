from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ['user_id', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    message_body = serializers.CharField()

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at']

class ConversationSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']

    def validate(self, data):
        if data.get('participants').count() < 2:
            raise serializers.ValidationError("A conversation should have at least two participants.")
        return data

    def get_messages(self, obj):
        messages = obj.message_set.all()
        return MessageSerializer(messages, many=True).data