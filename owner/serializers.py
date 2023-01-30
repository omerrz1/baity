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


    def create(self, validated_data):
        # add custom email function here
        return super().create(validated_data)


class ownerDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'phone'
        ]
