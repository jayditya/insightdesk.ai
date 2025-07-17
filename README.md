# insightdesk.ai
A smart support ticket system using Django and Flask. Users submit queries, and an AI model generates instant responses. Includes a dashboard, session memory, and a futuristic black-themed UI. Powered by Python, Scikit-learn, and SQLite.


# 🧠 AI-Powered Support Ticket System

> A smart support ticket system using Django and Flask. Users submit queries, and an AI model generates instant responses. Includes a dashboard, session memory, and a futuristic black-themed UI. Powered by Python, Scikit-learn, and SQLite.

---

## 🚀 Overview

This is a web-based **Support Ticket System** that uses **Machine Learning** to automatically respond to user-submitted tickets. Built with **Django** for handling submissions and dashboard views, and **Flask** for serving a trained ML model that generates intelligent replies.

---

## ✨ Features

- Submit support tickets with Name, Email, and Message  
- Get instant AI-generated responses using a trained model  
- Dashboard to view all tickets and responses  
- Remembers user details for repeated submissions  
- Logout option to reset session  
- Stylish black-themed futuristic UI

---

## 🛠 Tech Stack

- **Backend:** Django (ticket management & dashboard)  
- **API:** Flask (ML model response service)  
- **ML Tools:** Python, Scikit-learn  
- **Frontend:** HTML5, CSS3 (custom dark theme)  
- **Database:** SQLite (default)

---

## 📁 Project Structure

/project-root/
├── django-app/ # Ticket submission & dashboard
├── flask-api/ # AI model & response generation
├── static/css/ # Futuristic stylesheets
├── templates/ # HTML templates


---

## ⚙ How It Works

1. User submits a support ticket
2. Django sends the message to the Flask ML API
3. Flask predicts a response using a trained model
4. The response is saved and shown on the dashboard

---

## 🧪 Getting Started

1. **Clone the repo**  
2. Run Django server: python manage.py runserver
3. Run Flask API: python app.py
4. Open your browser at: http://127.0.0.1:8000/
