# Insurance Claim Fraud Detection App

A Flask-based web application allows users to submit detailed insurance claim information and receive predictions about the likelihood of fraud. The system collects user input through a multi-step form and sends it to external API to get preiction about potential classification (fraud, not fraud).

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
During filling the forms, data is collected into relatinal database. A JSON payload is sent to external API to get a prediction.
![image](https://github.com/user-attachments/assets/d8f1291b-5994-44a3-95fe-f0cf3acfb820)
![image](https://github.com/user-attachments/assets/2f49cb53-61e4-4e57-af36-d0a1ea265d38)
![image](https://github.com/user-attachments/assets/e2e078e0-bfbf-4c52-8512-d707a05ad0dc)
![image](https://github.com/user-attachments/assets/1c6b1abc-0d1f-4d8c-878d-1530286c3268)
The prediction is showed to user.
![image](https://github.com/user-attachments/assets/06c12e5f-074a-48fd-b055-ba4908da3304)
It is possible to check last prediction in database section.
![image](https://github.com/user-attachments/assets/878509ee-9f0b-4a53-a5ca-8bc3c365c275)









