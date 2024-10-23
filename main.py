from abc import ABC, abstractmethod

class Customer:
    def __init__(self, customer_id, name, age, address):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.address = address
        self.polices = []

    def add_policy(self, policy):
        self.polices.append(policy)

class Policy(ABC):
    def __init__(self, policy_type, base_premium):
        self.policy_type = policy_type
        self.base_premium = base_premium

    @abstractmethod
    def calculate_premium(self, customer):
        pass

class HealthPolicy(Policy):
    def __init__(self, base_premium, medical_conditions):
        super().__init__("Health", base_premium)
        self.medical_conditions = medical_conditions

    def calculate_premium(self, customer):
        premium = self.base_premium + (customer.age * 10)
        if self.medical_conditions:
            premium += 100  
        return premium
    
class AutoPolicy(Policy):
    def __init__(self, base_premium, driving_record):
        super().__init__('Auto', base_premium)
        self.driving_record = driving_record

    def calculate_premium(self, customer):
        premium = self.base_premium + (customer.age * 5)
        if self.driving_record == 'bad':
            premium += 200
        return premium
    
class LifePolicy(Policy):
    def __init__(self, base_premium, coverage_amount):
        super().__init__('Life', base_premium)
        self.coverage_amount = coverage_amount

    def calculate_premium(self, customer):
        premium = self.base_premium + (self.coverage_amount * 0.01) + (customer.age * 2)
        return premium
    
#test case
customer1 = Customer(1, 'Aleyna', 24, 'Maltepe')
health_policy = HealthPolicy(base_premium=500, medical_conditions=True)
auto_policy = AutoPolicy(base_premium=300, driving_record='good')
life_policy = LifePolicy(base_premium=200, coverage_amount=100000)

customer1.add_policy(health_policy)
customer1.add_policy(auto_policy)
customer1.add_policy(life_policy)

print(f"Health policy premium: {health_policy.calculate_premium(customer1)}")
print(f"Auto policy premium: {auto_policy.calculate_premium(customer1)}")
print(f"Life policy premium: {life_policy.calculate_premium(customer1)}")
        
