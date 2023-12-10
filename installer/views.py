# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  Task, Product, Transaction, Payment
from .serializers import TaskSerializer, ProductSerializer, TransactionSerializer, PaymentSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView



class TaskAPIView(APIView):
    def get(self, request):
        employees = Task.objects.all()
        serializer = TaskSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        headers = self.get_success_headers(serializer.data)  
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class TransactionAPIView(APIView):
    def get(self, request):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentAPIView(APIView):
    # queryset = Payment.objects.all()
    # serializer_class = PaymentSerializer


    def get(self, request):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)