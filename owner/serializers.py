from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.mail import EmailMessage
from django.conf import settings




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
        user_email = validated_data['email']
        username = validated_data['username']
        message = f'hi {username} welcome to baity app' 
        email = EmailMessage(
            f'wlecome {username}',
            message,
            settings.EMAIL_HOST_USER,
            [user_email]
        )
        email.fail_silently = False
        email.send()
        return super().create(validated_data)


class ownerDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'phone'
        ]
