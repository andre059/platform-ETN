from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'password', 'first_name', 'last_name', 'country', 'city', 'is_active',
                  'date_of_birth', 'avatar', 'is_authorized', 'is_authenticated']
