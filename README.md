# 🧫 Yeast Purity Prediction System

## 📌 Project Overview

The **Yeast Purity Prediction System** is a full stack web application developed during my internship at **Shiash Info Solutions**. The application uses machine learning to predict the purity of yeast samples based on various chemical and physical properties. This is particularly useful in biotechnology and fermentation-based industries, where yeast quality directly impacts production outcomes.

---

## 🧠 Key Features

- Predicts yeast purity using ML classification algorithms
- Real-time web-based prediction system
- Clean, user-friendly interface
- Stores user input and prediction results in a database
- End-to-end integration of AI with web technologies

---

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **Other Tools**: Django Admin, Joblib (for model serialization)

---

## 📊 Machine Learning Details

- Data preprocessing: cleaning, normalization, feature selection
- Algorithms tested: Logistic Regression, Random Forest, SVM
- Best-performing model serialized and integrated into Django backend
- Accuracy metrics used for evaluation

---

## 🔄 Workflow

1. User inputs yeast sample features via a web form
2. Backend sends the data to the ML model
3. Model returns prediction (Pure / Impure)
4. Result is displayed on the UI and saved to the database

---

## 🧪 Sample Features Used for Prediction

- Temperature
- pH value
- Fermentation time
- Moisture level
- Alcohol yield

*Note: These are placeholder features for illustration; adjust based on your actual dataset.*

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/yeast-purity-prediction.git

# Navigate into the project
cd yeast-purity-prediction

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run the Django server
python manage.py runserver



📬 Contact
Developer: Bharath
Internship Organization: Shiash Info Solutions
Email: your.email@example.com
LinkedIn: linkedin.com/in/yourprofile



✅ Status
Project: Completed
Future Scope: Add real-time sensor integration and model retraining with new data.

---

Let me know if you'd like me to generate a `requirements.txt` or help you set up the folder structure for uploading this project to GitHub.

