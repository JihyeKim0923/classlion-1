from .models import Post,Product
from .serializer import PostSerializer,ProductSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class PostList(APIView):
    def get(self,request):
        posts=Post.objects.all()
        serializer=PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serialrizer=PostSerializer(data=request.data)
        if serialrizer.is_valid():
            serialrizer.save()
            return Response(serialrizer.data, status=status.HTTP_201_CREATED)
        return Response(serialrizer.errors,status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self,request,pk,format=None):
        post=self.get_object(pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        post=self.get_object(pk)
        serializer=PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        post=self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data)

    def product(self, request):
        serialrizer=ProductSerializer(data=request.data)
        if serialrizer.is_valid():
            serialrizer.save()
            return Response(serialrizer.data, status=status.HTTP_201_CREATED)
        return Response(serialrizer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self,request,pk,format=None):
        product=self.get_object(pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        product=self.get_object(pk)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        product=self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)