# importing serializers
from .serializers import OwnerSerializer, ownerDetailsserializer,OTPSerializer, update_email_serializer,Update_username_phone_serializer,update_pass_serializer
from rest_framework import generics, permissions,authentication
from rest_framework.response import Response
from .emails import send_OTP
from rest_framework.decorators import api_view,permission_classes,authentication_classes



# importing the user model
from django.contrib.auth import get_user_model

# saving the onwer in this variable incase i wanted to change the AUTH_USER_MODEL settings
owner = get_user_model()


# an owner class based Createview
class CreateOwner(generics.CreateAPIView):
    queryset = owner.objects.all()
    serializer_class = OwnerSerializer

    def initial(self, request, *args, **kwargs):
        # Get the request data before it is validated
        data = request.data
        print (dict(data))
        if data['email']:
            email = data['email']

            print ('!!! !!!! inittial account created for ',email)
            check_owner = get_user_model()
            try:
                check_owner = check_owner.objects.get(email=email,confirmed= False)
                if check_owner:
                    print(check_owner,'will be deleted because it wasnt verified')
                    check_owner.delete()
            
            except:
                pass
        # Call the parent class's initial method
        super().initial(request, *args, **kwargs)

    def perform_create(self, serializer):
            if serializer.is_valid():
                serializer.save()
                email = serializer.validated_data.get('email')
                username = serializer.validated_data.get('username')

                send_OTP(email,username,template='OTP.html')
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
        if owner_otp==OTP:
            owner.is_active=True
            owner.confirmed= True
            owner.OTP=0
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



@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.TokenAuthentication])
def verfiy_email(request):
    user = request.user
    email = user.email
    send_OTP(email=email,username=user.username,template='emailOTP.html')
    return Response({'email sent to :':email})


# owners list view
class ownersList(generics.ListAPIView):
    queryset = owner.objects.all()
    serializer_class = ownerDetailsserializer


# delete owner view
class DeleteOwner(generics.DestroyAPIView):
    queryset = owner.objects.all()
    serializer_class = OwnerSerializer
    lookup_field = 'email'
    permission_classes = [permissions.IsAuthenticated]




@api_view(["GET",'POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.TokenAuthentication])
def delete_me(request, *args,**KWargs):
    owner = request.user
    name = owner.username
    owner.delete()
    return Response({'account deleted: ': name})
    

# owner details view
class ownerDetail(generics.RetrieveAPIView):
    serializer_class = ownerDetailsserializer
    queryset = owner.objects.all()
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]

# update owners details view
class UpdateOwner_username_phone(generics.UpdateAPIView):
    serializer_class = Update_username_phone_serializer
    queryset = owner.objects.all()
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        qs= super().get_queryset()
        id = self.request.user.id
        qs = qs.filter(id=id)
        return qs



class UpdateOwner_email(generics.UpdateAPIView):
    serializer_class = update_email_serializer
    queryset = get_user_model().objects.all()
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        qs = super().get_queryset()
        id = self.request.user.id
        qs = qs.filter(id =id)
        return qs

# update password
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.TokenAuthentication])
@api_view(["PUT"])
def Update_password(request, *args,**KWargs):
    user = request.user
    id = user.id
    print('!!! id = ',id)
    serialzer =update_pass_serializer(data=request.data)
    if serialzer.is_valid(raise_exception=True):
        body= request.data
        new_password = body['password']
        password = user.set_password(new_password)
        user.save()
        return Response({'password': password})
    return Response({'error':'something went wrong'})
        


class MyProfile(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class= ownerDetailsserializer
    queryset = owner.objects.all()

    def get_queryset(self):
        email = self.request.user.email
        qs = super().get_queryset()
        qs = qs.filter(email = email)
        return qs


