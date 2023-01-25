from rest_framework import serializers
from . models import House, photo


class photoserializer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = ['photo', 'house']


class houseserializer(serializers.ModelSerializer):
    photos = photoserializer(read_only=True, many=True)
    owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = House
        fields = [
            'id',
            'price',
            'owner',
            'area',
            'address',
            'description',
            'public',
            'bed_rooms',
            'bath_rooms',
            'living_rooms',
            'photos',
        ]
    
    
    def get_owner(self,obj):
        return obj.owner.username



