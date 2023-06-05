from django.shortcuts import render
from .serializers import FlightSeralizer, ReservationSerializer, StaffFlightSerializer
from .models import Flight, Reservation
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly
from datetime import datetime, date

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSeralizer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()
        
        if self.request.user.is_staff:
            return queryset
        else:
            queryset = Flight.objects.filter(date_of_departure__gt=today)
            if Flight.objects.filter(date_of_departure=today):
                today_qs = Flight.objects.filter(date_of_departure=today).filter(etd__gt=current_time)
                queryset = queryset.union(today_qs)
                
            return queryset
        
    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer
        return serializer_class
    

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)
    


