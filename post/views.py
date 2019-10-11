from django.shortcuts import render
from .models import Post,Product
from .serializer import PostSerializer,ProductSerializer
from rest_framework import viewsets,permissions

#@action
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    def highlight(self,request,*args,**kwargs):
        return HttpResponse("얍")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    def highlight(self,request,*args,**kwargs):
        return HttpResponse("얍")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
