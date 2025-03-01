from rest_framework import viewsets, filters, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Game 
from .serializers import GameSerializer 
from django.shortcuts import get_object_or_404


#Listar
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    # Sistema de filtros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]

    search_fields = ['title', 'year', 'price', 'genres' ]
    ordering_fields = ['title', 'year']

    # Sistema de paginación
    pagination_class = PageNumberPagination
    pagination_class.page_size = 8  # juegos por página
    

# CREATE
class GameCreateView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'juego creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)




    


# UPDATE

class GameDetailAPIView(APIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    
    def patch(self, request, pk=None):
        try:

            game = get_object_or_404(Game, pk=pk)
            serializer = GameSerializer(game, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje": "datos actualizados"}, status=status.HTTP_200_OK)
            
        except Exception as e:
            print(str(e))
            return Response({"mensaje": str(e)}, status=status.HTTP_400_BAD_REQUEST)