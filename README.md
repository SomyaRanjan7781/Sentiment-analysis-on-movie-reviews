# Sentiment-analysis-on-movie-reviews

Test my project here:
https://huggingface.co/spaces/somya-27-04-03/Sentiment-analyzer-on-movie-reviews
PROJECT TITLE: Sentiment Analysis on Movie Reviews

PROJECT OVERVIEW:
This project focuses on performing sentiment analysis on movie reviews using machine learning.
It classifies movie reviews into two categories: Positive or Negative sentiment.

The aim is to help understand public opinion on movies through automatic analysis of reviews,
providing valuable insights for studios, filmmakers, and review platforms.


FUNCTIONALITY:
✓ Accepts a movie review as input
✓ Predicts whether the sentiment is Positive or Negative
✓ Trained using Logistic Regression with TF-IDF vectorization
✓ Evaluated using accuracy and F1-score


HOW IT WORKS:
1. Loads and processes the dataset containing movie reviews and corresponding sentiment labels.
2. Splits the data into training and testing sets.
3. Applies TF-IDF vectorization to convert text data into numerical form.
4. Trains a Logistic Regression model.
5. Evaluates the model on unseen data using metrics like accuracy and F1-score.
6. (Optional) Launches a simple UI using Gradio for interactive testing or deployment.

REQUIREMENTS:
• Python 3.7+
• pandas
• scikit-learn
• gradio (optional, for UI)

Install requirements using:
pip install pandas scikit-learn gradio


DATA FORMAT:
The dataset (CSV format) should contain two columns:
- 'review' : The review text
- 'label' : 1 for Positive, 0 for Negative


DEPLOYMENT:
I've deployed this project on Hugging Face Spaces using Gradio.
Make sure to include:
• app.py
• requirements.txt
• The dataset file (if needed)

EXAMPLE USAGE:
Input: "I absolutely loved this movie. The story was gripping and performances were top-notch!"
Output: Positive 😊
Input: "The movie was too slow and boring. I expected much better."
Output: Negative 😞
AUTHOR:
SOMYA RANJAN MAHAPATRA

