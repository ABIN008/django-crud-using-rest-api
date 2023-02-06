from rest_framework import generics
from .models import Names,Details
from .serializers import NameSerializer,DetailSerializer

class DetailsList(generics.ListCreateAPIView):
    serializer_class=DetailSerializer

    def get_queryset(self):
        queryset=Details.objects.all()
        sports_item=self.request.query_params.get('sports_item')
        if sports_item is not None:
            queryset = queryset.filter(Items=sports_item)
        return queryset

class DetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailSerializer

class NamesList(generics.ListCreateAPIView):
    queryset = Names.objects.all()
    serializer_class =NameSerializer


class NamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Names.objects.all()
    serializer_class = NameSerializer