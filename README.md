# Network Intrusion Detection System Using KNN

## Results and Analysis

The KNN model achieved an accuracy score of 99.49% on the NSL-KDD dataset.

The confusion matrix shows that:

* 11,705 attack records were correctly identified.
* 13,363 normal traffic records were correctly classified.
* Only 68 attack records were misclassified as normal traffic.
* Only 59 normal records were incorrectly classified as attacks.

These results indicate that the model is highly effective in distinguishing malicious network activity from legitimate traffic.

From a cybersecurity perspective, minimizing False Negatives is critical because undetected attacks may lead to security incidents. The model demonstrated a strong attack detection capability with a very low number of missed attacks.

Although KNN is a relatively simple machine learning algorithm, the results show that distance-based classification can provide a solid foundation for building intrusion detection systems and understanding AI applications in cybersecurity.


## Overview

This project implements a simple Intrusion Detection System (IDS) using the K-Nearest Neighbors (KNN) algorithm. The model analyzes network traffic records and classifies them as either normal activity or potential cyber attacks.

The project uses the NSL-KDD dataset, a widely recognized benchmark dataset in cybersecurity research for evaluating intrusion detection techniques.

## Objectives

* Understand the fundamentals of machine learning in cybersecurity.
* Explore network traffic datasets used in intrusion detection research.
* Apply data preprocessing techniques to network security data.
* Train and evaluate a KNN classification model.
* Visualize attack patterns and model performance.

## Dataset

Dataset: NSL-KDD

The dataset contains network traffic features such as:

* Protocol Type
* Service
* Flag
* Source Bytes
* Destination Bytes
* Connection Statistics
* Traffic Behavior Metrics

For this project, the original attack categories are transformed into binary classes:

* Normal
* Attack

This approach simplifies the classification problem and focuses on detecting suspicious network activity.

## Project Workflow

1. Data Loading
2. Data Exploration and Visualization
3. Feature Encoding
4. Binary Classification Conversion
5. Train-Test Split
6. Feature Scaling
7. KNN Model Training
8. Performance Evaluation
9. Result Visualization

## Technologies

* Python
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn

## Visualizations

The project includes:

* Normal vs Attack Distribution
* Protocol Distribution
* Top Network Services
* Attack Category Distribution
* Correlation Heatmap
* KNN Accuracy Visualization
* Confusion Matrix

## Model

Algorithm:

K-Nearest Neighbors (KNN)

Configuration:

* K = 5
* StandardScaler for feature normalization
* 80% Training Data
* 20% Testing Data

## Results

The model successfully classifies network traffic into normal and attack categories.

Performance evaluation is conducted using:

* Accuracy Score
* Confusion Matrix

These metrics help assess the effectiveness of the intrusion detection system and identify potential false positives or false negatives.

## Cybersecurity Perspective

In a real-world Security Operations Center (SOC), intrusion detection systems play a critical role in identifying malicious network behavior.

Although KNN is a relatively simple machine learning algorithm, this project demonstrates the foundational concepts behind AI-driven threat detection and network anomaly analysis.

## Future Improvements

* Random Forest Intrusion Detection
* XGBoost-based Detection Model
* Deep Learning for Network Traffic Analysis
* Real-time Packet Analysis
* SIEM Integration
* AI-Assisted Security Monitoring

## Author

Pandu Satria
