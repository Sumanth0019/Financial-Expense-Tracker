# Financial Expense Tracker

An intelligent **Financial Expense Tracking System** built using **Streamlit, Machine Learning, JWT Authentication, SQLite, and SMTP automation** to help users track expenses, analyze spending patterns, predict future expenses, manage budgets, and receive automated monthly reports.

---

##  Project Overview

Managing personal finances manually can be difficult due to irregular spending habits and lack of forecasting. This project provides a **smart financial assistant** that helps users:

- Track daily expenses
- Categorize spending patterns
- Monitor monthly budgets
- Predict future expenses using Machine Learning
- Receive automatic budget alerts
- Get monthly expense reports via email
- Visualize financial trends using interactive charts

The system transforms expense tracking from a **manual process** into an **AI-assisted budgeting and forecasting solution**.

---

# Features

##  Authentication System
- User Registration
- User Login
- Password Hashing using BCrypt
- JWT Token Authentication
- Session Management
- Logout functionality

---

## Expense Management
Users can:

 Add expenses

 Categorize expenses:

- Food
- Travel
- Shopping
- Bills
- Healthcare
- Entertainment
- Others

 View all expenses

---

## 📊 Budget Tracking

Users can set monthly budgets and monitor:

- Total spending
- Remaining budget
- Savings
- Overspending

Automatic alerts:

⚠ Budget exceeds 80%

🚨 Budget exceeded

---

## 📈 Expense Analytics

Interactive visualizations:

- Pie Charts → Expense distribution
- Bar Charts → Spending trends
- Spending patterns analysis
- Highest spending category

---

## Machine Learning Prediction

The project includes:

### Existing Regression Model
Predicts:

```plaintext
Income + Category Expenses
↓
Total Expenditure
```

---

### Forecasting Model (Time Series)

Predicts:

```plaintext
Past Monthly Expenses
↓
Future Monthly Expenses
```

Example:

```plaintext
January → ₹10000
February → ₹12000
March → ₹15000

↓

Predicted April → ₹16000
```

Uses:

- Random Forest Regression
- Lag Features
- Forecasting Model (`forecast_model.pkl`)

---

## 📧 Automated Email Notifications

The system automatically sends:

### Budget Warning Emails

When:

```plaintext
80% budget used
```

User receives:

```plaintext
Budget Warning Email
```

---

### Overspending Alerts

When:

```plaintext
Expenses > Budget
```

User receives:

```plaintext
Urgent Budget Exceeded Alert
```

---

### Monthly Reports

Automatically sent every month:

Includes:

- Total expenses
- Budget
- Savings
- Predicted future expenses

Implemented using:

- SMTP
- Gmail App Password
- APScheduler

---

## Modern Dashboard UI

Includes:

✔ Gradient backgrounds

✔ Colored sidebar

✔ Hero section

✔ Glassmorphism cards

✔ Interactive charts

✔ Hover effects

✔ Animated buttons

✔ Dark theme styling

---

# 🏗 System Architecture

```plaintext
User
 ↓
Authentication (JWT)
 ↓
Dashboard
 ↓
Expense Tracking
 ↓
Analytics
 ├── Charts
 ├── Budget Analysis
 ├── Savings
 ├── Spending Patterns
 ↓
ML Prediction
 ↓
SMTP Alerts
 ↓
Monthly Reports
```

---

# 🛠 Tech Stack

## Frontend

- Streamlit
- HTML
- CSS
- Plotly

---

## Backend

- Python
- JWT Authentication
- BCrypt
- SMTP

---

## Database

- SQLite
- SQLAlchemy ORM

---

## Machine Learning

- Scikit-Learn
- Random Forest Regression
- Forecasting Models

---

## Scheduling

- APScheduler

---

# 📂 Project Structure

```plaintext
Financial Expense Tracker/

│
├── app.py
│
├── views/
│       login.py
│       register.py
│       dashboard.py
│
├── database/
│       db.py
│       models.py
│
├── auth/
│       jwt_auth.py
│
├── utils/
│       expense.py
│       charts.py
│       styles.py
│       email_report.py
│       monthly_scheduler.py
│
├── ml/
│       preprocess.py
│       train_model.py
│       predict.py
│       forecast_train.py
│       forecast_predict.py
│
│       model.pkl
│       forecast_model.pkl
│
│       dataset/
│             monthly_spending_dataset_2020_2025.csv
│
├── expenses.db
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Installation

Clone repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Move into folder:

```bash
cd Financial-Expense-Tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Running Project

Run:

```bash
streamlit run app.py
```

Open:

```plaintext
http://localhost:8501
```

---

#  Environment Setup

For SMTP Email:

Update:

```python
sender = "YOUR_GMAIL"

app_password =
"YOUR_16_CHAR_APP_PASSWORD"
```

Generate App Password:

Google Account →

Security →

2-Step Verification →

App Password

---

# Machine Learning Workflow

## Data Collection

Dataset:

```plaintext
monthly_spending_dataset_2020_2025.csv
```

Contains:

- Monthly expenses
- Income
- Savings
- Rent
- Groceries
- Total expenditure

---

## Preprocessing

Performed:

- Date conversion
- Feature engineering
- Lag feature creation
- Missing value handling

---

## Model Training

Uses:

### Random Forest Regressor

Input:

```plaintext
Past Expenses
```

Output:

```plaintext
Future Expense Prediction
```

---

## Model Saving

Saved as:

```plaintext
model.pkl

forecast_model.pkl
```

---

# Email Automation Workflow

```plaintext
User spends
        ↓
Budget reaches 80%
        ↓
Warning Email Sent

Budget exceeded
        ↓
Urgent Email Sent

1st of every month
        ↓
Generate Monthly Report
        ↓
Email User Automatically
```

---

# Example Dashboard Features

### Dashboard Overview

Shows:

```plaintext
Welcome User 👋

Total Expenses
Remaining Budget
Savings
Budget Progress

Charts

Predicted Future Expense

Monthly Reports
```

---

# Security Features

Implemented:

Password hashing

JWT authentication

Session management

Protected routes

---

# Future Improvements

Possible enhancements:

- PDF report generation
- Downloadable analytics
- Multi-user support
- LSTM forecasting
- Prophet forecasting
- Cloud deployment
- Mobile responsiveness
- Financial recommendations
- Investment suggestions

---

# Deployment Options

Deploy using:

- Streamlit Cloud
- Render
- Railway
- AWS
- Azure

---

# Use Cases

Useful for:

- Personal finance tracking
- Budget planning
- Expense forecasting
- Financial awareness
- Spending analysis

---

# Author

Developed as an Financial Expense Management System using:

```plaintext
Python + Streamlit + Machine Learning + SQL + SMTP + JWT
```

---

# icense

This project is developed for educational and learning purposes.

You may modify and extend it for personal or academic use.

---

# Final Outcome

This project combines:

```plaintext
Authentication
+
Expense Tracking
+
Visualization
+
Budget Management
+
Machine Learning
+
Forecasting
+
Email Automation
+
Modern UI
```

to create a complete:

# Financial Expense Tracker