# importing serializers
from .serializers import OwnerSerializer, ownerDetailsserializer,OTPSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from .emails import send_OTP
from rest_framework.decorators import api_view



# importing the user model
from django.contrib.auth import get_user_model

# saving the onwer in this variable incase i wanted to change the AUTH_USER_MODEL settings
owner = get_user_model()


# an owner class based Createview
class CreateOwner(generics.CreateAPIView):
    queryset = owner.objects.all()
    serializer_class = OwnerSerializer

    def perform_create(self, serializer):

        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data.get('email')
            username = serializer.validated_data.get('username')

            send_OTP(email,username)
            return Response({
                'info':'succes , check email',
                'status':200,
                'data': serializer.data
            })

# verfiy OTP view
@api_view(['POST'])
def verify_OTP(request):
    data = request.data
    serializer = OTPSerializer(data=data)
    if serializer.is_valid():
        email = serializer.data['email']
        OTP = serializer.data['OTP']

        print('eamil', email)
            
        try:
            owner = get_user_model()
            owner = owner.objects.get(email=email)
            owner_otp = owner.OTP
            print('owners otp: ', owner_otp)
        except:
            return Response({
            'account':'not verfied',
            'error':'owner not found'
            }, status=400)
        if owner_otp==int(OTP):
            owner.is_active=True
            owner.save()
            return Response({
                'account':'verfied',
            }, status=200)
        else: 
            return Response({
            'account':'not verfied',
            'error':'wrong code'
                 }, status=400)
    else:
        return Response({
            'account':'not verfied',
            'error':'data not valid'
        }, status=400)

# owners list view
class ownersList(generics.ListAPIView):
    queryset = owner.objects.all()
    serializer_class = ownerDetailsserializer


# delete owner view
class DeleteOwner(generics.DestroyAPIView):
    queryset = owner.objects.all()
    serializer_class = OwnerSerializer
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]

# owner details view
class ownerDetail(generics.RetrieveAPIView):
    serializer_class = ownerDetailsserializer
    queryset = owner.objects.all()
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]

# update owners details view
class UpdateOwner(generics.UpdateAPIView):
    serializer_class = OwnerSerializer
    queryset = owner.objects.all()
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]
