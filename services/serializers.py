from rest_framework import serializers
from django.urls import reverse

from .models import *
from users.serializers import UserSerializer


class TaskerSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskerSkills
        fields = '__all__'

class TaskerCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskerCertificate
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class TaskerSerializer(serializers.ModelSerializer):

    skills = TaskerSkillsSerializer(many=True)
    certificate = TaskerCertificateSerializer(many=True)
    work_cities = CitySerializer(many=True)

    user = UserSerializer()

    class Meta:
        model = Tasker
        fields = ('id', 'user', 'address', 'bio', 'rating', 'tasks_done',
                  'skills', 'certificate', 'work_cities', 'is_available',
                  'created_at')


class BlogListSerializer(serializers.ModelSerializer):

    author = serializers.HyperlinkedRelatedField(
        view_name='tasker-detail',
        read_only=True,
        lookup_field='pk'
    )

    detail = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('id', 'author', 'title', 'summary', 'thumbnail', 'created_at', 'detail')

    def get_detail(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('blog-detail', args=[obj.id]))


class BlogDetailSerializer(serializers.ModelSerializer):

    author = TaskerSerializer()

    class Meta:
        model = Blog
        fields = ('id', 'author', 'title', 'summary', 'thumbnail', 'full_text', 'created_at')


class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = ('id', 'title', 'description', 'thumbnail', 'price')


class ServiceSerializer(serializers.ModelSerializer):
    sub_service = SubServiceSerializer(many=True)
    class Meta:
        model = Service
        fields = ('id', 'title', 'description', 'thumbnail', 'min_price', 'sub_service')


class ServiceChoiceSerializer(serializers.ModelSerializer):
    sub_service = SubServiceSerializer()
    user = serializers.StringRelatedField(read_only=True)

    taskers = serializers.HyperlinkedRelatedField(
        view_name='tasker-detail',
        read_only=True,
        lookup_field='pk'
    )

    class Meta:
        model = ServiceBook
        fields = ('id', 'sub_service', 'user', 'created', 
                  'address', 'issue', 'attachment', 'taskers')


class OrderListSerializer(serializers.ModelSerializer):

    sub_service = serializers.HyperlinkedRelatedField(
        view_name='sub-service-detail',
        read_only=True,
        lookup_field='pk'
    )
    tasker = serializers.HyperlinkedRelatedField(
        view_name='tasker-detail',
        read_only=True,
        lookup_field='pk'
    )

    order_detail_url = serializers.HyperlinkedIdentityField(
        view_name='order-detail',
        lookup_field='pk'
    )


    class Meta:
        model = Order
        fields = ('id', 'order_detail_url', 'tasker', 
                  'sub_service', 'start_date', 'address', 
                  'price', 'status', 'created_at', 'task_photo')


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'customer', 'tasker', 'sub_service', 
                  'start_date', 'address', 'price', 'status', 
                  'created_at', 'task_photo', 'task_detail')


class OrderDetailSerializer(serializers.ModelSerializer):
    sub_service = serializers.HyperlinkedRelatedField(
        view_name='sub-service-detail',
        read_only=True,
        lookup_field='pk'
    )
    tasker = serializers.HyperlinkedRelatedField(
        view_name='tasker-detail',
        read_only=True,
        lookup_field='pk'
    )

    class Meta:
        model = Order
        fields = ('id', 'customer', 'tasker', 'sub_service', 
                  'start_date', 'address', 'price', 'created_at', 
                  'status', 'task_photo', 'task_detail', 'price')
