"""
URL configuration for StudentV4BE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from student import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.get_student),
    path('students/query/', views.query_student),
    path('sno/check/', views.is_exsits_sno),
    path('students/add/', views.add_student),
    path('students/update/', views.update_student),
    path('students/delete/', views.delete_student),
    path('students/deletes/', views.delete_students),
    path('upload/', views.upload)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)