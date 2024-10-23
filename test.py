import pytest
from main import Customer, HealthPolicy, AutoPolicy, LifePolicy

@pytest.fixture
def customer_data():
    return Customer(1, 'Aleyna', 24, 'Maltepe')

@pytest.fixture
def policies():
    health_policy = HealthPolicy(base_premium=500, medical_conditions=True)
    auto_policy = AutoPolicy(base_premium=300, driving_record='good')
    life_policy = LifePolicy(base_premium=200, coverage_amount=100000)
    return [health_policy, auto_policy, life_policy]

def test_health_policy(customer_data):
    health_policy = HealthPolicy(base_premium=500, medical_conditions=True)
    expected_premium = 500 + (customer_data.age * 10) + 100
    assert health_policy.calculate_premium(customer_data) == expected_premium

def test_auto_policy(customer_data):
    auto_policy = AutoPolicy(base_premium=300, driving_record='good')
    expected_premium = 300 + (customer_data.age * 5)
    assert auto_policy.calculate_premium(customer_data) == expected_premium

def test_life_policy(customer_data):
    life_policy = LifePolicy(base_premium=200, coverage_amount=100000)
    expected_premium = 200 + (100000 * 0.01) + (customer_data.age * 2)
    assert life_policy.calculate_premium(customer_data) == expected_premium

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])

