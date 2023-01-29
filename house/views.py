from rest_framework import generics, permissions
from . models import House
from . serializers import houseserializer, photoserializer
import random

# list houses
class MainHouses(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = houseserializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs =qs.filter(public = True)
        houses = list(qs)
        random.shuffle(houses)
        return houses

#list houses that were created by the user

class Myhouses(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = houseserializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(owner=user)
        return qs





class SearchHouse(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = houseserializer


    def get_queryset(self):
        qs = super().get_queryset()
        q= self.request.query_params.get('q')
        print (q)
        address_query = qs.filter(address__icontains=q, public = True)
        description_query = qs.filter(description__icontains=q, public = True)
        qs = [*address_query , *description_query]

        def unique(ls):
            unique_ls = []
            for item in ls:
                if item not in unique_ls:
                    unique_ls.append(item)
            return unique_ls

        return unique(qs)


# create a houes
class CreateHouse(generics.CreateAPIView):
    serializer_class = houseserializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

# add the photos to the house
class CreatePhotos(generics.CreateAPIView):
    serializer_class = photoserializer


#house details view
class HouseDetails(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = houseserializer
    lookup_field = 'pk'


#update house view
class UpdateHouse(generics.UpdateAPIView):
    queryset =  House.objects.all()
    serializer_class = houseserializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(owner=user)
        return qs

#destroy houes viwe
class DeleteHouse(generics.DestroyAPIView):
    queryset = House.objects.all()
    serializer_class = houseserializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(owner=user)
        return qs




