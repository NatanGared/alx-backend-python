from django.urls import path, include
from rest_framework import routers 
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-message')

urlpatterns = router.urls + nested_router.urls