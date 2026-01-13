import pytest
from backend.app import create_app
from backend.config import Config


@pytest.fixture
def client():
    """Create a test client for the application"""
    app = create_app(Config)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    """Test the home page route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Multi-Converter' in response.data


def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'message' in data


def test_api_info_endpoint(client):
    """Test the API info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data['name'] == 'Multi-Converter Application'
    assert data['version'] == '1.0.0'
    assert 'features' in data
    assert len(data['features']) > 0


def test_get_units_endpoint(client):
    """Test the get units endpoint"""
    response = client.get('/api/units')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert 'length' in data
    assert 'weight' in data
    assert 'temperature' in data
    assert 'volume' in data
    assert 'currency' in data
    assert 'number_base' in data


def test_convert_length_success(client):
    """Test length conversion"""
    response = client.post('/api/convert/length', json={
        'value': 100,
        'from_unit': 'meter',
        'to_unit': 'kilometer'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert 'result' in data
    assert data['result'] == 0.1


def test_convert_length_invalid_unit(client):
    """Test length conversion with invalid unit"""
    response = client.post('/api/convert/length', json={
        'value': 100,
        'from_unit': 'invalid',
        'to_unit': 'kilometer'
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
    assert 'error' in data


def test_convert_weight_success(client):
    """Test weight conversion"""
    response = client.post('/api/convert/weight', json={
        'value': 1000,
        'from_unit': 'gram',
        'to_unit': 'kilogram'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['result'] == 1.0


def test_convert_temperature_success(client):
    """Test temperature conversion"""
    response = client.post('/api/convert/temperature', json={
        'value': 0,
        'from_unit': 'celsius',
        'to_unit': 'fahrenheit'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['result'] == 32.0


def test_convert_volume_success(client):
    """Test volume conversion"""
    response = client.post('/api/convert/volume', json={
        'value': 1,
        'from_unit': 'liter',
        'to_unit': 'milliliter'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['result'] == 1000.0


def test_convert_currency_success(client):
    """Test currency conversion"""
    response = client.post('/api/convert/currency', json={
        'value': 100,
        'from_currency': 'USD',
        'to_currency': 'EUR'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert 'result' in data
    assert isinstance(data['result'], float)


def test_convert_number_base_success(client):
    """Test number base conversion"""
    response = client.post('/api/convert/number-base', json={
        'value': '10',
        'from_base': 'decimal',
        'to_base': 'binary'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['result'] == '1010'


def test_convert_number_base_hex(client):
    """Test hexadecimal conversion"""
    response = client.post('/api/convert/number-base', json={
        'value': 'FF',
        'from_base': 'hexadecimal',
        'to_base': 'decimal'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['result'] == '255'


def test_convert_missing_parameters(client):
    """Test conversion with missing parameters"""
    response = client.post('/api/convert/length', json={
        'value': 100
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False


def test_convert_invalid_value(client):
    """Test conversion with invalid value"""
    response = client.post('/api/convert/length', json={
        'value': 'invalid',
        'from_unit': 'meter',
        'to_unit': 'kilometer'
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data['success'] is False
