from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Pago
from .serializers import PagoSerializer
from .procesos.cargo import generar_cargo
import json

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
    
@csrf_exempt
def pago_list(request):
    """
    create a new pago.
    """

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PagoSerializer(data=data)
        if serializer.is_valid():
            rpta = generar_cargo(data=data)
            if rpta == '201':
                return JSONResponse(rpta, status=201)
            return JSONResponse(rpta, status=400)
        return JSONResponse(serializer.errors, status=400)

