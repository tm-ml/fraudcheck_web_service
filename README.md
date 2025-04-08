# 🛡️ Insurance Claim Fraud Detection App

A Flask-based web application that allows users to submit detailed insurance claim information and receive real-time predictions about the likelihood of fraud. The system collects user input through a multi-step form and sends it to a prediction API to assess fraud risk.

---

## 🚀 Features

- Multi-step form to collect:
  - Driver information
  - Vehicle details
  - Policy data
  - Claim circumstances
- Automatic record creation in a relational database
- Fraud detection via external API request
- Organized views for users and data administrators
- Responsive interface using Flask-Bootstrap

---

## 🖼️ Demo

https://fraudcheck-web-service.onrender.com

---

## 📦 Tech Stack

- **Backend:** Flask
- **Database:** SQLAlchemy (SQLite, PostreSQL)
- **Frontend:** Jinja2 templates + Bootstrap5
- **Environment Management:** python-dotenv
- **Prediction Service:** Custom API call via `make_request()`

---

## 🧑‍💻 Getting Started

🧠 How It Works
User submits form data in multiple steps.
Data is stored in a relational SQLite database.
Once all forms are submitted, the app aggregates the data.
A JSON payload is sent to a prediction API.
The API responds with a fraud risk prediction.
The result is shown to the user and saved in the database.

📊 Database View
Use the /database route to view all submitted requests and prediction results in table format.

📬 Contact
Feel free to get in touch via the Contact Page in the app — or just open an issue on GitHub.

🌱 Contributing
Contributions are welcome! If you'd like to help, open a pull request or submit feedback via issues.




