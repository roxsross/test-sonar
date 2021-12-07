"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index),
    # path('car', views.add_car),
    # path('<str:car_name>', views.get_car),

    # path('', views.apiOverview, name="api-overview"),
	# path('task-list/', views.taskList, name="task-list"),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	# path('task-create/', views.taskCreate, name="task-create"),

	# path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	# path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),

    path('', views.apiOverview, name="api-overview"),
	path('product-list/', views.productList, name="product-list"),
	path('product-detail/<str:pk>/', views.productDetail, name="product-detail"),
	path('product-create/', views.productCreate, name="product-create"),

	path('product-update/<str:pk>/', views.productUpdate, name="product-update"),
	path('product-delete/<str:pk>/', views.productDelete, name="product-delete"),

]
