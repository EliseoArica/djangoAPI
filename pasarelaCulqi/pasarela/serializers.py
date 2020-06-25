from rest_framework import serializers
from .models import Pago


class PagoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pago
        fields = ('id','amount', 'currency_code', 'description', 'email', 'source_id')

    id = serializers.IntegerField(read_only=True)
    amount = serializers.IntegerField()
    currency_code = serializers.CharField()
    description = serializers.CharField()
    email = serializers.CharField()
    source_id = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new 'Pago' instance, given the validated data.
        """
        return Pago.objects.create(**validated_data)
