import datetime

class Vehicle:
    def __init__(self, model, year, color, daily_rate, is_rented=False):
        self._model = model
        self._year = year
        self._color = color
        self._daily_rate = daily_rate
        self._is_rented = is_rented
    
    # Getter and Setter for model
    def get_model(self):
        return self._model
    
    def set_model(self, model):
        self._model = model
    
    # Getter and Setter for year
    def get_year(self):
        return self._year
    
    def set_year(self, year):
        self._year = year
    
    # Getter and Setter for color
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color
    
    # Getter and Setter for daily_rate
    def get_daily_rate(self):
        return self._daily_rate
    
    def set_daily_rate(self, daily_rate):
        self._daily_rate = daily_rate
    
    # Getter and Setter for is_rented
    def get_is_rented(self):
        return self._is_rented
    
    def set_is_rented(self, is_rented):
        self._is_rented = is_rented
    
    def __str__(self):
        return f"{self._model} ({self._year}) - {self._color} - Rs{self._daily_rate}/day - {'Rented' if self._is_rented else 'Available'}"

class Car(Vehicle):
    def __init__(self, model, year, color, daily_rate, is_rented=False):
        super().__init__(model, year, color, daily_rate, is_rented)

class Person:
    def __init__(self, name, number):
        self._name = name
        self._number = number
    
    # Getter and Setter for name
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    # Getter and Setter for number
    def get_number(self):
        return self._number
    
    def set_number(self, number):
        self._number = number
    
    def __str__(self):
        return f"{self._name} - {self._number}"

class Customer(Person):
    def __init__(self, name, number, rented_car=None):
        super().__init__(name, number)
        self._rented_car = rented_car
    
    # Getter and Setter for rented_car
    def get_rented_car(self):
        return self._rented_car
    
    def set_rented_car(self, rented_car):
        self._rented_car = rented_car
    
    def __str__(self):
        return f"{self._name} - {self._number} - {'Rented: ' + str(self._rented_car) if self._rented_car else 'No Car'}"

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
                f.write(f"{car.get_model()},{car.get_year()},{car.get_color()},{car.get_daily_rate()},{car.get_is_rented()}\n")
        
        with open("customers.txt", "w") as f:
            for customer in self.customers:
                f.write(f"{customer.get_name()},{customer.get_number()}\n")
    
    def add_car(self):
        model = input("Enter the car model: ").strip()
        if not model or any(char.isdigit() for char in model):
            print("Error: Car model cannot be empty or contain digits.")
            return
        
        try:
            year = int(input("Enter the car year (numbers only): "))
        except ValueError:
            print("Error: Car year must be an integer.")
            return
        
        color = input("Enter the car color: ").strip()
        if not color or any(char.isdigit() for char in color):
            print("Error: Car color cannot be empty or contain digits.")
            return
        
        try:
            daily_rate = float(input("Enter daily rental price (numbers only): "))
        except ValueError:
            print("Error: Daily rental price must be a valid number.")
            return
        
        self.cars.append(Car(model, year, color, daily_rate))
        print("Car added successfully!")
    
    def remove_car(self):
        self.list_cars()
        try:
            car_index = int(input("Enter the index of the car to remove: "))
        except ValueError:
            print("Error: Please enter a valid integer index.")
            return
        
        if 0 <= car_index < len(self.cars):
            car = self.cars.pop(car_index)
            print(f"Car {car.get_model()} removed successfully!")
        else:
            print("Invalid car index.")
    
    def add_customer(self):
        name = input("Enter customer name: ").strip()
        if not name or any(char.isdigit() for char in name):
            print("Error: Customer name cannot be empty or contain digits.")
            return
        
        number = input("Enter customer number: ")
        
        self.customers.append(Customer(name, number))
        print("Customer added successfully!")
    
    def remove_customer(self):
        self.list_customers()
        customer_name = input("Enter the name of the customer to remove: ").strip()
        if not customer_name or any(char.isdigit() for char in customer_name):
            print("Error: Customer name cannot be empty or contain digits.")
            return
        
        customer = next((c for c in self.customers if c.get_name() == customer_name), None)
        if customer:
            self.customers.remove(customer)
            print(f"Customer {customer.get_name()} removed successfully!")
        else:
            print("Customer not found.")
    
    def rent_car(self):
        self.list_cars()
        try:
            car_index = int(input("Enter the index of the car to rent: "))
        except ValueError:
            print("Error: Please enter a valid integer index.")
            return
        
        if 0 <= car_index < len(self.cars):
            car = self.cars[car_index]
            if not car.get_is_rented():
                customer_name = input("Enter your name: ").strip()
                customer = next((c for c in self.customers if c.get_name() == customer_name), None)
                if customer:
                    try:
                        days = int(input("Enter number of days to rent (numbers only): "))
                    except ValueError:
                        print("Error: Number of days must be an integer.")
                        return
                    
                    total_cost = days * car.get_daily_rate()
                    rental_date = datetime.date.today()
                    car.set_is_rented(True)
                    customer.set_rented_car(car)
                    print(f"{customer_name} has rented {car.get_model()} for {days} days. Total cost: Rs{total_cost}")
                    
                    with open("rental_history.txt", "a") as f:
                        f.write(f"{customer.get_name()},{car.get_model()},{car.get_year()},{rental_date},-,{days},Rs{total_cost}\n")
                else:
                    print("Customer not found. Please add the customer first.")
            else:
                print("Car is already rented.")
        else:
            print("Invalid car index.")
    
    def return_car(self):
        customer_name = input("Enter your name: ")
        customer = next((c for c in self.customers if c.get_name() == customer_name), None)
        if customer and customer.get_rented_car():
            car = customer.get_rented_car()
            return_date = datetime.date.today()
            car.set_is_rented(False)
            print(f"{customer_name} has returned {car.get_model()}.")
            customer.set_rented_car(None)
            
            with open("rental_history.txt", "r") as f:
                lines = f.readlines()
            with open("rental_history.txt", "w") as f:
                for line in lines:
                    if f"{customer_name},{car.get_model()},{car.get_year()},-" in line:
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
            print("5. Remove Customer")
            print("6. List Customers")
            print("7. Rent Car")
            print("8. Return Car")
            print("9. View Rental History")
            print("10. Exit")

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
                self.remove_customer()
            elif choice == "6":
                self.list_customers()
            elif choice == "7":
                self.rent_car()
            elif choice == "8":
                self.return_car()
            elif choice == "9":
                self.view_rental_history()
            elif choice == "10":
                print("Exiting...")
                self.save_data()
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = CarRentalApp()
    app.main_menu()
