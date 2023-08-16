from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking
from .serializers import bookingSerializer,menuSerializer
from .forms import ApplicationForm
# Create your views here.

def form(request):
    forms = ApplicationForm()
    return render(request,'forms.html',{'form':forms})
def bootstapPage(request):
    return render(request,'bootstrap tutorial.html',{})
def index(request):
    return render(request, 'index.html',{})

class bookingview(APIView):
    def get(self,request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items,many=True)
        return Response(serializer.data) #returs json
class menuview(APIView):
    def post(self,request):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})