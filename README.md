🌸 Iris Flower Prediction using SVM & Streamlit

A beginner-friendly machine learning project that predicts the species of an Iris flower using a Support Vector Machine (SVM) classification model and provides an interactive web interface built with Streamlit.

This project was created primarily to experiment with Streamlit deployment and machine learning model integration using the classic Iris dataset.

---

📌 Project Overview

The Iris Flower Prediction application takes four measurements of an Iris flower:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Using these measurements, a trained Support Vector Machine (SVM) model predicts the flower species.

The model can classify an Iris flower into one of three species:

- 🌱 Iris Setosa
- 🌿 Iris Versicolor
- 🌺 Iris Virginica

The trained model is saved as a ".pkl" file and loaded into the Streamlit application for making predictions.

---

🎯 Objectives

The main objectives of this project are:

- Understand the basic workflow of a machine learning classification project.
- Experiment with the Support Vector Machine (SVM) algorithm.
- Work with the classic Iris dataset.
- Save and load a trained machine learning model using Joblib.
- Build an interactive ML application using Streamlit.
- Understand how a trained ML model can be integrated into a web application.

---

🧠 Machine Learning Algorithm

Support Vector Machine (SVM)

Support Vector Machine is a supervised machine learning algorithm commonly used for classification and regression problems.

In this project, SVM is used to classify Iris flowers based on their four numerical measurements.

The model learns the relationship between the flower measurements and their corresponding species during training.

After training, the model can receive new measurements and predict the corresponding Iris species.

---

📊 Dataset

This project uses the Iris Flower Dataset.

The dataset contains measurements of Iris flowers belonging to three different species.

Features

Feature| Description
SepalLengthCm| Length of the sepal in centimeters
SepalWidthCm| Width of the sepal in centimeters
PetalLengthCm| Length of the petal in centimeters
PetalWidthCm| Width of the petal in centimeters

Target

The target variable is:

- "Iris-setosa"
- "Iris-versicolor"
- "Iris-virginica"

The dataset is stored in:

Iris.csv

---

🖥️ Streamlit Application

The Streamlit application provides an interactive interface where users can enter flower measurements using sliders.

The application accepts:

Sepal Length
Sepal Width
Petal Length
Petal Width

After clicking:

🔮 Predict Iris Flower

the trained SVM model predicts the flower species and displays the result.

Example:

Predicted Flower: Setosa

---

🔄 Project Workflow

                Iris Dataset
                     │
                     ▼
             Data Preparation
                     │
                     ▼
             Train SVM Model
                     │
                     ▼
              Save Model
          (svm_model1.pkl)
                     │
                     ▼
          Load Model in Streamlit
                     │
                     ▼
        User Enters Flower Features
                     │
                     ▼
             SVM Prediction
                     │
                     ▼
          Predicted Iris Species

---

📁 Project Structure

iris-flower-streamlit-main/
│
├── Iris.csv
│
├── SVM (1).ipynb
│
├── main.py
│
├── svm_model1.pkl
│
└── README.md

File Description

"Iris.csv"

Contains the Iris dataset used for the machine learning project.

"SVM (1).ipynb"

Jupyter Notebook containing the SVM model development/training workflow.

"main.py"

The Streamlit application that loads the trained model and provides the prediction interface.

"svm_model1.pkl"

Serialized trained SVM model used by the Streamlit application.

"README.md"

Project documentation.

---

🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

⚙️ Installation

1. Clone the repository

git clone <your-repository-url>

2. Navigate to the project directory

cd iris-flower-streamlit-main

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

5. Install dependencies

pip install streamlit pandas scikit-learn joblib

---

▶️ Run the Application

Start the Streamlit application using:

streamlit run main.py

After running the command, Streamlit will provide a local URL where the application can be opened in a browser.

---

🧪 Making Predictions

1. Open the Streamlit application.
2. Adjust the four flower measurements using the sliders.
3. Click 🔮 Predict Iris Flower.
4. The application sends the entered values to the trained SVM model.
5. The predicted Iris species is displayed on the screen.

---

💡 Example Input

Sepal Length : 5.1 cm
Sepal Width  : 3.5 cm
Petal Length : 1.4 cm
Petal Width  : 0.2 cm

Example prediction:

Predicted Flower: Setosa

---

📚 What I Learned

Through this project, I practiced:

- Building a basic machine learning classification workflow.
- Using SVM for classification.
- Working with the Iris dataset.
- Loading a trained ML model using Joblib.
- Passing user input to a machine learning model.
- Creating an interactive ML interface with Streamlit.
- Connecting a machine learning model with a simple web application.

---

🚀 Future Improvements

Some possible improvements for this project are:

- Add model accuracy and evaluation metrics.
- Display the prediction probability/confidence.
- Add data visualization using charts.
- Add an exploratory data analysis section.
- Add multiple machine learning models for comparison.
- Add a confusion matrix and classification report.
- Improve the UI with custom CSS.
- Add model performance information to the application.
- Deploy the application online using Streamlit Community Cloud or another hosting platform.
- Add automated dependency management using "requirements.txt".

---

📈 Future ML Workflow

A more production-oriented version of this project could follow:

Data Collection
      ↓
Data Validation
      ↓
Exploratory Data Analysis
      ↓
Train/Test Split
      ↓
Preprocessing
      ↓
Model Training
      ↓
Hyperparameter Tuning
      ↓
Model Evaluation
      ↓
Model Selection
      ↓
Save Model
      ↓
Streamlit Application
      ↓
Deployment
      ↓
Monitoring

---

⭐ Project Purpose

This repository was created as an experimental machine learning and Streamlit project to understand how a trained machine learning model can be integrated into an interactive application.

Although the Iris dataset is simple, the project provides a foundation for building and deploying more advanced machine learning applications.

---

👨‍💻 Author

Sri Vardhan Jilla

BTech CSE Student | AI & Machine Learning Enthusiast

---

📄 License

This project is intended for educational and experimentation purposes.
