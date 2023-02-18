from django.urls import path

from . import views

urlpatterns = [
    path('tasker/', views.TaskerView.as_view(), name='tasker'),
    path('tasker/<int:pk>/', views.TaskerDetailView.as_view(), name='tasker-detail'),

    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),

    path('service/', views.ServiceListView.as_view(), name='service'),
    path('service/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail'),

    path('sub-service/', views.SubServiceListView.as_view(), name='sub-service'),
    path('sub-service/<int:pk>', views.SubServiceDetailView.as_view(), name='sub-service-detail'),

    path('service-choices/', views.ServiceChoiceList.as_view(), name='service-choice'),
    path('service-choices/<int:pk>/', views.ServiceChoiceDetail.as_view(), name='service-choice-detail'),

    path('order/', views.OrderListCreateView.as_view(), name='order'),
    path('order/<int:pk>', views.OrderDetailUpdateView.as_view(), name='order-detail'),
]
