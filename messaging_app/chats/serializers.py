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
    messages = MessageSerializer(many=True, read_only=True)
    
    def validate(self, attrs):
        if len(attrs.get('messages')) > 100:
            raise serializers.ValidationError("Too many messages in the conversation.")
        return attrs

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']