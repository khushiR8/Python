import datetime

# Global lists to store cars, customers, and rentals
cars = []
customers = []
rentals = []

class Vehicle:
    # Class variable to count the number of vehicles
    vehicle_count = 0

    def __init__(self, model, year, color, daily_rate, is_rented=False):
        self._model = model
        self._year = year
        self._color = color
        self._daily_rate = daily_rate
        self._is_rented = is_rented
        Vehicle.vehicle_count += 1  # Increment vehicle count

    # Getter and Setter for model
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    # Getter and Setter for year
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        current_year = datetime.datetime.now().year
        if year > current_year:
            print(f"Error: Year cannot be in the future. Current year is {current_year}.")
            return  # Simply return without setting the value
        self._year = year

    # Getter and Setter for color
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    # Getter and Setter for daily_rate
    @property
    def daily_rate(self):
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, daily_rate):
        self._daily_rate = daily_rate

    # Getter and Setter for is_rented
    @property
    def is_rented(self):
        return self._is_rented

    @is_rented.setter
    def is_rented(self, is_rented):
        self._is_rented = is_rented

    def __str__(self):
        return f"{self._model} ({self._year}) - {self._color} - Rs{self._daily_rate}/day - {'Rented' if self._is_rented else 'Available'}"


class Car(Vehicle):
    def __init__(self, car_id, model, year, color, daily_rate, is_rented=False):
        super().__init__(model, year, color, daily_rate, is_rented)
        self._car_id = car_id

    # Getter and Setter for car_id
    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, car_id):
        self._car_id = car_id

    def __str__(self):
        return f"ID: {self._car_id} - {self._model} ({self._year}) - {self._color} - Rs{self._daily_rate}/day - {'Rented' if self._is_rented else 'Available'}"


class Person:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    # Getter and Setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # Getter and Setter for number
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    def __str__(self):
        return f"{self._name} - {self._number}"


class Customer(Person):
    def __init__(self, name, number, customer_id, rented_car=None):
        super().__init__(name, number)
        self._customer_id = customer_id
        self._rented_car = rented_car

    # Getter and Setter for customer_id
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id

    # Getter and Setter for rented_car
    @property
    def rented_car(self):
        return self._rented_car

    @rented_car.setter
    def rented_car(self, rented_car):
        self._rented_car = rented_car

    def __str__(self):
        return f"ID: {self._customer_id} - {self._name} - {self._number} - {'Rented: ' + str(self._rented_car) if self._rented_car else 'No Car'}"


class Rental:
    def __init__(self, customer, car, rental_date, return_date, total_cost):
        self._customer = customer
        self._car = car
        self._rental_date = rental_date
        self._return_date = return_date
        self._total_cost = total_cost

    # Getter and Setter for customer
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        self._customer = customer

    # Getter and Setter for car
    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, car):
        self._car = car

    # Getter and Setter for rental_date
    @property
    def rental_date(self):
        return self._rental_date

    @rental_date.setter
    def rental_date(self, rental_date):
        self._rental_date = rental_date

    # Getter and Setter for return_date
    @property
    def return_date(self):
        return self._return_date

    @return_date.setter
    def return_date(self, return_date):
        self._return_date = return_date

    # Getter and Setter for total_cost
    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        self._total_cost = total_cost

    def __str__(self):
        return f"{self._customer.name} rented {self._car.model} on {self._rental_date.strftime('%d/%m/%Y')} and returned on {self._return_date.strftime('%d/%m/%Y')}. Total Cost: Rs{self._total_cost}"


class CarRentalSystem:
    def load_data():
        global cars, customers
        try:
            with open("cars.txt", "r") as f:
                for line in f:
                    car_id, model, year, color, daily_rate, rented = line.strip().split(",")
                    cars.append(Car(car_id, model, int(year), color, float(daily_rate), rented == "True"))
        except FileNotFoundError:
            pass
            #print("Error: cars.txt file not found.")
        
        try:
            with open("customers.txt", "r") as f:
                for line in f:
                    name, number, customer_id = line.strip().split(",")
                    customers.append(Customer(name, number, customer_id))
        except FileNotFoundError:
            pass
           
    def save_data():
        with open("cars.txt", "w") as f:
            for car in cars:
                f.write(f"{car.car_id},{car.model},{car.year},{car.color},{car.daily_rate},{car.is_rented}\n")

        with open("customers.txt", "w") as f:
            for customer in customers:
                f.write(f"{customer.name},{customer.number},{customer.customer_id}\n")

    def add_car():
        print()
        while True:
            car_id = input("Enter car ID: ").strip()
            if len(car_id) == 4 and car_id[0] == "V" and car_id[1:].isdigit():
                if not any(c.car_id == car_id for c in cars):
                    break
                print("Error: Car ID already exists.")
            else:
                print("Error: Car ID must be in the format V followed by 3 digits (e.g., V001).")

        model = input("Enter the car model: ").strip()

        while True:
            try:
                year = int(input("Enter the car year: "))
                current_year = datetime.datetime.now().year
                if year <= current_year:
                    break
                print(f"Error: Year cannot be in the future. Current year is {current_year}.")
            except ValueError:
                print("Error: Car year must be an integer.")

        while True:
            color = input("Enter the car color: ").strip()
            if color and not any(char.isdigit() for char in color):
                break
            print("Error: Car color cannot be empty or contain digits.")

        while True:
            try:
                daily_rate = float(input("Enter daily rental price: "))
                break
            except ValueError:
                print("Error: Daily rental price must be a valid number.")

        cars.append(Car(car_id, model, year, color, daily_rate))
        print("Car added successfully!")

    def remove_car():
        print()

        # Check if the list of cars is empty
        if not cars:
            print("The list of cars is empty.")
            return

        CarRentalSystem.list_cars()

        # Loop until the car ID is valid
        while True:
            car_id = input("Enter the car ID of the car to remove : ").strip()

            # Validate car ID format
            if len(car_id) == 4 and car_id[0] == "V" and car_id[1:].isdigit():
                break  # Exit loop if input is valid
            else:
                print("Error: Car ID must be in the format V followed by 3 digits (e.g., V001). Please try again.")

        # Search for the car
        car = next((c for c in cars if c.car_id == car_id), None)
        if car:
            cars.remove(car)
            print(f"Car {car.model} removed successfully!")
        else:
            print("Car not found.")

    def add_customer():
        print()
        while True:
            customer_id = input("Enter customer ID: ").strip()
            if len(customer_id) == 4 and customer_id[0] == "C" and customer_id[1:].isdigit():
                if not any(c.customer_id == customer_id for c in customers):
                    break
                print("Error: Customer ID already exists.")
            else:
                print("Error: Customer ID must be in the format C followed by 3 digits (e.g., C001).")

        while True:
            name = input("Enter customer name: ").strip()
            if name and not any(char.isdigit() for char in name):
                break
            print("Error: Customer name cannot be empty or contain digits.")

        while True:
            number = input("Enter customer number: ").strip()
            if number.isdigit() and len(number) == 8:
                break
            print("Error: Customer number must be exactly 8 digits.")

        customers.append(Customer(name, number, customer_id))
        print("Customer added successfully!")

    def remove_customer():
        print()

        # Check if the list of customers is empty
        if not customers:
            print("The list of customers is empty.")
            return

        CarRentalSystem.list_customers()
        print()

        # Loop until the customer ID is valid
        while True:
            customer_id = input("Enter the customer ID of the customer to remove : ").strip()

            # Validate customer ID format
            if len(customer_id) == 4 and customer_id[0] == "C" and customer_id[1:].isdigit():
                break  # Exit loop if input is valid
            else:
                print("Error: Customer ID must be in the format C followed by 3 digits (e.g., C001). Please try again.")

        # Search for the customer
        customer = next((c for c in customers if c.customer_id == customer_id), None)
        if customer:
            customers.remove(customer)
            print(f"Customer {customer.name} removed successfully!")
        else:
            print("Customer not found.")

    def rent_car():
        print()
        CarRentalSystem.list_cars()
        print("----------------------------------------------------------------------")
        CarRentalSystem.list_customers()
        print()
    
        while True:
            car_id = input("Enter the car ID of the car to rent : ").strip()
            if len(car_id) == 4 and car_id[0] == "V" and car_id[1:].isdigit():
                break
            print("Error: Car ID must be in the format V followed by 3 digits (e.g., V001).")
    
        car = next((c for c in cars if c.car_id == car_id), None)
        if car:
            if not car.is_rented:
                while True:
                    customer_id = input("Enter your customer ID : ").strip()
                    if len(customer_id) == 4 and customer_id[0] == "C" and customer_id[1:].isdigit():
                        break
                    print("Error: Customer ID must be in the format C followed by 3 digits (e.g., C001).")
            
                customer = next((c for c in customers if c.customer_id == customer_id), None)
                if customer:
                    while True:
                        try:
                            days = int(input("Enter number of days to rent : "))
                            if days > 0:
                                 break
                            print("Error: Number of days must be a positive integer.")
                        except ValueError:
                            print("Error: Number of days must be an integer.")
                
                    total_cost = days * car.daily_rate
                    rental_date = datetime.date.today()
                    return_date = rental_date + datetime.timedelta(days=days)  # Calculate final return date

                    car.is_rented = True
                    customer.rented_car = car

                    # Save to rental history file
                    with open("rental_history.txt", "a") as f:
                        f.write(f"{customer.name},{car.model},{car.year},{rental_date},{return_date},{days},Rs{total_cost}\n")

                    print()
                    print(f"{customer.name} has rented {car.model} for {days} days.")
                    print(f"Total cost: Rs{total_cost}")
                    print(f"Rental Date: {rental_date.strftime('%d/%m/%Y')}")
                    print(f"Expected Return Date: {return_date.strftime('%d/%m/%Y')}")
                else:
                    print("Customer not found. Please add the customer first.")
            else:
                print("Car is already rented.")
        else:
            print("Car not found.")
    
    def return_car():
        print()
        CarRentalSystem.list_customers()

        # Loop until the customer ID is valid
        while True:
            customer_id = input("Enter your customer ID : ").strip()

            # Validate customer ID format
            if len(customer_id) == 4 and customer_id[0] == "C" and customer_id[1:].isdigit():
                break  # Exit loop if input is valid
            else:
                print("Error: Customer ID must be in the format C followed by 3 digits (e.g., C001). Please try again.")

        # Search for the customer
        customer = next((c for c in customers if c.customer_id == customer_id), None)
        if customer and customer.rented_car:
            car = customer.rented_car
            return_date = datetime.date.today()
            car.is_rented = False
            print(f"{customer.name} has returned {car.model}.")
            customer.rented_car = None

        # Update the rental history with the return date
            with open("rental_history.txt", "r") as f:
                lines = f.readlines()
            with open("rental_history.txt", "w") as f:
                for line in lines:
                    if f"{customer.name},{car.model},{car.year},-" in line:
                            f.write(line.replace("-,", f"{return_date},"))  # Update return date
                    else:
                        f.write(line)
        else:
            print("No car to return or customer not found.")

    def view_rental_history():
        print()
        try:
            with open("rental_history.txt", "r") as f:
                print("Rental History:")
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("No rental history found.")

    def list_cars():
        print()
        print("Available Cars:")
        print()
        for car in cars:
            print(car)

    def list_customers():
        print()
        print("Customers:")
        for customer in customers:
            print(customer)


# Main function to run the program
def main():
    CarRentalSystem.load_data()
    while True:
        print("\n--------Car Rental System--------")
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

        choice = input("Enter your choice : ")

        if choice == "1":
            CarRentalSystem.add_car()
        elif choice == "2":
            CarRentalSystem.remove_car()
        elif choice == "3":
            CarRentalSystem.list_cars()
        elif choice == "4":
            CarRentalSystem.add_customer()
        elif choice == "5":
            CarRentalSystem.remove_customer()
        elif choice == "6":            
            CarRentalSystem.list_customers()
        elif choice == "7":
            CarRentalSystem.rent_car()  
        elif choice == "8":
            CarRentalSystem.return_car()
        elif choice == "9":
            CarRentalSystem.view_rental_history()
        elif choice == "10":
            print("Exiting...")
            CarRentalSystem.save_data()
            break
        else:
            print("Invalid choice, please try again.")

main()

