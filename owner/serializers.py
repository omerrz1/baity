from django.contrib.auth import get_user_model
from rest_framework import serializers






class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'phone',
            'password',
            'email'
        ]



class ownerDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'phone'
        ]
