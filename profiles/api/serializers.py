from profiles.models import SellerProfile, ClientProfile
from rest_framework import serializers, status
# from models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='password',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # def __str__(self):
    #     return self.user


class ClientSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = ClientProfile
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        buyer, created = ClientProfile.objects.update_or_create(
            user=user,
            # mobileNo=validated_data.pop('mobileNo'),
            # location=validated_data.pop('location'),
            # address=validated_data.pop('address'),

        )
        return buyer


class SellerSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = SellerProfile
        fields = ('user', 'mobileNo', 'cnic',
                  'city', 'address', 'state', 'shop_name')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        seller, created = SellerProfile.objects.update_or_create(user=user,
                                                                 mobileNo=validated_data.pop(
                                                                     'mobileNo'),
                                                                 cnic=validated_data.pop(
                                                                     'cnic'),
                                                                 city=validated_data.pop(
                                                                     'city'),
                                                                 address=validated_data.pop(
                                                                     'address'),
                                                                 shop_name=validated_data.pop(
                                                                     'shop_name'),
                                                                 )
        return seller
