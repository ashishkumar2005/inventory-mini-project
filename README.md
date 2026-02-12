# 📘 INVENTORY MANAGEMENT SYSTEM

## Introduction

In small businesses, shops, and warehouses, managing inventory manually can lead to many problems such as data loss, incorrect stock records, and no proper monitoring of staff activities. Without a structured system, it becomes difficult to track products, update stock, or monitor changes made by employees.

To solve this problem, we have developed a Role-Based Inventory Management System using Python. This system allows different users (Admin and Staff) to access features based on their roles. It ensures that data is saved permanently and that staff activities are properly recorded.

This project demonstrates the use of Object-Oriented Programming (OOP) concepts along with file handling and error management in Python.

---

## Problem Statement

Many small businesses face the following issues:

- Stock records are maintained manually.  
- Product data may be lost when the system closes.  
- Staff members can update stock without monitoring.  
- No system to prevent duplicate product IDs.  
- Errors occur when wrong inputs are given.  

The goal of this project is to build a structured system that:

- Stores product information properly  
- Saves data permanently  
- Allows different access levels for Admin and Staff  
- Tracks staff activities  
- Prevents common input errors  

---

## Objective of the Project

The main objectives of this project are:

1. To implement a structured inventory system using OOP principles.  
2. To implement role-based authentication.  
3. To save product data using file handling.  
4. To log staff activities for monitoring.  
5. To handle user input errors safely.  
6. To create a beginner-friendly but professional system.  

---

## Technologies and Concepts Used

This project uses the following technologies and programming concepts:

- Python Programming Language  
- Object-Oriented Programming (OOP)  
- Abstraction  
- Inheritance  
- Encapsulation  
- File Handling (JSON & TXT files)  
- Exception Handling (try-except)  
- Role-Based Authentication  

---

## Explanation of OOP Concepts Used

### Abstraction

Abstraction means hiding internal implementation details and showing only necessary features.

In this project, we created an abstract class called:

`InventorySystem`

This class defines required methods like:

- `view_products()`  
- `update_stock()`  

Any class that inherits from this abstract class must implement these methods. This ensures a proper structure and consistency in the system. Abstraction helps in designing clean and professional software.

---

### Inheritance

Inheritance allows one class to use properties and methods of another class.

In this system:

- User → Base class  
- Admin → Inherits from User  
- Staff → Inherits from User  

This helps us reuse authentication logic and maintain clean code structure. Instead of writing login logic multiple times, both Admin and Staff use the same authentication system.

---

### Encapsulation

Encapsulation means protecting important data from direct access.

In this system, inventory data is stored inside the class and accessed through methods only. This prevents accidental modification and increases data safety. Encapsulation makes the system more secure and organized.

---

## Role-Based Authentication System

When the program starts, the system asks:

**Who are you?**

- Admin  
- Staff  

After selecting the role, the user must enter:

- Username  
- Password  

If authentication is successful:

- Admin gets full access  
- Staff gets limited access  

If authentication fails, access is denied. This ensures that only authorized users can access the system.

---

## Admin and Staff Functionalities

### Admin Functionalities

Admin has full control over the inventory system. Admin can:

- Add new products  
- Delete products  
- View all products  
- Update stock  
- View staff activity logs  
- View total inventory value  
- Get low stock alerts  

Admin acts as the system controller and monitors all operations.

---

### Staff Functionalities

Staff has limited access. Staff can:

- View products  
- Update stock  

Staff cannot add or delete products.

Whenever staff updates stock, the action is recorded in a log file. This ensures transparency and accountability.

---

## File Handling Implementation

File handling ensures that data is not lost when the program closes.

We use two files:

### 1. inventory.json

This file stores:

- Product ID  
- Product Name  
- Quantity  
- Price  

The data is saved in JSON format because:

- It supports dictionary structure  
- It is easy to read  
- It is easy to store and retrieve  

Whenever a product is added, deleted, or updated, the file is updated automatically.

---

### 2. staff_log.txt

This file stores staff activity logs.

Each time staff updates stock, the system records:

- Date and time  
- Product ID  
- Updated quantity  

**Example:**
2026-02-11 10:30:25 - Staff updated stock of Product ID P101 to 50


This helps the admin monitor staff actions carefully.

---

## Error Handling Strategy

To make the system stable and professional, we use try-except blocks.

The system handles:

- Invalid number input  
- Duplicate Product ID  
- Negative quantity  
- Empty Product ID  
- Wrong Product ID during update  
- Invalid price input  

Instead of crashing, the system shows proper warning messages. This approach is called Defensive Programming.

---

        Author
        Ashish Kumar
