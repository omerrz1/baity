from rest_framework import serializers
from . models import House, photo


class photoserializer(serializers.ModelSerializer):
    key= serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = photo
        fields = ['photo', 'house','key']
    
    
    def get_key(self,obj):
        return str(obj.id)



class houseserializer(serializers.ModelSerializer):
    photos = photoserializer(read_only=True, many=True)
    owner = serializers.SerializerMethodField(read_only=True)
    key = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = House
        fields = [
            'key',
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

    
    def get_key(self,obj):
        return str(obj.id)



