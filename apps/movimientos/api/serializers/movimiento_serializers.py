from rest_framework import serializers


class MovimientosListSerializer(serializers.Serializer):
    cod_movimiento = serializers.DecimalField(max_digits=18, decimal_places=0)
    nombres = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    dni = serializers.CharField(max_length=25)
    sexo = serializers.CharField(max_length=1)
    cargo = serializers.CharField(max_length=100, allow_blank=True)
    empresa = serializers.CharField(max_length=100)
    fecha_movimiento = serializers.DateTimeField()
    fecha_salida = serializers.CharField(allow_null=True, allow_blank=True)
    tipo_ingreso = serializers.CharField(max_length=50, allow_blank=True)
    tipo_personal = serializers.CharField(max_length=50)
    imagen = serializers.CharField(max_length=255)

    class Meta:
        fields = '__all__'



# class MovimientosDiaSerializer(serializers.Serializer):
#     cod_movimiento = serializers.DecimalField(max_digits=18, decimal_places=0)
#     nombres = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
#     dni = serializers.CharField(max_length=25)
#     sexo = serializers.CharField(max_length=1)
#     cargo = serializers.CharField(max_length=100, allow_blank=True)
#     empresa = serializers.CharField(max_length=100)
#     fecha_movimiento = serializers.DateTimeField()
#     fecha_salida = serializers.CharField(allow_blank=True, allow_null=True)
#     tipo_ingreso = serializers.CharField(max_length=50, allow_blank=True)
#     tipo_personal = serializers.CharField(max_length=50)
#     imagen = serializers.CharField(max_length=255)
#
#     class Meta:
#         fields = '__all__'
