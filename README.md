<h1 align="center"><b>PERSONALYZE</b></h1>
<h3 align="center"><i>A Plotly-powered R Dashboard using Logistic Regression to visualize and analyze Heart Failure clinical records for predictions and insights</i></h3> 

**Personalyze** is a lightweight AI-powered web application designed to predict whether a person is an **Introvert** or **Extrovert** based on social behavior inputs. The app features a machine learning backend and a clean Streamlit frontend—packaged and deployed using Docker.
<div align="center">
  <img height="200" src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmx2ZWs1bDYyZzFqOTh5ODJ3cXpqMmpzMG5iNHVkZjRiaXE5MWo0NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ie3U6gTmbY4KTQtOPJ/giphy.gif"  />
</div>
<br> 

---

## 🔍 What it Does

This app uses a trained classification model to analyze determine your personality type based on factors :
- Time spent alone
- Stage fear level
- Social event attendance
- Social media activity
- Friend circle size
- Post frequency

---

## 🚀 Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: FastAPI (Python)
- **ML Model**: Trained using KNN, SVM, Logistic Regression, Random Forest
- **Containerization**: Docker & Docker Compose

---

## 🐳 Run Locally with Docker

### Step 1: Clone the Repo

```bash
git clone https://github.com/yourusername/personalyze.git
cd personalyze
