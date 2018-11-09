from rest_framework import serializers
from . models import employess
from . models import ejemplo

class employesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employess
#        fields = ('firstname', 'lastname')
        fields = '__all__'

class ejemploSerializer(serializers.ModelSerializer):
    class Meta:
        model = ejemplo
        #        fields = ('firstname', 'lastname')
        fields = '__all__'
        print(fields)

