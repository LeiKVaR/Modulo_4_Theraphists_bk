
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from therapists.models import Therapist

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def therapist_data():
    return {
        "first_name": "Ana",
        "last_name_paternal": "Gómez",
        "last_name_maternal": "López",
        "document_number": "87654321",
        "document_type": "DNI",
        "birth_date": "1990-05-15",
        "gender": "Femenino",
        "email": "ana@example.com",
        "phone": "987654321",
        "country": "Perú",
        "address": "Av. Siempre Viva 123",
        "department": "Lima",
        "province": "Lima",
        "district": "Miraflores",
        "personal_reference": None,    # <-- Agregado
        "profile_picture": None,       # <-- Agregado
    }

@pytest.fixture
def therapist(db, therapist_data):
    return Therapist.objects.create(**therapist_data)

@pytest.mark.django_db
def test_list_therapists(api_client, therapist):
    url = reverse('therapist-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert any(t['id'] == therapist.id for t in response.data)

@pytest.mark.django_db
def test_create_therapist(api_client, therapist_data):
    url = reverse('therapist-list')
    # Elimina dinámicamente los campos con valor None
    data = {k: v for k, v in therapist_data.items() if v is not None}
    response = api_client.post(url, data)
    print("RESPONSE DATA:", response.data)
    assert response.status_code == 201
    assert Therapist.objects.filter(email="ana@example.com").exists()
    
@pytest.mark.django_db
def test_soft_delete_therapist(api_client, therapist):
    url = reverse('therapist-detail', args=[therapist.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    therapist.refresh_from_db()
    assert therapist.is_active is False

@pytest.mark.django_db
def test_restore_therapist(api_client, therapist):
    therapist.is_active = False
    therapist.save()
    url = reverse('therapist-restore', args=[therapist.id])
    response = api_client.post(url)
    assert response.status_code == 200
    therapist.refresh_from_db()
    assert therapist.is_active is True

@pytest.mark.django_db
def test_inactive_therapists(api_client, therapist):
    therapist.is_active = False
    therapist.save()
    url = reverse('therapist-inactive')
    response = api_client.get(url)
    assert response.status_code == 200
    assert any(t['id'] == therapist.id for t in response.data)

@pytest.mark.django_db
def test_filter_active_therapists(api_client, therapist):
    url = reverse('therapist-list')
    response = api_client.get(url, {'active': 'true'})
    assert response.status_code == 200
    assert any(t['id'] == therapist.id for t in response.data)

@pytest.mark.django_db
def test_filter_inactive_therapists(api_client, therapist):
    therapist.is_active = False
    therapist.save()
    url = reverse('therapist-list')
    response = api_client.get(url, {'active': 'false'})
    assert response.status_code == 200
    assert any(t['id'] == therapist.id for t in response.data)