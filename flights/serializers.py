from rest_framework import serializers
from .models import Flight, Reservation, Passenger

class FlightSeralizer(serializers.ModelSerializer):
    
    class Meta:
        model= Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number"
        )  
        
class ReservationSerializer(serializers.ModelSerializer):

    flight = serializers.StringRelatedField()
    flight_id = serializers.IntegerField()
    
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False)
    passenger = PassengerSerializer(many=True)
    
    class Meta:
        model = Reservation
        fields = (
            "id",
            "flight",  # GET
            "flight_id",  # POST
            "user",  # GET
            "user_id",  # POST
            "passenger"
        )
        
    def create(self, validated_data):
        passenger = validated_data.pop("passenger")
        validated_data["user_id"] = self.context["request"].user.id
        reservation = Reservation.objects.create(**validated_data)
        
        for i in passenger:
            pas = Passenger.objects.create(**i)
            reservation.passenger.add(pas)
        
        reservation.save()
        return reservation
        
class StaffFlightSerializer(serializers.ModelSerializer):
    
    reservations = ReservationSerializer(many=True, read_only=True)
    
    class Meta:
        model= Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd",
            "reservations"
        )