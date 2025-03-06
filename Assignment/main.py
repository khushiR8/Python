import datetime

# Global lists to store cars and customers
cars = []
customers = []


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

    # Destructor to clean up resources
    def __del__(self):
        Vehicle.vehicle_count -= 1  # Decrement vehicle count
        print(f"A vehicle ({self._model}) has been deleted.")

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


# Helper functions for file operations
def load_data():
    global cars, customers
    try:
        with open("cars.txt", "r") as f:
            for line in f:
                car_id, model, year, color, daily_rate, rented = line.strip().split(",")
                cars.append(Car(car_id, model, int(year), color, float(daily_rate), rented == "True"))
    except FileNotFoundError:
        pass

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


# Helper functions for car and customer managemenT

def add_car():
    car_id = input("Enter car ID: ").strip()
    # Validate car ID format (e.g., C followed by 3 digits)
    if not (len(car_id) == 4 and car_id[0] == "C" and car_id[1:].isdigit()):
        print("Error: Car ID must be in the format C followed by 3 digits (e.g., C001).")
        return

    # Check if car ID already exists
    if any(c.car_id == car_id for c in cars):
        print("Error: Car ID already exists.")
        return

    model = input("Enter the car model: ").strip()

    try:
        year = int(input("Enter the car year: "))
        current_year = datetime.datetime.now().year
        if year > current_year:
            print(f"Error: Year cannot be in the future. Current year is {current_year}.")
            return
    except ValueError:
         print("Error: Car year must be an integer.")
         return





    color = input("Enter the car color: ").strip()
    if not color or any(char.isdigit() for char in color):
        print("Error: Car color cannot be empty or contain digits.")
        return

    try:
        daily_rate = float(input("Enter daily rental price: "))
    except ValueError:
        print("Error: Daily rental price must be a valid number.")
        return

    try:
        cars.append(Car(car_id, model, year, color, daily_rate))
        print("Car added successfully!")
    except ValueError as e:
        print(f"Error: {e}")



def remove_car():
    list_cars()
    car_id = input("Enter the car ID of the car to remove : ").strip()

    # Validate car ID format
    if not (len(car_id) == 4 and car_id[0] == "C" and car_id[1:].isdigit()):
        print("Error: Car ID must be in the format C followed by 3 digits (e.g., C001).")
        return

    car = next((c for c in cars if c.car_id == car_id), None)
    if car:
        cars.remove(car)
        print(f"Car {car.model} removed successfully!")
    else:
        print("Car not found.")


def add_customer():
    customer_id = input("Enter customer ID : ").strip()
    # Validate customer ID format (e.g., C followed by 3 digits)
    if not (len(customer_id) == 4 and customer_id[0] == "C" and customer_id[1:].isdigit()):
        print("Error: Customer ID must be in the format C followed by 3 digits (e.g., C001).")
        return

    # Check if customer ID already exists
    if any(c.customer_id == customer_id for c in customers):
        print("Error: Customer ID already exists.")
        return
    
    name = input("Enter customer name : ").strip()
    if not name or any(char.isdigit() for char in name):
        print("Error: Customer name cannot be empty or contain digits.")
        return

    number = input("Enter customer number : ").strip()
    # Validate that the number is exactly 8 digits and contains only digits
    if not number.isdigit() or len(number) != 8:
        print("Error: Customer number must be exactly 8 digits.")
        return

    customers.append(Customer(name, number, customer_id))
    print("Customer added successfully!")


def remove_customer():
    list_customers()
    customer_id = input("Enter the customer ID of the customer to remove : ").strip()

    # Validate customer ID format
    if not (len(customer_id) == 4 and customer_id[0] == "C" and customer_id[1:].isdigit()):
        print("Error: Customer ID must be in the format C followed by 3 digits (e.g., C001).")
        return

    customer = next((c for c in customers if c.customer_id == customer_id), None)
    if customer:
        customers.remove(customer)
        print(f"Customer {customer.name} removed successfully!")
    else:
        print("Customer not found.")


def rent_car():
    list_cars()
    print("*******************************************************************************************************")
    list_customers()
    car_id = input("Enter the car ID of the car to rent : ").strip()

    # Validate car ID format
    if not (len(car_id) == 4 and car_id[0] == "C" and car_id[1:].isdigit()):
        print("Error: Car ID must be in the format C followed by 3 digits (e.g., C001).")
        return

    car = next((c for c in cars if c.car_id == car_id), None)
    if car:
        if not car.is_rented:
            customer_id = input("Enter your customer ID : ").strip()

            # Validate customer ID format
            if not (len(customer_id) == 4 and customer_id[0] == "C" and customer_id[1:].isdigit()):
                print("Error: Customer ID must be in the format C followed by 3 digits (e.g., C001).")
                return

            customer = next((c for c in customers if c.customer_id == customer_id), None)
            if customer:
                try:
                    days = int(input("Enter number of days to rent : "))
                except ValueError:
                    print("Error: Number of days must be an integer.")
                    return

                total_cost = days * car.daily_rate
                rental_date = datetime.date.today()
                return_date = rental_date + datetime.timedelta(days=days)  # Calculate final return date

                car.is_rented = True
                customer.rented_car = car
                print(f"{customer.name} has rented {car.model} for {days} days.")
                print(f"Total cost: Rs{total_cost}")
                print(f"Rental Date: {rental_date.strftime('%d/%m/%Y')}")
                print(f"Return Date: {return_date.strftime('%d/%m/%Y')}")

                # Save to rental history file
                with open("rental_history.txt", "a") as f:
                    f.write(f"{customer.name},{car.model},{car.year},{rental_date},{return_date},{days},Rs{total_cost}\n")
            else:
                print("Customer not found. Please add the customer first.")
        else:
            print("Car is already rented.")
    else:
        print("Car not found.")


def return_car():
    list_customers()
    customer_id = input("Enter your customer ID : ").strip()

    # Validate customer ID format
    if not (len(customer_id) == 4 and customer_id[0] == "C" and customer_id[1:].isdigit()):
        print("Error: Customer ID must be in the format C followed by 3 digits (e.g., C001).")
        return

    customer = next((c for c in customers if c.customer_id == customer_id), None)
    if customer and customer.rented_car:
        car = customer.rented_car
        return_date = datetime.date.today()
        car.is_rented = False
        print(f"{customer.name} has returned {car.model}.")
        customer.rented_car = None

        with open("rental_history.txt", "r") as f:
            lines = f.readlines()
        with open("rental_history.txt", "w") as f:
            for line in lines:
                if f"{customer.name},{car.model},{car.year},-" in line:
                    f.write(line.replace("-,", f"{return_date},"))
                else:
                    f.write(line)
    else:
        print("No car to return or customer not found.")


def view_rental_history():
    try:
        with open("rental_history.txt", "r") as f:
            print("Rental History:")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No rental history found.")


def list_cars():
    print("Available Cars:")
    for car in cars:
        print(car)


def list_customers():
    print("Customers:")
    for customer in customers:
        print(customer)


# Main function to run the program
def main():
    load_data()
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
            add_car()
        elif choice == "2":
            remove_car()
        elif choice == "3":
            list_cars()
        elif choice == "4":
            add_customer()
        elif choice == "5":
            remove_customer()
        elif choice == "6":
            list_customers()
        elif choice == "7":
            rent_car()
        elif choice == "8":
            return_car()
        elif choice == "9":
            view_rental_history()
        elif choice == "10":
            print("Exiting...")
            save_data()
            break
        else:
            print("Invalid choice, please try again.")


#if __name__ == "__main__":
main()