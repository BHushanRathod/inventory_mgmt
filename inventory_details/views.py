from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from inventory_details.models import InvertoryStack, Purchase


class ListInventoyry(APIView):
    @staticmethod
    def get(request):
        inventory_obj = InvertoryStack.objects.all().values('id', 'quantity', 'name')
        return Response(inventory_obj, status=status.HTTP_200_OK)


class PurchaseView(APIView):
    def get(self, request):
        return Response(Purchase.objects.all().values(), status=status.HTTP_200_OK)

    def post(self, request):
        item_id = request.data['item']
        quantity = request.data['quantity']

        item_obj = InvertoryStack.objects.get(id=item_id)
        if int(quantity) > item_obj.quantity:
            return Response({'Purchase Quantity can not be greater than actual quantity'}, status=status.HTTP_200_OK)
        else:
            Purchase.objects.create(item_id=item_obj, quantity=quantity)
            remain_item = item_obj.quantity - int(quantity)
            InvertoryStack.objects.filter(id=item_id).update(quantity=remain_item)
            return Response({'Item Purchased'}, status=status.HTTP_200_OK)
