from django.shortcuts import render
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings

from .models import *
from .serializers import *
from .permissions import IsCustomerOrTasker

# Create your views here.

class TaskerView(generics.ListAPIView):
    queryset = Tasker.objects.filter(is_active = True)
    serializer_class = TaskerSerializer


class TaskerDetailView(generics.RetrieveAPIView):
    queryset = Tasker.objects.filter(is_active = True)
    serializer_class = TaskerSerializer


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_active = True)
    serializer_class = BlogListSerializer


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.filter(is_active = True)
    serializer_class = BlogDetailSerializer


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class SubServiceListView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class SubServiceDetailView(generics.RetrieveAPIView):
    queryset = SubService.objects.filter(is_active=True)
    serializer_class = SubServiceSerializer


class ServiceChoiceList(generics.ListAPIView):
    queryset = ServiceBook.objects.all()
    serializer_class = ServiceChoiceSerializer


class ServiceChoiceDetail(generics.RetrieveAPIView):
    queryset = ServiceBook.objects.all()
    serializer_class = ServiceChoiceSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateSerializer
        return OrderListSerializer
    
    def perform_create(self, serializer):
        order = serializer.save()

        send_mail(
            'New Order Created',
            'Thank you for your order. Your order has been created successfully.',
            settings.EMAIL_HOST_USER,
            [order.customer],
            fail_silently=False
        )

        send_mail(
            'New Order Assigned',
            f'You have been assigned a new order. Order ID: {order.id}',
            settings.EMAIL_HOST_USER,
            [order.tasker],
            fail_silently=False,
        )


class OrderDetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsCustomerOrTasker]
