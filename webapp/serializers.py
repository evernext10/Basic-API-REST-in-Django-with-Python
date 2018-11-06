from rest_framework import serializers
from . models import employess

class employesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employess
#        fields = ('firstname', 'lastname')
        fields = '__all__'