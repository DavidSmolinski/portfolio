from rest_framework.generics import ListAPIView

from ratings.models import Rating
from .serializers import Rating_Serializers


class Rating_ListAPIView(ListAPIView):
    """view for the pretty api page"""
    # list of dicts, Each dict has data about someone's survey.
    queryset = Rating.objects.all()
    serializer_class = Rating_Serializers