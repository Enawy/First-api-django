from rest_framework.response import Response
from rest_framework.decorators import api_view
from customer.models import customer
from .serializers import customerserializer

@api_view(['GET'])
def getdata(request):
    test = customer.objects.all()
    serializer = customerserializer(test, many=True)
    return Response(serializer.data)