from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Held
from .serializers import HeldSerializer


class HeldViewSet(viewsets.ModelViewSet):
    serializer_class = HeldSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Held.objects.none()
        return Held.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

