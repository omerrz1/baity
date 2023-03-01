from django.contrib.auth import get_user_model
from rest_framework import serializers


# #  request = self.request
#         data = request.data 
#         email = data['email']
#         print ('account created for ',email)
#         check_owner = get_user_model()
#         check_owner = check_owner.get(email=email,confirmed= False)
#         if check_owner:
#             print(check_owner,'will be deleted')
#             check_owner.delete()




class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'phone',
            'password',
            'email'
        ]
   

# otp serilaizer
class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    OTP = serializers.IntegerField()



class ownerDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'email',
            'phone'
        ]



class Update_username_phone_serializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =[
            'username',
            'phone'
        ]



class update_email_serializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields=[
            'email'
        ]