from rest_framework.test import (
    APITestCase,
    APIRequestFactory,
    force_authenticate,
)  # using APITestCase for testing
from flights.views import FlightView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from flights.models import Flight


class FlightViewTestCase(APITestCase):
    def create_flight(self):
        flight = Flight.objects.create(
            flight_number="DE04",
            operation_airlines="ryanair",
            departure_city="koblenz",
            arrival_city="prag",
            date_of_departure="2024-12-30",
            etd="19:00:00",
        )
        return flight

    def setUp(self):
        self.factory = APIRequestFactory()
        self.flight = self.create_flight()
        self.user = User.objects.create_user(
            username="admin", email="a@a.com", password="654321aA*"
        )
        if not Token.objects.filter(user=self.user).exists():
            self.token = Token.objects.create(user=self.user)
        else:
            self.token = Token.objects.get(user=self.user)

    def test_list_as_non_user(self):
        request = self.factory.get("flights/flight")
        response = FlightView.as_view({"get": "list"})(request)
        self.assertEquals(response.status_code, 200)

    def test_list_as_auth_user(self):
        request = self.factory.get(
            "flights/flight", HTTP_AUTHORIZATION="Token {}".format(self.token)
        )
        request.user = self.user
        request.user.is_staff = True
        self.user.save()
        response = FlightView.as_view({"get": "list"})(request)
        self.assertEquals(response.status_code, 200)

    def test_list_as_non_auth_user(self):
        request = self.factory.get(
            "flights/flight", HTTP_AUTHORIZATION="Token {}".format(self.token)
        )
        request.user = self.user
        # request.user.is_staff = True
        self.user.save()
        response = FlightView.as_view({"get": "list"})(request)
        self.assertEquals(response.status_code, 200)

    def test_create_as_admin_user(self):
        data = {
            "flight_number": "DE04",
            "operation_airlines": "ryanair",
            "departure_city": "koblenz",
            "arrival_city": "prag",
            "date_of_departure": "2024-12-30",
            "etd": "19:00:00",
        }
        # data = self.flight
        self.user.is_staff = True
        self.user.save()
        request = self.factory.post(
            "flights/flight", data, HTTP_AUTHORIZATION="Token {}".format(self.token)
        )
        response = FlightView.as_view({"post": "create"})(request)
        self.assertEquals(response.status_code, 201)

    def test_create_flight_as_non_user(self):
        request = self.factory.post("flights/flight")
        response = FlightView.as_view({"post": "create"})(request)
        self.assertEquals(response.status_code, 401)

    def test_create_flight_as_non_staff(self):
        request = self.factory.post(
            "flights/flight", HTTP_AUTHORIZATION="Token {}".format(self.token)
        )
        response = FlightView.as_view({"post": "create"})(request)
        self.assertEquals(response.status_code, 403)

    def test_flight_model_str_method(self):
        self.assertEquals(
            str(self.flight),
            f"{self.flight.flight_number} - {self.flight.departure_city} - {self.flight.arrival_city}",
        )

    def test_delete_as_admin_user(self):
        self.user.is_staff = True
        self.user.save()
        request = self.factory.delete(
            "flights/flight/1/", HTTP_AUTHORIZATION="Token {}".format(self.token)
        )
        force_authenticate(request, user=self.user)
        response = FlightView.as_view({"delete": "destroy"})(request, pk="1")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Flight.objects.count(), 0)
