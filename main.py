from datetime import datetime, timedelta
import calendar
import os

class Person:
    def __init__(self, fname, lname, phone, email, DOB):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.DOB = DOB

class Guest(Person):
    def __init__(self, guestID, fname, lname, phone, email, DOB):
        super().__init__(fname, lname, phone, email, DOB)
        self.guestID = guestID

    def check_guest(self,id):
        with open(r"Guest.txt", "r") as file:
            listguestid=[]
            for line in file:
                x=line.strip()
                listguestid=x.split("|")
                if id== listguestid[0] :
                    return True
        return False

    def save_guest(self):
        with open(r"Guest.txt", "a") as file:
            file.write(f"{self.guestID}|{self.fname}|{self.lname}|{self.phone}|{self.email}|{self.DOB}\n")
    
    def print_invoice(self,price):
        os.system('cls')
        today = datetime.today()
        print( f"""\n{'='*40}\n🏨 HOTEL INVOICE RECEIPT 🏨\n{'='*40}\nCustomer: {self.fname} {self.lname}\nDate: {today.year}/{today.month}/{today.day}\n{'-'*40}\n{'-'*40}\nTotal Amount:  Rs {price:.2f}\n{'='*40}\nThank you for your stay! We hope to see you again.\n""")
 
    def view_customer():
        print(f"----------------------🛎️ VIEW GUEST DETAILS 🛎️----------------------")
        with open('Guest.txt','r') as file:
           for x in file:
                line = x.split('|')
                print(f"Guest ID: {line[0]} | First name: {line[1]} | Last name: {line[2]} | Phone No {line[3]}\nGuest Email {line[4]} | Date of Birth {line[5]}\n{"-" * 72} ")
                
class Room():
    def __init__(self, roomNo, room_type):
        self.roomNo = roomNo
        self.room_type = room_type

    def choose_which_file(self,type):
        if type== "single":
            return r"single.txt"
        elif type=="double":
            return r"double.txt"
        elif type=="family":
            return r"family.txt"
        else:
            os.system('cls')
        return self.choose_which_file()
          
    def display_room_available(type):
        checklist=[]
        listidavailable=[]
        listroomavailable=[]
        def check_date(x):
            while True:
                try:
                    cdate= input(x)
                    return datetime.strptime(cdate, "%Y-%m-%d").date()
                except ValueError:
                  print("Invalid format! Please enter the date in YYYY-MM-DD format.")
        x=0
        while x==0:
            check_in = check_date("Enter check-in date (YYYY-MM-DD): ")
            check_out = check_date("Enter check-out date (YYYY-MM-DD): ")
            if check_out <= check_in:
                print("Error: Check-out date must be after check-in date.")
            else:
                x=1
                current_date = check_in
                while current_date <= check_out:
                    checklist.append(str(current_date))
                    current_date += timedelta(days=1)
        x=Room.choose_which_file(Room,type)
        with open(x,'r') as sroom:
            for line in sroom:
                if any(str(i) in line for i in checklist):
                            continue    
                x=line.strip()
                listroomavailable.append(x.split("|"))
                for row in listroomavailable:
                    if row[0] not in listidavailable:
                        listidavailable.append(row[0])

            cin=check_in.strftime("%Y-%m-%d")
            cout=check_out.strftime("%Y-%m-%d")
            os.system('cls')
            return listidavailable,cin,cout

class System():
    def __init__(self,Room,checkin,checkout):
        self.room = Room
        self.check_in = checkin
        self.check_out = checkout

    def display_menu(self):
        print("Welcome to the hotel Reservation system\n1. Make a booking\n2. View guest details\n3. Cancel a booking\n4. View all booking\n5. Exit\n")
        x=str(input("Enter correct option : "))
        os.system('cls')
        if x in "12345":
            return x
          
    def display_calendar(self,remove):
        os.system('cls')
        currentmonth = datetime.now().month
        currentyear = datetime.now().year # Get current date
        currentday = datetime.now().day
        for i in range(1, currentday +1):  # Remove all past days from the current month
            remove[currentmonth - 1].append(i)   # Add all days from 1st to today to be removed
        for month in range(currentmonth, currentmonth + 3): # Display the next 2 months' calendars with unavailable days removed
            cal = calendar.monthcalendar(currentyear, month)
            print(f"\n{calendar.month_name[month]} {currentyear}") # print name and year of month
            for week in cal:
                for i, day in enumerate(week):
                    if day in remove[month - 1]:  # Check if the day is in the list of unavailable days
                        week[i] = "--"  # Replace with "--" instead of number
                    elif day == 0:
                        week[i] = "  "  # Keep empty spaces       
                print(" ".join(f"{str(day):>2}" for day in week))   # Print formatted week
            
    def find_date_to_remove(self,file):
        list1=[]
        listdays=[[] for _ in range(12)]
        listallbook=[[] for _ in range(12)]
        with open(file,'r') as fileroom:
            for line in fileroom:
                x=line.strip()
                list1.append(x.split("|"))
            for row in list1:
                for day in row[1:]:
                    x=datetime.strptime(day, "%Y-%m-%d")
                    month=x.month
                    day=x.day
                    listdays[month-1].append(day)
            for row in range(len(listdays)):
                for day in range(len(listdays[row])):
                    x=listdays[row].count(listdays[row][day])
                    if x==5:
                        if listdays[row][day] not in listallbook[row]:
                            listallbook[row].append(listdays[row][day])
            return(listallbook) 

    def calculate_price(self,Room):
        if Room.room_type== "single":
            price=1000
        elif Room.room_type== "double" :
            price=2000
        else:
          price = 3000  
        date1 = datetime.strptime(self.check_in, "%Y-%m-%d")
        date2 = datetime.strptime(self.check_out, "%Y-%m-%d")
        total_days = (date2-date1).days
        return int(total_days) * price
    
    def save_reservation(self, guest):
        with open("reservation.txt", "a") as file:
            file.write(f"{guest.guestID}|{guest.fname}|{guest.lname}|{self.room.roomNo}|{self.room.room_type}|{self.check_in}|{self.check_out}\n")

    def view_booking():
        print(f"------------------------📅 VIEW YOUR BOOKINGS 📅-----------------------")
        with open('reservation.txt','r') as file:
            for x in file:
                line = x.split('|')
                print(f"Guest ID: {line[0]} | First name: {line[1]} | Last name: {line[2]} | Room No {line[3]} | Room Type {line[4]}\nCheck-in Date: {line[5]} | Check-out Date: {line[6]}\n{"-" * 72}")

    def cancel_reservation():
        print(f"------------------------❌ CANCEL YOUR RESERVATION ❌-----------------------\nPlease enter the Guest ID of the reservation you'd like to cancel:")
        while not (id := input("Enter 4-digit guest ID: ")).isdigit() or len(id) != 4: #validation for geust ID
            print("Invalid ID! Please enter a 4-digit number.")
        with open('reservation.txt', 'r') as file: # Read all lines from the file
            data = file.readlines() # Read all lines from the file
            found = False
            for line in data: #retrieves specific fields to use in remove_checkdate
                retrieved = line.split('|')
                if retrieved[0] == id:
                    found = True
                    Rno = retrieved[3]
                    Rtype = retrieved[4]
                    Cin = retrieved[5].strip()
                    Cout = retrieved[6].strip()
        if found == True:
            with open('reservation.txt', 'w') as file: # Open the file in write mode to overwrite the contents
                for line in data:
                    info = line.split('|')
                    if info[0] != id: # Write the line back if it doesn't match the ID to cancel
                        file.write(line)
            System.remove_checkdate(Rtype,Rno,Cin,Cout)
            print('RESERVATION CANCELLED!')
        else:
            print(f"No reservation found for Guest ID {id}.\n")
        
    def add_new_checkdate_room(self,Room):
        date_list = []
        updated_lines = []
        if Room.room_type== "single":
                file= r"single.txt"
        elif Room.room_type=="double":
                file= r"double.txt"
        elif Room.room_type=="family":
                file= r"family.txt"
        with open(file, "r") as file1:
                lines = file1.readlines()
        start_date= datetime.strptime(self.check_in, "%Y-%m-%d")
        end_date = datetime.strptime(self.check_out, "%Y-%m-%d")
        current_date = start_date
        while current_date <= end_date:
                date_list.append(current_date.strftime("%Y-%m-%d"))
                current_date += timedelta(days=1)
        id_found = False
        for line in lines:
                if line.startswith(Room.roomNo):  # If the line contains the ID, update it
                    line = line.strip() + "|" + "|".join(date_list) + "\n"
                    id_found = True
                updated_lines.append(line)
        if not id_found:
            updated_lines.append(f"{Room.roomNo}|{'|'.join(date_list)}\n")
        with open(file, "w") as file2:
            file2.writelines(updated_lines)
   
    def remove_checkdate (Roomt,id,checkin,checkout):
        dates_to_remove = []
        file_map = {"single": "single.txt", "double": "double.txt", "family": "family.txt"}
        file_path = file_map.get(Roomt)
        with open(file_path, "r") as file1:
            lines = file1.readlines()
        start_date = datetime.strptime(checkin, "%Y-%m-%d")
        end_date = datetime.strptime(checkout, "%Y-%m-%d")
        current_date = start_date
        while current_date <= end_date:
            dates_to_remove.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)
        updated_lines = []
        for line in lines:
            parts = line.strip().split("|")  # Split by '|'
            if parts[0] == id:  # If it's the matching ID
                filtered_dates = [date for date in parts[1:] if date not in dates_to_remove]  # Remove dates
                if filtered_dates:
                    line = id + "|" + "|".join(filtered_dates) + "\n"  # Rebuild line
                else:
                    continue  # If no dates left, remove the line completely
            updated_lines.append(line)
        with open(file_path, "w") as file2:
            file2.writelines(updated_lines)
         
def main():
    os.system('cls')
    option=str(System.display_menu(System))     
    while option != "5":                    
        while option not in "12345":
            option=str(System.display_menu(System))                       
        if option =="1":
            print(f"""\n--------------------- 🏨 ROOM PRICES 🏨 --------------------\n|      Room Type       |      Price per Night (Rs)            |\n--------------------------------------------------------------\n|        SINGLE        |             1,000                    |\n|        DOUBLE        |             2,000                    |\n|        FAMILY        |             3,000                    |\n-------------------------------------------------------------\n""")
            Roomt=str(input("Enter correct room type : ")).strip().lower()                
            while Roomt not in ["single","double" ,"family"]:                               
                Roomt=str(input("Enter correct room type : ")).strip().lower()              
            y=Room.choose_which_file(Room,Roomt)
            x=System.find_date_to_remove(System,y)
            System.display_calendar(System,x)
            room_available=Room.display_room_available(Roomt)
            print("Available rooms are : ")
            print(room_available[0])
            while True:
                room_number = input("Enter Room Number: ")
                if room_number in room_available[0]:
                    room1 = Room(room_number, Roomt) #object room
                    os.system('cls')                          
                    break  
                else:
                    print("Enter room id in the list above")
            while not (id := input("Enter 4-digit guest ID: ")).isdigit() or len(id) != 4: #validation for geust ID
                print("Invalid ID! Please enter a 4-digit number.")
            flag=Guest.check_guest(Guest,id)
            if flag ==False:
                while not (fname := input("Enter First Name: ")).isalpha(): print("Invalid! Only letters allowed.") #validation for first name
                while not (lname := input("Enter Last Name: ")).isalpha(): print("Invalid! Only letters allowed.") #validation for last name
                while not (pnum := input("Enter Phone Number (8 digits): ")).isdigit() or len(pnum) != 8: print("Invalid! Enter a 8-digit number.") #validation for phone number
                while not (email := input("Enter Email: ")).count("@") == 1 or "." not in email.split("@")[-1]: print("Invalid! Enter a valid email.") #validation for email
                while not (dob := input("Enter DOB (YYYY-MM-DD): ")).count("-") == 2 or len(dob) != 10: print("Invalid! Use format YYYY-MM-DD.") #validation for date of birth
                guest1 = Guest(id, fname, lname, pnum, email,dob) #object guest
                Guest.save_guest(guest1)
            else:
                print("Guest already exist") #get guest information then print invoice
            with open('Guest.txt','r') as file:
                for line in file:  
                    data = line.split('|')
                    if data[0] == id:
                        guest1 = Guest(data[0],data[1],data[2],data[3],data[4],data[5])  
            system1=System(room1,room_available[1],room_available[2])  
            system1.save_reservation(guest1)                                             
            print(guest1.print_invoice(system1.calculate_price(room1)))
            system1.add_new_checkdate_room(room1)
        elif option=="2":
            Guest.view_customer()
        elif option=="3":
            System.cancel_reservation()
        elif option=="4":
            System.view_booking() 
        else:
            print("exit")
        option=str(System.display_menu(System))

main()