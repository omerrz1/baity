from django.db import models
from django.contrib.auth import get_user_model


class House(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='owner')
    price = models.IntegerField(default=0)
    area = models.IntegerField(null=True)
    address = models.TextField(null=True)
    description = models.TextField(null=True)
    public = models.BooleanField(default= True)
    bed_rooms = models.IntegerField(default=0)
    bath_rooms = models.IntegerField(default=0)
    living_rooms = models.IntegerField(default=0)
    rent = models.BooleanField(default=True)
    sell = models.BooleanField(default=False)

    def contact (self):
        return self.owner.phone

    def __str__(self):
        return self.address


class photo(models.Model):
    photo = models.ImageField(upload_to='media')
    house = models.ForeignKey(
        House, related_name='photos', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.photo)
