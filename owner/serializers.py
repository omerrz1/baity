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


# otp serilaizer 
class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    OTP = serializers.CharField()

    

class ownerDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'phone'
        ]
