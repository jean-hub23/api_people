from django.db import connection
from rest_framework.response import Response
from apps.movimientos.api.serializers.movimiento_serializers import *
from rest_framework import viewsets, status


class MovimientosViewSet(viewsets.GenericViewSet):
    serializer_class = MovimientosListSerializer

    def list(self, request):

        data = []
        cursor = connection.cursor()

        try:

            params = self.request.query_params.dict()

            tipoMovimiento = params['tipoMovimiento']
            idServicio = params['idServicio']
            tipoPersonal = params['tipoPersonal']

            cursor.execute("EXEC [dbo].[AppCA_ListadoMovimientosPeople] {0}, {1}, {2} , {3}".format(idServicio, tipoPersonal, "''", tipoMovimiento))

            movimientos_data = cursor.fetchall()

            for movimiento in movimientos_data:

                dataTemp = {
                    'cod_movimiento': movimiento[0],
                    'nombres': movimiento[1],
                    'dni': movimiento[2],
                    'sexo': movimiento[3],
                    'cargo': movimiento[4],
                    'empresa': movimiento[5],
                    'fecha_movimiento': movimiento[6],
                    'fecha_salida': '' if movimiento[7] is None else movimiento[7],
                    'tipo_ingreso': movimiento[8],
                    'tipo_personal': movimiento[9],
                    'imagen': movimiento[10],
                }

                data.append(dataTemp)

            movimientos_serializer = self.get_serializer(data=data, many=True)

            if movimientos_serializer.is_valid():
                return Response(movimientos_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(movimientos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        finally:
            cursor.close()


# class MovimientosDiaViewSet(viewsets.GenericViewSet):
#     serializer_class = MovimientosDiaSerializer
#
#     def list(self, request):
#
#         data = []
#         cursor = connection.cursor()
#
#         try:
#             params = self.request.query_params.dict()
#             idServicio = params['idServicio']
#             tipoPersonal = params['tipoPersonal']
#
#             cursor.execute("EXEC [dbo].[AppCA_ListadoMovimientosPeople] {0}, {1}, {2} , {3}".format(idServicio, tipoPersonal, "''",2))
#
#             movimientos_data = cursor.fetchall()
#
#             for movimiento in movimientos_data:
#                 dataTemp = {
#                     'cod_movimiento': movimiento[0],
#                     'nombres': movimiento[1],
#                     'dni': movimiento[2],
#                     'sexo': movimiento[3],
#                     'cargo': movimiento[4],
#                     'empresa': movimiento[5],
#                     'fecha_movimiento': movimiento[6],
#                     'fecha_salida': movimiento[7],
#                     'tipo_ingreso': movimiento[8],
#                     'tipo_personal': movimiento[9],
#                     'imagen': movimiento[10],
#                 }
#
#                 data.append(dataTemp)
#
#             movimientos_serializer = self.get_serializer(data=data, many=True)
#
#             if movimientos_serializer.is_valid():
#                 return Response(movimientos_serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response(movimientos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         finally:
#             cursor.close()
