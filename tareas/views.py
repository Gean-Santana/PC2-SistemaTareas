from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Lista, Tarea, Etiqueta
from .serializers import ListaSerializer, TareaSerializer, EtiquetaSerializer

class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    # Marcar tarea como completada
    @action(detail=True, methods=['post'])
    def completar(self, request, pk=None):
        tarea = self.get_object()
        tarea.completada = True
        tarea.save()
        return Response({'status': 'tarea completada'})

    # Filtrar tareas
    def get_queryset(self):
        queryset = Tarea.objects.all()
        prioridad = self.request.query_params.get('prioridad')
        fecha = self.request.query_params.get('fecha_limite')
        estado = self.request.query_params.get('completada')

        if prioridad:
            queryset = queryset.filter(prioridad=prioridad)
        if fecha:
            queryset = queryset.filter(fecha_limite=fecha)
        if estado is not None:
            queryset = queryset.filter(completada=(estado.lower() == 'true'))

        return queryset

    # Asignar etiquetas a una tarea
    @action(detail=True, methods=['post'])
    def asignar_etiquetas(self, request, pk=None):
        tarea = self.get_object()
        etiquetas_ids = request.data.get('etiquetas', [])
        tarea.etiquetas.set(etiquetas_ids)
        tarea.save()
        return Response({'status': 'etiquetas asignadas'})
