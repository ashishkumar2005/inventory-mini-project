# Importing ABC and abstractmethod for creating abstract class
from abc import ABC, abstractmethod

# Importing json to store inventory data in JSON format
import json

# Importing os to check if file exists
import os

# Importing datetime to log staff actions with timestamp
from datetime import datetime


# -------------------- FILE HANDLING FUNCTIONS --------------------

def load_inventory():
    """
    This function loads inventory data from inventory.json file.
    If file exists → read and return data.
    If file does not exist → return empty dictionary.
    """
    if os.path.exists("inventory.json"):  # Check if file exists
        with open("inventory.json", "r") as file:  # Open file in read mode
            return json.load(file)  # Convert JSON data to Python dictionary
    return {}  # If file doesn't exist, return empty dictionary


def save_inventory(inventory):
    """
    This function saves inventory dictionary into inventory.json file.
    """
    with open("inventory.json", "w") as file:  # Open file in write mode
        json.dump(inventory, file, indent=4)  # Convert dictionary to JSON format


def log_staff_action(action):
    """
    This function logs staff actions into staff_log.txt file.
    """
    with open("staff_log.txt", "a") as file:  # Open file in append mode
        file.write(f"{datetime.now()} - {action}\n")  # Write time + action


# -------------------- ABSTRACT CLASS --------------------

class InventorySystem(ABC):
    """
    Abstract class that forces child classes
    to implement required inventory methods.
    """

    @abstractmethod
    def view_products(self):
        pass  # Must be implemented in child class

    @abstractmethod
    def update_stock(self):
        pass  # Must be implemented in child class


# -------------------- BASE USER CLASS --------------------

class User:
    """
    Base class for Admin and Staff.
    Contains common authentication logic.
    """

    def __init__(self, username, password, role):
        self._username = username   # Protected username
        self._password = password   # Protected password
        self.role = role            # Role of user (admin/staff)

    def authenticate(self, username, password):
        """
        Checks if entered username and password match stored credentials.
        Returns True if correct, otherwise False.
        """
        return self._username == username and self._password == password


# -------------------- ADMIN CLASS --------------------

class Admin(User, InventorySystem):
    """
    Admin class inherits from:
    - User (for authentication)
    - InventorySystem (for abstract methods)
    """

    def __init__(self, username, password):
        super().__init__(username, password, "admin")  # Call parent constructor
        self.inventory = load_inventory()  # Load inventory from file


    def add_product(self):
        """
        Admin can add new products.
        Includes validation and duplicate ID check.
        """
        try:
            pid = input("Enter Product ID: ").strip()  # Remove extra spaces

            if not pid:
                print("⚠ Product ID cannot be empty!")
                return

            if pid in self.inventory:
                print("⚠ Product ID already exists!")
                return

            name = input("Enter Product Name: ").strip()
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))

            if quantity < 0 or price < 0:
                print("⚠ Quantity and Price cannot be negative!")
                return

            # Store product in dictionary
            self.inventory[pid] = {
                "name": name,
                "quantity": quantity,
                "price": price
            }

            save_inventory(self.inventory)  # Save to file
            print("✅ Product Added Successfully!")

        except ValueError:
            print("⚠ Quantity must be integer and price must be number!")


    def delete_product(self):
        """
        Admin can delete product using Product ID.
        """
        pid = input("Enter Product ID to delete: ").strip()

        if pid not in self.inventory:
            print("❌ Product ID not found!")
            return

        del self.inventory[pid]  # Remove product from dictionary
        save_inventory(self.inventory)  # Update file
        print("🗑 Product Deleted Successfully!")


    def view_products(self):
        """
        Displays all products with total inventory value.
        Also shows low stock alert.
        """
        if not self.inventory:
            print("Inventory is empty!")
            return

        total_value = 0
        print("\n--- Product List ---")

        for pid, details in self.inventory.items():
            value = details["quantity"] * details["price"]  # Calculate value
            total_value += value

            print(f"""
Product ID: {pid}
Name: {details['name']}
Quantity: {details['quantity']}
Price: {details['price']}
Total Value: {value}
-------------------------""")

            if details["quantity"] < 5:
                print("⚠ Low Stock Alert!")

        print(f"\n💰 Total Inventory Value: {total_value}")


    def update_stock(self):
        """
        Admin can update stock quantity.
        """
        try:
            pid = input("Enter Product ID to update: ").strip()

            if pid not in self.inventory:
                print("❌ Product ID not found!")
                return

            quantity = int(input("Enter new quantity: "))

            if quantity < 0:
                print("⚠ Quantity cannot be negative!")
                return

            self.inventory[pid]["quantity"] = quantity
            save_inventory(self.inventory)
            print("✅ Stock Updated!")

        except ValueError:
            print("⚠ Quantity must be a valid number!")


    def view_staff_logs(self):
        """
        Admin can view all staff actions.
        """
        if os.path.exists("staff_log.txt"):
            with open("staff_log.txt", "r") as file:
                print("\n--- Staff Activity Log ---")
                print(file.read())
        else:
            print("No staff activity found.")


# -------------------- STAFF CLASS --------------------

class Staff(User, InventorySystem):
    """
    Staff class inherits from User and InventorySystem.
    Staff has limited permissions.
    """

    def __init__(self, username, password):
        super().__init__(username, password, "staff")
        self.inventory = load_inventory()


    def view_products(self):
        """
        Staff can only view products.
        """
        if not self.inventory:
            print("Inventory is empty!")
            return

        print("\n--- Product List ---")
        for pid, details in self.inventory.items():
            print(f"{pid} | {details['name']} | Qty: {details['quantity']} | Price: {details['price']}")


    def update_stock(self):
        """
        Staff can update stock.
        Action will be logged.
        """
        try:
            pid = input("Enter Product ID to update: ").strip()

            if pid not in self.inventory:
                print("❌ Product ID not found!")
                return

            quantity = int(input("Enter new quantity: "))

            if quantity < 0:
                print("⚠ Quantity cannot be negative!")
                return

            self.inventory[pid]["quantity"] = quantity
            save_inventory(self.inventory)

            action = f"Staff updated stock of Product ID {pid} to {quantity}"
            log_staff_action(action)  # Log action

            print("✅ Stock Updated!")

        except ValueError:
            print("⚠ Quantity must be a valid number!")


# -------------------- MAIN FUNCTION --------------------

def main():
    """
    Main function controls the full system workflow.
    """

    admin = Admin("admin", "1234")  # Hardcoded admin
    staff = Staff("staff", "1111")  # Hardcoded staff

    print("Who are you?")
    print("1. Admin")
    print("2. Staff")

    role_choice = input("Enter choice: ")

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Admin login
    if role_choice == "1" and admin.authenticate(username, password):

        while True:
            print("""
1. Add Product
2. View Products
3. Update Stock
4. Delete Product
5. View Staff Logs
6. Exit
""")

            choice = input("Enter choice: ")

            if choice == "1":
                admin.add_product()
            elif choice == "2":
                admin.view_products()
            elif choice == "3":
                admin.update_stock()
            elif choice == "4":
                admin.delete_product()
            elif choice == "5":
                admin.view_staff_logs()
            elif choice == "6":
                break
            else:
                print("Invalid choice!")

    # Staff login
    elif role_choice == "2" and staff.authenticate(username, password):

        while True:
            print("""
1. View Products
2. Update Stock
3. Exit
""")

            choice = input("Enter choice: ")

            if choice == "1":
                staff.view_products()
            elif choice == "2":
                staff.update_stock()
            elif choice == "3":
                break
            else:
                print("Invalid choice!")

    else:
        print("Authentication Failed!")


# Run the program
if __name__ == "__main__":
    main()
