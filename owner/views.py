# importing serializers
from .serializers import OwnerSerializer, ownerDetailsserializer
from rest_framework import generics, permissions



# importing the user model
from django.contrib.auth import get_user_model

# saving the onwer in this variable incase i wanted to change the AUTH_USER_MODEL settings
owner = get_user_model()


# an owner class based Createview
class CreateOwner(generics.CreateAPIView):
    queryset = owner.objects.all()
    serializer_class = OwnerSerializer


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
