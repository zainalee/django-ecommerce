from products.models import Product, Categories
from rest_framework import viewsets
from .serializers import ProductSerializers, CategoriesSerializers
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
import json
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes

#  {ListAPIView,
# RetrieveAPIView,
# CreateAPIView,
# DestroyAPIView,
# UpdateAPIView}


@api_view(['GET', ])
def api_detail_product_view(request, pk):

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": status.HTTP_404_NOT_FOUND})

    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response({
            "status": status.HTTP_200_OK,
            "result": serializer.data,
        })


class ProductAPIView(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['title']

# @api_view(['GET', ])
# def checkout(request)

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     if queryset == "":
    #         message = "no data avaialable"
    #         return Response({"error": status.HTTP_204_NO_CONTENT})

    # def list(self, request):
    #     if self.filter_backends == '':
    #         return self.response
    # print(filter_backends)
    # print(search_fields)

    # def list(self, request):
    #     filter_backends = (SearchFilter)
    #     search_fields = ['title', 'category']
    #     queryset = Product.objects.all()
    #     serializer = ProductSerializers(queryset, many=True)
    #     message = "success"
    #     return Response({
    #         "message": message,
    #         "status": status.HTTP_201_CREATED,
    #         "Record": serializer.data
    #     })

    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = Product.objects.all()
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(title__icontains=query)
    #         ).distinct()
    #     return queryset_list
    # return Response({
    #     "message": "success",
    #     "status": status.HTTP_201_CREATED,
    #     "Record": queryset_list
    # })

    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     filter_backends = (SearchFilter, OrderingFilter)
    #     search_fields = ['title']
    #     return
    # else:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryAPIView(ListAPIView):
    def list(self, request):
        queryset = Categories.objects.all()
        serializer = CategoriesSerializers(queryset, many=True)
        if serializer.data is None:
            return Response({
                "message": "Data Not Found"
            })
        else:
            return Response({
                "message": "success",
                "status": status.HTTP_200_OK,
                "Record": serializer.data
            })


# class ProductViewSet(viewsets.ModelViewSet):
#     pass
    #     search_fields = ['title']
    #     filter_backends = (filters.SearchFilter,)
    #     serializer_class = ProductSerializers
    #     queryset = Product.objects.all()
    #  def get_queryset(self):
    #         user = self.request.user
    #     return user.purchase_set.all()
    #     message = "success"
    #     return Response({
    #         "message": message,
    #         "status": status.HTTP_201_CREATED,
    #         "Record": serializer,
    #     })
    # permission_classes = []

    # def get (self,request, *args, **kwargs):
    #     if request.method =='GET':
    #         snippets = Product.objects.all()
    #         serializer = ProductSerializers(snippets, many=True)
    #         return Response(serializer.data)

    #     if request.method == 'POST':
    #         serializer = ProductSerializers(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response (
    #             {
    #             "message":"Success",
    #             "status" : 200,
    # "result": ax.data,
    # "result_count" : qs.count()

    # })
    # elif:
    #     return Response(
    #     {
    #         'message':fail,
    #         "status" : 400,
    #     }
    # )


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializers
    queryset = Categories.objects.all()
