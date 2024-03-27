from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
    
    
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
    
class WomenAPIView(APIView):
    # def get(self, request):
    #     lst = Women.objects.all().values()
    #     return Response({'posts': list(lst)})
    
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})
    
    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        post_new = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id'],    
        )
        # return Response({'post': model_to_dict(post_new)})
        return Response({'post': WomenSerializer(post_new).data})