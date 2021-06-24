from rest_framework import serializers

from .models import Code
from CouponAPI.constants import VALIDATION


class CodeSerializer(serializers.Serializer):
    """
    Serializing of model Code.
    """
    code = serializers.CharField()
    discount = serializers.IntegerField(default=15)
    active = serializers.BooleanField(default=True)

    def validate(self, data):
        """
        Check that the code is already present in database or not.
        """
        if len(data['code']) > 10 or len(data['code']) == 0:
            raise serializers.ValidationError(VALIDATION[0][1])
        elif Code.objects.filter(code=data['code']).exists():
            raise serializers.ValidationError(VALIDATION[1][2])
        elif data['discount'] < 0 or data['discount'] > 100:
            raise serializers.ValidationError(VALIDATION[2][2])
        return data

    def create(self, validated_data):
        """
        Create new instance of an model after validating serialized data.
        """
        return Code.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing instance after validating serialized data.
        """
        instance.code = validated_data.get('code', instance.code)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
