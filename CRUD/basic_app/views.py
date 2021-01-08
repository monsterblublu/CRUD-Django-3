from django.shortcuts import render
from basic_app.models import Mahasiswa
from django.urls import reverse_lazy,reverse

from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView,
                                    RedirectView)


# Create your views here.
class MahasiswaIndexView(RedirectView):
    url = '/mahasiswa/'
    
class MahasiswaListView(ListView):
    
    model = Mahasiswa

class MahasiswaDetailView(DetailView):
    context_object_name = 'mahasiswa_detail'
    model = Mahasiswa

class CreateMahasiswaView(CreateView):
    fields = '__all__'
    model = Mahasiswa

class MahasiswaUpdateView(UpdateView):
    fields = ('name','nisn','nis','address','phone','profile_pic','quote_me')
    model = Mahasiswa

class MahasiswaDeleteView(DeleteView):
    context_object_name = 'mahasiswa'
    model = Mahasiswa
    success_url = reverse_lazy('mahasiswa_list')