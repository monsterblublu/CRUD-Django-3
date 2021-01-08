from django.urls import path
from basic_app import views
from django.conf import settings
from django.conf.urls.static import static

# ... your normal urlpatterns here



urlpatterns = [
    path('',views.MahasiswaIndexView.as_view(),name='mahasiswa_index'),
    path('mahasiswa/',views.MahasiswaListView.as_view(),name='mahasiswa_list'),
    path('mahasiswa/<int:pk>',views.MahasiswaDetailView.as_view(),name='mahasiswa_detail'),
    path('mahasiswa/new',views.CreateMahasiswaView.as_view(),name='mahasiswa_new'),
    path('mahasiswa/<int:pk>/edit',views.MahasiswaUpdateView.as_view(),name='mahasiswa_edit'),
    path('mahasiswa/<int:pk>/remove',views.MahasiswaDeleteView.as_view(),name='mahasiswa_remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)