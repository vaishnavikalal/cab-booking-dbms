# Cab Booking System 🚖

> 📚 **Academic Project** — Developed as part of a Database Management Systems (DBMS) coursework at UTA.

This project is a **Database Management System** designed for a **Cab Booking Company** to manage and store data related to bookings, customers, drivers, cabs, and locations. It captures essential information to help efficiently run a cab booking business within a city.

---

## 👥 Team Members

- Aarti Agrawal
- Mansi Patel
- Vaishnavi Kalal
- Sakshi Kshirsagar

---

## ✨ Key Features

- **Customer & Driver Management** — Stores personal details, ride history, and account creation records.
- **Cab Booking System** — Manages cab availability, booking records, and ride details.
- **Pricing & Payment System** — Fixed pricing model for different vehicle categories and travel passes.
- **Data Insights** — Analyze peak booking times, demand for car types, and location-based ride trends.

---

## 🛠️ Tech Stack

`MySQL` `Python3` `Java` `JDBC` `Oracle` `HTML5` `CSS3`

---

## 🚀 How to Run

**Requirements:**
1. Python3
2. `oracledb` library
3. `tabulate` library
4. `instantclient_21_7` saved on desktop
5. Connected to Pulse Secure VPN

**Steps:**
1. Open `script.py` in any Python interpreter
2. Run the file
3. Navigate through the Command Line GUI and select any option

---

## 🖥️ Command Line Interface

Once you run the project, you'll be presented with the following menu:

```
-------------------------------------- ACTIONABLE ITEMS --------------------------------

1.  List of All Database Tables
2.  Get information of a selected table
3.  Change the Last Name of Customer
4.  View Customer details with Customer ID
5.  Add new Location
6.  Which pickup location has the highest number of bookings?
7.  Which drop location has the highest number of bookings?
8.  Which Category of car has the highest demand in terms of bookings?
9.  Retrieve customer ID, Pass ID and total amount spent by given range of customer for highest revenue generating customers
10. Retrieve vehicle ID, pickup and drop locations and sum total of revenue for range of given V_ID
11. View Customer list with total number of particular zipcode
0.  Exit
```

---

## 💡 Future Improvements

### 🖥️ Frontend / UI
- Build a proper web interface using Flask or Django instead of command line
- Add a mobile app (React Native or Flutter)
- Admin dashboard with charts showing booking trends, revenue, and peak hours



### ☁️ Deployment
- Host the database on AWS RDS or Supabase
- Deploy the app on Heroku or Render
- Add a REST API so frontend and mobile can connect easily

---

## 📄 Documentation

Refer to the following files in this repo for more details:
- `Project Overview.pdf` — Full project description
- `EER Diagram.pdf` — Entity-Relationship diagram
- `Relational Mapping.pdf` — Database schema
- `BCNF Normalization.jpeg` — Normalization details
- `Presentation.pdf` — Project presentation slides
