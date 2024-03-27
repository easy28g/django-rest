from rest_framework import generics, viewsets, mixins, views
from .models import Women, Category
from .serializers import WomenSerializer   
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


class WomenViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        
        if not pk:
            return Women.objects.all()[:3]
        
        return Women.objects.filter(pk=pk)
    
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
        


#Easy

# class WomenListAPIView(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
    
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
    
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
  
  
#Medium  
    
# class WomenAPIView(APIView):
    
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
    
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
    
    
#     def delete(self, request, pk):
#         try:
#             instance = Women.objects.get(pk=pk)
#         except Women.DoesNotExist:
#             return Response({"error": "Object does not exist"})
        
#         serializer = WomenSerializer(data=request.data)
#         serializer.delete(instance)
#         return Response({"success": "Object deleted successfully"})

#Hard

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

    # def get(self, request):
    #     lst = Women.objects.all().values()
    #     return Response({'posts': list(lst)})
        
        # post_new = Women.objects.create(
        #     title = request.data['title'],
        #     content = request.data['content'],
        #     cat_id = request.data['cat_id'],    
        # )
        # return Response({'post': model_to_dict(post_new)})
        # return Response({'post': WomenSerializer(post_new).data})