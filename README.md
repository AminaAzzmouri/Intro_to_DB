# 📚 ALX Book Store SQL Database

Welcome to the **ALX Book Store** project! This repository contains a MySQL database schema designed for an online bookstore. The schema models essential components such as books, authors, customers, orders, and order details.

## 🗄️ Database Name

`alx_book_store`

---

## 🧱 Database Schema Overview

### 1. `Authors`
Stores information about book authors.

- `author_id` (Primary Key)
- `author_name` - `VARCHAR(215)`

### 2. `Books`
Stores details about books available for sale.

- `book_id` (Primary Key)
- `title` - `VARCHAR(130)`
- `author_id` (Foreign Key referencing `Authors`)
- `price` - `DOUBLE`
- `publication_date` - `DATE`

### 3. `Customers`
Stores customer information.

- `customer_id` (Primary Key)
- `customer_name` - `VARCHAR(215)`
- `email` - `VARCHAR(215)`
- `address` - `TEXT`

### 4. `Orders`
Stores order data made by customers.

- `order_id` (Primary Key)
- `customer_id` (Foreign Key referencing `Customers`)
- `order_date` - `DATE`

### 5. `Order_Details`
Stores the books included in each order.

- `orderdetailid` (Primary Key)
- `order_id` (Foreign Key referencing `Orders`)
- `book_id` (Foreign Key referencing `Books`)
- `quantity` - `DOUBLE`

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/alx_book_store.git
cd alx_book_store
