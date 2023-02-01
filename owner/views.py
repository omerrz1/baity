# importing serializers
from .serializers import OwnerSerializer, ownerDetailsserializer,OTPSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from .emails import send_OTP



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



        





# verfiy email OTP view her //////
class OTPVerfiy(generics.CreateAPIView):
    serializer_class = OTPSerializer

    def perform_create(self, serializer):
        request = self.request
        data = request.data

        serializer = OTPSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data['email']
            OTP = serializer.data['OTP']

            owner = owner.objects.get(email=email)
            owner.is_active=True
            owner.save()
            return Response({
                'status':200,
                'account':'verfied'
            })
        else:
            return Response({
                'status':400,
                'account':'not verfied'
            })



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
