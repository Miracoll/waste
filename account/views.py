from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Waste
from .serializers import BinSerializer, WasteSerializer

# Create your views here.

def home(request):
    context = {}
    return render(request, 'account/index.html', context)

def waste(request):
    user = request.user
    wastes = Waste.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        if Waste.objects.filter(name=name).exists():
            messages.error(request, f'{name} already exist')
            return redirect('waste')
        Waste.objects.create(name=name,location=location,user=user)
        messages.success(request, 'Waste create successfully')
        return redirect('waste')
    context = {
        'wastes':wastes,
    }
    return render(request, 'account/waste.html', context)

def settings(request):
    context={}
    return render(request, 'account/settings.html', context)

def profile(request):
    context={}
    return render(request, 'account/profile.html', context)

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Unauthorised access')
            return redirect('login')
    return render(request, 'account/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

class BinDetail(APIView):
    
    def get(self, request, ref):
        try:
            bin = Waste.objects.get(ref=ref)
        except Waste.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BinSerializer(bin)
        return Response(serializer.data)

class WasteList(APIView):
    def get(self, request):
        try:
            control = Waste.objects.all()
        except Waste.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BinSerializer(control, many=True)
        return Response(serializer.data)
    
class ConfigDetail(APIView):
    def get(self, request, ref):
        try:
            waste = Waste.objects.get(ref=ref)
        except Waste.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WasteSerializer(waste)
        return Response(serializer.data)
    
    def put(self, request, ref):
        config = Waste.objects.get(ref=ref)
        serializer = WasteSerializer(config, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class ConfigResponse(APIView):
#     def put(self, request, ref):
#         # try:
#         config = Config.objects.get(id=ref)
#         config.connection_status = True
#         config.save()
#         # except Config.DoesNotExist:
#         #     return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ConfigSerializer(config)
#         return Response(serializer.data)