from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.fields import ReadOnlyField
import logging
logger=logging.getLogger('django')
from .rid import response_id



class QualList(APIView):
    def get(self,request):
        logger.info(' rid: [{}]'.format(response_id()))
        model=Qualification.objects.all()
        serializer=QualificationSerializer(model,many=True)
        return Response({"r_id":response_id(),"gql":serializer.data})
  


class WorkList(APIView):
    def get(self,request):
        logger.info(' rid: [{}]'.format(response_id()))
        model=Work.objects.all()
        serializer=WorkSerializer(model,many=True)
        return Response({"r_id":response_id(),"gwp":serializer.data})




class TypeList(APIView):
    def get(self,request):
        logger.info('Welcome to Typelist')
        model=Type.objects.all()
        serializer=WorkSerializer(model,many=True)
        return Response({"r_id":response_id(),"gwt":serializer.data})
 
 