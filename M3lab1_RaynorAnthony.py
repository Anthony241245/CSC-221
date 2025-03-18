# Anthony Raynor
# M3lab1
# 3/13/25
# Reading csv data into class onjects
import csv

# Make a class
class Customer:
    # Create __init__ function
    def __init__(self, first, last, phone, email, state, address):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.state = state
        self.address = address

    def display_info(self):
        return f"\n{self.first} {self.last}\n{self.phone}\n{self.email}\n{self.address}, {self.state}\n\n"
    
# Test
# customer1 = Customer("Anthony", "J", "704-555-4521", "JJOE@gmail.com", "NC","2313 fasthill drive")

# print(customer1.display_info())

# Create Empty List to hold csv info
def main():

    add_customer = input("Would you like to add a new Customer: ")

    while add_customer != "no":

        fname = input("Enter customer's first name: ")
        lname = input("Enter customer's last name : ")
        pnumber = input("Enter customer's phone number: ")
        email = input("Enter customer's email: ")
        state = input("Enter customer's State: ")
        address = input("Enter customer's address: ")

        with open('customer.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([fname, lname, pnumber, email, state, address])
        add_customer = input("Add another customer: ")

        
     
    

    customers = []

    with open('customer.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            customer = Customer(*row)
            customers.append(customer)

    for customer in customers[1:]:
        print(customer.display_info())


    # Get info from user

    

    # call main
main()
