# from rest_framework import viewsets
# from profiles.models import SellerProfile
# from .serializers import SellerSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class=SellerSerializer
#     queryset = SellerProfile.objects.all()


from .serializers import *
from profiles.models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = SellerProfile.objects.all()
    def get(self, format=None):

        seller = SellerProfile.objects.all()
        serializer = SellerSerializer(seller, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class BuyerViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = ClientProfile.objects.all()
    def get(self, format=None):

        seller = ClientProfile.objects.all()
        serializer = UserSerializer(seller, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
