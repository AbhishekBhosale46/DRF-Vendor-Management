
# Vendor Management System Api

Vendor Management System REST API built using Django and Django REST Framework. This system efficiently manages vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

## Key Features

**Vendor Profile Management:**
Effortlessly create, manage, and update vendor profiles. The system enables a seamless retrieval of essential vendor information, including contact details, address, and a unique vendor code. With a RESTful API, users can perform operations such as creating new vendor profiles, listing all vendors, retrieving specific vendor details, updating vendor information, and even deleting a vendor when necessary.

**Purchase Order Tracking:**
Track and manage purchase orders efficiently. The system allows the creation, listing, retrieval, update, and deletion of purchase orders. Each purchase order is meticulously recorded with details such as the purchase order number, vendor reference, order date, items, quantity, and status. Users can filter purchase orders by vendor, retrieve specific purchase order details, and update or delete purchase orders as needed.

**Performance Metrics:**
Automated calculations include the on-time delivery rate, quality rating average, average response time, and fulfillment rate. These metrics offer a comprehensive view of vendor performance, aiding organizations in making informed decisions and maintaining high operational standards.

**User Authentication:** 
Users can register and log in securely. Token-based authentication for API access.

## Deployed API

[Deployed API](https://drf-vendor-management-production.up.railway.app/api/docs/)

## Documentation

[Postman Documentation](https://documenter.getpostman.com/view/23351614/2s9YkjBPKw)

## Run Locally

**1] Clone the project**

```bash
  git clone https://github.com/AbhishekBhosale46/DRF-Vendor-Management
```

**2] Go to the project directory**

```bash
  cd my-project
```

**3] Install dependencies**

```bash
  pip install -r requirements.txt
```

**4] Set up the database**

```bash
  python manage.py migrate
```

**5] Start the development server**

```bash
  python manage.py runserver
```



