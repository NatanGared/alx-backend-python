from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, editable=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role_choices = (
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=role_choices)
    created_at = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, editable=False)
    participants = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    