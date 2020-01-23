import pytest
from szkody.models import Klient
from django.urls import reverse

def test__add_klient(authorized_client):
    # This is the data we want to save in the model
    data_to_save = {
        'PESEL': '12345678',
        'imie': 'test',
        'nazwisko': 'test',
        'nrPrawaJazdy': 'test123',
        'created_by': 1
    }

    # Let's assume our endpoint looks like this:
    # POST localhost:8080/api/animals
    url = reverse('KlientList')

    # Time to send the data
    response = authorized_client.post(
        url,
        data_to_save,
        content_type='application/json',
    )

    # Let's check if the request was successful
    assert response.status_code == 200

    # Does the response json match what we posted?
    assert response.json() == data_to_save

    # Let's see if the object was added
    all_klient = Klient.objects.all()
    assert all_klient.count() == 1

    # Check, if the object is exactly like the one we wanted to save
    saved_klient = all_klient.first()
    assert saved_klient.PESEL == '12345678'
    assert saved_klient.imie == 'test'
    assert saved_klient.nazwisko == 'test'
    assert saved_klient.nrPrawaJazdy == 'test123'
    assert saved_klient.created_by == 1
