from rest_framework import generics, filters, permissions
from apps.faq.serializers import FaqSerializer
from apps.faq.models import Faq


class FAQListView(generics.ListAPIView):
    serializer_class = FaqSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Faq.objects.all()
