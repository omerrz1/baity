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
        send_mail(
                'welcome to baity',
                f'hi {username}, thanks for siging up to baity',
                'omer@baity.uk',
                [f'{user_email}'],
                fail_silently=False,
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
