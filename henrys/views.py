from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from henrys.serializers import *


class RentalsListView(ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class ReservationsListView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

@api_view(['GET'])
def getLatestReservations(request):
    reservationsOrdered = Reservation.objects.all().order_by('rental','checkin')

    rows=[]

    previous_reservation=None
    for reservation in reservationsOrdered:
        d = {}
        d['rental_name']=reservation.rental.name
        d['reservation_id']= reservation.id
        d['reservation_checkin']=reservation.checkin
        d['reservation_checkout']=reservation.checkout

        ## same rental
        if previous_reservation and previous_reservation.rental == reservation.rental:
                d['prev_reservation']=previous_reservation.id
        ## new rental start
        else:
            d['prev_reservation']='NA'

        previous_reservation = reservation

        rows.append(d)

    return Response({'data':rows})





