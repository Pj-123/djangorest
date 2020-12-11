from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.fields import ReadOnlyField
import logging
logger=logging.getLogger('django')
from .rid import response_id



class Infolist(APIView):
    def get(self,request):
        logger.info(' rid: [{}]'.format(response_id()))
        model=Student.objects.all()
        serializer=QualificationSerializer(model,many=True)
        return Response({"r_id":response_id(),"res":serializer.data})
  

