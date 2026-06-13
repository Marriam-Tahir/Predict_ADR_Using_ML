# Predict_ADR_Using_ML
A Machine Learning system for predicting Adverse Drug Reactions (ADRs) using the official FDA FAERS dataset to improve post-marketing drug safety surveillance.

## 📌 Project Overview
This repository contains my Bachelor of Science in Information Technology (BS-IT) Final Year Project. The objective of this project is to build an intelligent, data-driven application capable of predicting potential adverse reactions based on drug combinations and patient profiles. 

By extracting and preprocessing real-world, high-stakes medical data, this system provides healthcare professionals and pharmaceutical researchers with an interactive interface to evaluate drug safety signals before clinical issues arise.


## 📊 Dataset: FDA FAERS
This project utilizes data from the **FDA Adverse Event Reporting System (FAERS)**, a public repository containing millions of adverse event and medication error reports.

* **Source:** OpenFDA / FAERS API extracts
* **Format:** Raw data was parsed and engineered from complex JSON structures.
* **Data Engineering Challenge:** Designed automated scripts to dynamically load and parse JSON files featuring thousands of unique features (drug names and clinical reactions) without hardcoding values.

## 🤖 Machine Learning Models & Use Cases
To find the most accurate predictor for Adverse Drug Reactions, this project implements and compares **six distinct machine learning models**. Each architecture was rigorously trained and evaluated using metrics like Accuracy, Precision, Recall, and F1-Score:

| Model Name | Description / Use Case in Project |


| **Gaussian Naive Bayes** | A probabilistic classifier used for fast baseline predictions, assuming independence among the complex FDA FAERS features. |


| **Logistic Regression** | Used as a fundamental statistical baseline model to evaluate linear decision boundaries within the dataset. 


| **XGBoost** | A high-performance gradient-boosted framework optimized to handle the heavily imbalanced nature of adverse event reports. |


| **Decision Tree** | Implemented to provide a highly interpretable, rule-based logic mapping out the exact decision paths for adverse reactions. |


| **Random Forest** | An ensemble tree-based algorithm used to maximize prediction stability and calculate feature importance scores across drug attributes. |


| **Multi-Layer Perceptron (MLP)** | A feedforward Artificial Neural Network (ANN) used to capture deep, non-linear hidden relationships within patient and drug data. |


## 💻 Web Deployment & Frontend Architecture
* **Frontend Framework:** Built entirely with **Streamlit** to offer an intuitive, user-friendly dashboard for real-time predictions.
* **Dynamic UI Rendering:** Implemented optimal file handling where the web frontend dynamically reads data from backend JSON arrays to populate user dropdowns seamlessly—efficiently managing thousands of data points.


## 📁 Repository Structure
To navigate this project, files are structured into separate directories as follows:

 assets/
 ──>(Contains UI configurations, design elements, and parsed JSON files for the dropdown lists)


 data/
 ──> (Contains subsets of preprocessed FDA FAERS datasets and JSON files)

 
 Predict ADR using ML.ipynb
 ──> (The main Jupyter Notebook detailing the complete ML engineering pipeline)

 
├── app.py 
──>(The primary Streamlit web application deployment file)


└── README.md
 ──> (Project introductory documentation)


├── requirements.txt
    ──>(Required Libraries and environment used )
