from django.urls import path
from . import views

urlpatterns = [
	#Task URL
	# path('', views.apiOverview, name="api-overview"),
	# path('task-list/', views.taskList, name="task-list"),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	# path('task-create/', views.taskCreate, name="task-create"),

	# path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	# path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),

	#product URL
	path('product-list/', views.productList, name="product-list"),
	path('product-detail/<str:pk>/', views.productDetail, name="product-detail"),
	path('product-create/', views.productCreate, name="prodcut-create"),

	path('product-update/<str:pk>/', views.productUpdate, name="product-update"),
	path('product-delete/<str:pk>/', views.productDelete, name="product-delete"),
]
