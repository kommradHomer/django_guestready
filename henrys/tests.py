from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

class RentalTest(TestCase):
    fixtures = ['fixtures/sample-data.json']

    def setUp(self):
        # Load fixtures
        for fixture in self.fixtures:
            call_command('loaddata', fixture, verbosity=0)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/rentalApp/testTask')
        self.assertEqual(response.status_code, 200)


    def test_rental_list(self):
        response = self.client.get(reverse('testTask'))
        self.assertEqual(response.status_code, 200)

        respData=response.data['data']
        for d in respData:
            print('|'.join(([str(v) for k,v in d.items()])))

        for i,row in enumerate(respData):
            if row['prev_reservation'] != 'NA':
                self.assertEqual(row['prev_reservation'],respData[i-1]['reservation_id'])

