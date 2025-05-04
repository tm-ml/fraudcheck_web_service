# Insurance Claim Fraud Detection App

A Flask-based web application that allows users to submit detailed insurance claim information and receive real-time predictions about the likelihood of fraud. The system collects user input through a multi-step form and sends it to a prediction API to assess fraud risk.

---

## Features

- Multi-step form to collect:
  - Driver details,
  - Vehicle details,
  - Policy inomation,
  - Claim circumstances
- Data automatically saved to a relational database,
- Fraud assessment is made by sending a request to external API,
- Responsive interface using Flask-Bootstrap

---

## Demo

https://fraudcheck-web-service.onrender.com

---

## Tech Stack

- **Backend:** Flask
- **Database:** SQLAlchemy (SQLite, PostreSQL)
- **Frontend:** Jinja2 templates + Bootstrap5

---

## Getting Started

### How It Works
User submits form data in multiple steps:
![image](https://github.com/user-attachments/assets/d8f1291b-5994-44a3-95fe-f0cf3acfb820)
![image](https://github.com/user-attachments/assets/2f49cb53-61e4-4e57-af36-d0a1ea265d38)
![image](https://github.com/user-attachments/assets/e2e078e0-bfbf-4c52-8512-d707a05ad0dc)
![image](https://github.com/user-attachments/assets/1c6b1abc-0d1f-4d8c-878d-1530286c3268)








Data is stored in a relational SQLite database.
Once all forms are submitted, the app aggregates the data.
A JSON payload is sent to a prediction API.
The API responds with a fraud risk prediction.
The result is shown to the user and saved in the database.








