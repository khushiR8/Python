import datetime

class Vehicle:
    def __init__(self, model, year, color, daily_rate, is_rented=False):
        self.model = model
        self.year = year
        self.color = color
        self.daily_rate = daily_rate
        self.is_rented = is_rented
    
    def __str__(self):
        return f"{self.model} ({self.year}) - {self.color} - Rs{self.daily_rate}/day - {'Rented' if self.is_rented else 'Available'}"

class Car(Vehicle):
    def __init__(self, model, year, color, daily_rate, is_rented=False):
        super().__init__(model, year, color, daily_rate, is_rented)

class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def __str__(self):
        return f"{self.name} - {self.number}"

class Customer(Person):
    def __init__(self, name, number, rented_car=None):
        super().__init__(name, number)
        self.rented_car = rented_car
    
    def __str__(self):
        return f"{self.name} - {self.number} - {'Rented: ' + str(self.rented_car) if self.rented_car else 'No Car'}"

class CarRentalApp:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.load_data()
    
    def load_data(self):
        try:
            with open("cars.txt", "r") as f:
                for line in f:
                    model, year, color, daily_rate, rented = line.strip().split(",")
                    self.cars.append(Car(model, int(year), color, float(daily_rate), rented == "True"))
        except FileNotFoundError:
            pass
        
        try:
            with open("customers.txt", "r") as f:
                for line in f:
                    name, number = line.strip().split(",")
                    self.customers.append(Customer(name, number))
        except FileNotFoundError:
            pass
    
    def save_data(self):
        with open("cars.txt", "w") as f:
            for car in self.cars:
                f.write(f"{car.model},{car.year},{car.color},{car.daily_rate},{car.is_rented}\n")
        
        with open("customers.txt", "w") as f:
            for customer in self.customers:
                f.write(f"{customer.name},{customer.number}\n")
    
    def add_car(self):
        model = input("Enter the car model: ")
        year = int(input("Enter the car year: "))
        color = input("Enter the car color: ")
        daily_rate = float(input("Enter daily rental price: "))
        self.cars.append(Car(model, year, color, daily_rate))
        print("Car added successfully!")
    
    def remove_car(self):
        self.list_cars()
        car_index = int(input("Enter the index of the car to remove: "))
        if 0 <= car_index < len(self.cars):
            car = self.cars.pop(car_index)
            print(f"Car {car.model} removed successfully!")
        else:
            print("Invalid car index.")
    
    def add_customer(self):
        name = input("Enter customer name: ")
        number = input("Enter customer number: ")
        self.customers.append(Customer(name, number))
        print("Customer added successfully!")
    
    def rent_car(self):
        self.list_cars()
        car_index = int(input("Enter the index of the car to rent: "))
        if 0 <= car_index < len(self.cars):
            car = self.cars[car_index]
            if not car.is_rented:
                customer_name = input("Enter your name: ")
                customer = next((c for c in self.customers if c.name == customer_name), None)
                if customer:
                    days = int(input("Enter number of days to rent: "))
                    total_cost = days * car.daily_rate
                    rental_date = datetime.date.today()
                    car.is_rented = True
                    customer.rented_car = car
                    print(f"{customer_name} has rented {car.model} for {days} days. Total cost: Rs{total_cost}")
                    with open("rental_history.txt", "a") as f:
                        f.write(f"{customer.name},{car.model},{car.year},{rental_date},-,{days},Rs{total_cost}\n")
                else:
                    print("Customer not found.")
            else:
                print("Car is already rented.")
        else:
            print("Invalid car index.")
    
    def return_car(self):
        customer_name = input("Enter your name: ")
        customer = next((c for c in self.customers if c.name == customer_name), None)
        if customer and customer.rented_car:
            car = customer.rented_car
            return_date = datetime.date.today()
            car.is_rented = False
            print(f"{customer_name} has returned {car.model}.")
            customer.rented_car = None
            with open("rental_history.txt", "r") as f:
                lines = f.readlines()
            with open("rental_history.txt", "w") as f:
                for line in lines:
                    if f"{customer_name},{car.model},{car.year},-" in line:
                        f.write(line.replace("-,", f"{return_date},"))
                    else:
                        f.write(line)
        else:
            print("No car to return or customer not found.")
    
    def view_rental_history(self):
        try:
            with open("rental_history.txt", "r") as f:
                print("Rental History:")
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("No rental history found.")
    
    def list_cars(self):
        print("Available Cars:")
        for i, car in enumerate(self.cars):
            print(f"{i}. {car}")
    
    def list_customers(self):
        print("Customers:")
        for customer in self.customers:
            print(customer)
    
    def main_menu(self):
        while True:
            print("\nCar Rental System")
            print("1. Add Car")
            print("2. Remove Car")
            print("3. List Cars")
            print("4. Add Customer")
            print("5. List Customers")
            print("6. Rent Car")
            print("7. Return Car")
            print("8. View Rental History")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_car()
            elif choice == "2":
                self.remove_car()
            elif choice == "3":
                self.list_cars()
            elif choice == "4":
                self.add_customer()
            elif choice == "5":
                self.list_customers()
            elif choice == "6":
                self.rent_car()
            elif choice == "7":
                self.return_car()
            elif choice == "8":
                self.view_rental_history()
            elif choice == "9":
                print("Exiting...")
                self.save_data()
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = CarRentalApp()
    app.main_menu()
