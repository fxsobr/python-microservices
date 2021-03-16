from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Produto
from .serializer import ProdutoSerializer


class ProdutoViewSet(viewsets.ViewSet):
    def list(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        produto = Produto.objects.get(id=pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    def update(self, request, pk=None):
        produto = Produto.objects.get(id=pk)
        serializer = ProdutoSerializer(instance=produto, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        produto = Produto.objects.get(id=pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
