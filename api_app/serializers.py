from rest_framework import serializers
from .models import CartItem
from .models import Arma
from .models import Monicao


class MonicaoSerializer(serializers.ModelSerializer):
    marca = serializers.CharField(max_length=200)
    modelo = serializers.CharField(max_length=200)
    valor_estimado = serializers.IntegerField(required=False, default=1)



    class Meta:
        model = Monicao
        fields = ('__all__')

class ArmaSerializer(serializers.ModelSerializer):
    marca = serializers.CharField(max_length=200)
    modelo = serializers.CharField(max_length=200)
    quantidade_de_tiros = serializers.IntegerField(required=False, default=1)
    valor_estimado = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = Arma
        fields = ('__all__')
