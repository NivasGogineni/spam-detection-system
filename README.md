# Spam Detection System

A Machine Learning-based web application that classifies SMS/text messages as Spam or Ham using Natural Language Processing (NLP) techniques.

## Features
- Spam and Ham message classification
- TF-IDF Vectorization
- Machine Learning Model
- Django Web Interface
- Real-time Prediction

## Technologies Used
- Python
- Django
- Scikit-learn
- Pandas
- NumPy
- NLP
- TF-IDF

## Project Structure
spam-detection-system/
├── classifier/
├── spam_detector/
├── templates/
├── manage.py
├── spam_model.pkl
└── tfidf_vectorizer.pkl

## How to Run
```bash
pip install -r requirements.txt
python manage.py runserver
