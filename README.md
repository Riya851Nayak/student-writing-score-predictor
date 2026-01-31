# Student Writing Score Predictor
This is a Machine Learning web application built using **Streamlit**.

# Structure 
student-writing-score-predictor/
│
├── app.py
├── models/
│   └── writing_score_model.pkl
├── README.md
├── requirements.txt


## Project Overview
The app predicts a student's **writing score** based on:
- Math score
- Reading score

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## How to Run the Project
1. Clone the repository
2. Install dependencies
   pip install -r requirements.txt
3. Run the Streamlit app
   streamlit run app.py

## Machine Learning Model
- Random Forest Regressor
- Trained on student performance dataset

## Future Improvements
- Deploy app on Streamlit Cloud
- Add more input features
- Improve model accuracy

# important points
- Built an end-to-end Machine Learning web application using Streamlit
- Trained and deployed a regression model to predict student writing scores
- Implemented model saving/loading using Joblib
- Created an interactive UI for real-time predictions


