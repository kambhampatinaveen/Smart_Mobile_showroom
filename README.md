# Smart Mobile Showroom

A simple Smart Mobile Showroom web application developed using Python, Flask, HTML, CSS, and MongoDB. The application allows users to browse mobile phones and place orders through an easy-to-use web interface. Customer order details are stored in a MongoDB database.

## Features

- Home page displaying the mobile showroom
- Mobile products page
- Order placement page
- Customer order form
- Stores order details in MongoDB
- Simple and responsive user interface

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- MongoDB
- PyMongo

## Project Structure

```
Smart Mobile Showroom/
│
├── app.py
├── index.html
├── mobile.html
├── order.html
└── style.css
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-mobile-showroom.git
```

### 2. Move into the Project Folder

```bash
cd smart-mobile-showroom
```

### 3. Install Required Packages

```bash
pip install flask pymongo
```

### 4. Start MongoDB

Make sure MongoDB is installed and running locally on:

```
mongodb://localhost:27017/
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Browser

```
http://127.0.0.1:5000/
```

## Database

Database Name

```
mobile_showroom
```

Collection Name

```
orders
```

Each order stores:

- Customer Name
- Email Address
- Phone Number
- Address
- Payment Method

## Future Improvements

- User Authentication
- Shopping Cart
- Product Search
- Admin Dashboard
- Online Payment Gateway
- Order Tracking
- Product Images from Database
- Responsive Mobile Design

## Learning Outcomes

This project helped in understanding:

- Flask Routing
- HTML Form Handling
- MongoDB Integration
- Database Operations using PyMongo
- Frontend and Backend Integration
- Web Application Development


## License

This project is created for learning and educational purposes.
