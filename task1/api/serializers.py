from rest_framework import serializers
from customer.models import customer

class customerserializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'