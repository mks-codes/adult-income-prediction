#  Adult Income Predictor

This is an **end-to-end Machine Learning project** that predicts whether a person’s income is **≤ 50K** or **> 50K** based on demographic and work-related attributes.  

Built with **Python, scikit-learn, Pandas, Streamlit** 

## Project Overview
- **Goal**: Predict salary category (≤ 50K or > 50K) using census data.  
- **Dataset**: UCI Adult Income Dataset.  
- **Features Used**:
  - `age` (numeric)
  - `workclass` (categorical)
  - `education` (categorical)
  - `marital_status` (categorical)
  - `occupation` (categorical)
  - `relationship` (categorical)
  - `race` (categorical)
  - `sex` (categorical)
  - `hours_per_week` (numeric)
  - `native_country` (categorical)

---

## ⚙️ Tech Stack
- **Python 3.12**
- **scikit-learn**
- **Pandas / Numpy**
- **Joblib / Pickle** (model saving)
- **Streamlit** (deployment)
- **Matplotlib / Seaborn** (EDA)

---

## 🔑 Key Steps
1. **Data Preprocessing**
   - Handled missing values  
   - OneHotEncoding for categorical features  
   - StandardScaler for numerical features  

2. **Model Building**
   - Built a **Pipeline** with preprocessing + classifier  
   - Trained and evaluated multiple models (DecisionTree, RandomForest, Logistic Regression, etc.)  
   - Saved the final pipeline as `pipe.pkl`  

3. **Deployment**
   - Streamlit web app for user-friendly predictions  
   - Users enter their details → Model predicts income category  

---

## 🚀 How to Run Locally
Clone the repo:
```bash
git clone https://github.com/mks-codes/adult-income-prediction.git
cd adult-income-prediction

Install dependencies:
pip install -r requirements.txt

Run Streamlit app:
streamlit run app.py


