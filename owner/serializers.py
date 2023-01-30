from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.mail import send_mail



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
        send_mail(
            subject=f'welcome {username}',
            message=message,
            from_email='omermajdi250@gmail.com',
            recipient_list=[user_email],
            auth_password='mero999999'
        )
        return super().create(validated_data)


class ownerDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'phone'
        ]
