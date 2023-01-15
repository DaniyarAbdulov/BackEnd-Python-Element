from django.contrib.admin import actions
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework.decorators import action, api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from . import models, serializers


class ProductViewSet(ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = models.Product.objects.filter(category=category)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)



