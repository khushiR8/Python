import json
import os
from datetime import datetime, timedelta

# Base class for common functionality
class Entity:
    def __init__(self, entity_id):
        self.entity_id = entity_id

    def __del__(self):
        print(f"{self.__class__.__name__} with ID {self.entity_id} is being destroyed.")

# Car Class inheriting from Entity
class Car(Entity):
    def __init__(self, car_id, brand, model, year, car_type, status, rental_price_per_day, maintenance_schedule):
        super().__init__(car_id)  # Call the base class constructor
        self.brand = brand
        self.model = model
        self.year = year
        self.car_type = car_type
        self.status = status
        self.rental_price_per_day = rental_price_per_day
        self.maintenance_schedule = maintenance_schedule

    def rent_car(self):
        self.status = 'rented'

    def return_car(self):
        self.status = 'available'

    def maintenance_check(self):
        return self.maintenance_schedule <= datetime.now()

# Customer Class inheriting from Entity
class Customer(Entity):
    def __init__(self, customer_id, name, contact_info, drivers_license):
        super().__init__(customer_id)  # Call the base class constructor
        self.name = name
        self.contact_info = contact_info
        self.drivers_license = drivers_license
        self.rental_history = []
        self.loyalty_points = 0

    def add_rental(self, rental):
        self.rental_history.append(rental)

    def apply_loyalty_discount(self):
        return self.loyalty_points * 0.05  # 5% discount per loyalty point

# Rental Class inheriting from Entity
class Rental(Entity):
    def __init__(self, rental_id, customer_id, car_id, rental_start_date, rental_end_date, insurance=False, late_fee=0):
        super().__init__(rental_id)  # Call the base class constructor
        self.customer_id = customer_id
        self.car_id = car_id
        self.rental_start_date = rental_start_date
        self.rental_end_date = rental_end_date
        self.insurance = insurance
        self.late_fee = late_fee

    def calculate_total_cost(self, car_price_per_day):
        rental_duration = (self.rental_end_date - self.rental_start_date).days
        total_cost = rental_duration * car_price_per_day
        if self.insurance:
            total_cost += rental_duration * 5  # Add insurance cost
        total_cost += self.late_fee
        return total_cost

# CarRentalSystem Class
class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.rentals = []
        self.load_data()

    def load_data(self):
        # Load data from JSON files if they exist
        if os.path.exists('cars.json'):
            with open('cars.json', 'r') as f:
                self.cars = [Car(**car) for car in json.load(f)]
        if os.path.exists('customers.json'):
            with open('customers.json', 'r') as f:
                self.customers = [Customer(**customer) for customer in json.load(f)]
        if os.path.exists('rentals.json'):
            with open('rentals.json', 'r') as f:
                self.rentals = [Rental(**rental) for rental in json.load(f)]

    def save_data(self):
        # Save data to JSON files
        with open('cars.json', 'w') as f:
            json.dump([car.__dict__ for car in self.cars], f, default=str)
        with open('customers.json', 'w') as f:
            json.dump([customer.__dict__ for customer in self.customers], f, default=str)
        with open('rentals.json', 'w') as f:
            json.dump([rental.__dict__ for rental in self.rentals], f, default=str)

    def add_car(self, car):
        self.cars.append(car)
        self.save_data()

    def register_customer(self, customer):
        self.customers.append(customer)
        self.save_data()

    def rent_car(self, customer_id, car_id, rental_period_days, insurance=False):
        car = next((car for car in self.cars if car.entity_id == car_id), None)
        if not car or car.status != 'available':
            print("Car is not available for rent.")
            return None
        rental_start_date = datetime.now()
        rental_end_date = rental_start_date + timedelta(days=rental_period_days)
        rental = Rental(len(self.rentals) + 1, customer_id, car_id, rental_start_date, rental_end_date, insurance)
        car.rent_car()
        self.rentals.append(rental)
        customer = next((customer for customer in self.customers if customer.entity_id == customer_id), None)
        if customer:
            customer.add_rental(rental)
            self.save_data()
            return rental
        return None

    def return_car(self, rental_id):
        rental = next((rental for rental in self.rentals if rental.entity_id == rental_id), None)
        if rental:
            car = next((car for car in self.cars if car.entity_id == rental.car_id), None)
            if car:
                car.return_car()
                rental.late_fee = max(0, (datetime.now() - rental.rental_end_date).days) * 10  # $10 per day late fee
                total_cost = rental.calculate_total_cost(car.rental_price_per_day)
                print(f"Total cost for rental {rental_id}: ${total_cost}")
                self.save_data()

    def generate_rental_report(self):
        report = []
        for rental in self.rentals:
            customer = next((customer for customer in self.customers if customer.entity_id == rental.customer_id), None)
            car = next((car for car in self.cars if car.entity_id == rental.car_id), None)
            if customer and car:
                report.append({
                    "rental_id": rental.entity_id,
                    "customer_name": customer.name,
                    "car_model": car.model,
                    "rental_period": f"{rental.rental_start_date} to {rental.rental_end_date}",
                    "total_cost": rental.calculate_total_cost(car.rental_price_per_day)
                })
        return report

    def generate_financial_report(self):
        total_revenue = 0
        for rental in self.rentals:
            car = next((car for car in self.cars if car.entity_id == rental.car_id), None)
            if car:
                total_revenue += rental.calculate_total_cost(car.rental_price_per_day)
        return total_revenue

# Test the system
if __name__ == "__main__":
    system = CarRentalSystem()

    # Add some cars to the system
    car1 = Car(1, 'Toyota', 'Camry', 2020, 'economy', 'available', 30, datetime(2025, 1, 15))
    car2 = Car(2, 'BMW', 'X5', 2022, 'luxury', 'available', 100, datetime(2025, 2, 20))
    system.add_car(car1)
    system.add_car(car2)

    # Register a customer
    customer = Customer(1, 'John Doe', '123-456-7890', 'D1234567')
    system.register_customer(customer)

    # Rent a car
    rental = system.rent_car(1, 1, 5, insurance=True)

    # Return the car and calculate cost
    system.return_car(rental.entity_id)

    # Generate reports
    rental_report = system.generate_rental_report()
    print("Rental Report:", rental_report)

    financial_report = system.generate_financial_report()
    print("Total Revenue:", financial_report)