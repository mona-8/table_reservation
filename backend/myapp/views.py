from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer
from django.http import HttpResponse

# def postData(request):
#     # b = Restaurant(name="Buhari",location="Egmore",cuisine="Indian",description="Serves delicious food.",rating=4.5,type="Non-Veg",img_url="xyz",food_img_url_1="abc",food_img_url_2="abc")
#     # b.save()
#     if request.method == 'POST':
#         res = Restaurant(request.POST)
#         if res.is_valid():
#             res.save()
#     return HttpResponse("Weeeeeeeeee!")

@api_view(['POST'])
def postData(request):
    if request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data)
