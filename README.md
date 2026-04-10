# IoT Network Attack Detection using BoT-IoT Dataset

## Project Overview

This project focuses on analyzing IoT network traffic and detecting cyber attacks using data science and machine learning techniques.

It is divided into two main parts:

1. **Data Analysis & Visualization**
2. **Machine Learning Model for Attack Detection**

---

# PART 1: Data Analysis & Visualization

## Aim

To analyze and visualize the BoT-IoT dataset for identifying different types of cyber attacks.

## Objective

* Understand network traffic patterns
* Identify attack distribution
* Visualize attack behavior

## Dataset

* **Name:** BoT-IoT Dataset
* **Source:** UNSW Canberra
* **Records:** ~3.6 Million
* **Format:** CSV
* **Features:** 20

## Types of Attacks

* DDoS
* DoS
* Reconnaissance
* Theft
* Normal Traffic

## Tools Used

* Python
* Pandas
* Matplotlib
* Seaborn

## Methodology

1. Import Libraries
   <img width="979" height="208" alt="image" src="https://github.com/user-attachments/assets/53b08864-c264-41aa-bdcc-fd7d8bff871e" />
3. Load
   <img width="979" height="440" alt="image" src="https://github.com/user-attachments/assets/be8fc8b7-2f41-4cf2-8880-e07a6d9d4e45" />
5. Data Understanding
   <img width="979" height="303" alt="image" src="https://github.com/user-attachments/assets/a5f2a329-1870-43f3-b4e9-930ce8eef208" />
7. Analyze Attack Distribution
   <img width="979" height="120" alt="image" src="https://github.com/user-attachments/assets/3cd99a66-7b31-49e1-91b0-94a3d53ae879" />
9. Analyze Attack Categories
    <img width="958" height="278" alt="image" src="https://github.com/user-attachments/assets/81ef4b5f-39b9-432b-9b94-ea9d6d16ebbb" />
11. Analyze Protocol Distribution
    <img width="920" height="249" alt="image" src="https://github.com/user-attachments/assets/3c7de4f4-1aac-4bf7-b152-d5c78bd96b07" />
13. Visualization
    <img width="968" height="185" alt="image" src="https://github.com/user-attachments/assets/85cb94e1-7410-49f3-a9b3-1f6a7e2e2071" />
    <img width="979" height="841" alt="image" src="https://github.com/user-attachments/assets/ab448811-fe8e-4f3e-89a0-3f16461404c5" />
14. Types of Attacks
    <img width="979" height="200" alt="image" src="https://github.com/user-attachments/assets/41698584-8708-4598-8220-c2bd68a7e41f" />
    <img width="979" height="830" alt="image" src="https://github.com/user-attachments/assets/c9bd7053-7a59-494e-bffc-0fc4a6b23800" />

## Key Findings

* Attack records: **3,668,045**
* Normal records: **477**
* Dataset is **highly imbalanced**
* Most common attacks:

  * DDoS (Highest)
  * DoS (Second)
* Most used protocols:

  * UDP (Highest)
  * TCP (Second)

## Insights

* IoT networks are heavily targeted by attacks
* DDoS dominates traffic
* Visualization confirms attack-heavy dataset

---

# PART 2: Machine Learning Model

## Aim

To detect IoT network attacks using a **Random Forest Classifier**

## Objective

* Classify network traffic as:

  * Attack (1)
  * Normal (0)

## Tools & Technologies

* Python
* Pandas
* NumPy
* Scikit-learn

## Methodology

1. Import Libraries
2. Load Dataset
3. Data Preprocessing

   * Remove missing values
   * Select numerical features
   * Drop irrelevant columns
4. Train-Test Split
5. Model Training (Random Forest)
6. Prediction & Evaluation

## Results

* Model Accuracy: **~99.99%**
* Successfully detects attack traffic

## Analysis

* Dataset is highly imbalanced
* High accuracy due to dominance of attack data
* Only numerical features used

---

# Project Structure

```
📂 IoT-Attack-Detection
 ┣ 📜 analyze.py        # Data analysis & visualization
 ┣ 📜 project.py        # ML model
 ┣ 📜 README.md
```

---

# Dataset Note

Due to large size, dataset is not included.

Download from:
https://research.unsw.edu.au/projects/bot-iot-dataset

---

# Conclusion

* IoT networks are highly vulnerable to cyber attacks
* DDoS and DoS attacks dominate
* Machine learning can effectively detect attacks
* Dataset imbalance must be handled for real-world use

---

# Authors

* Vishnu Irappa Sangammanavar - 23BCE10569
* N Bharath -23BCE10570
* Tejas Tekade -23BCE10580
* Advay Singh -23BCE10596
* Adarsh Agrawal -23BCE10638
* Ayasha Mishra -23BCE10798

---
