import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

#Load dataset
df = pd.read_csv(
    "C:/Users/vishn/OneDrive/Documents/FDS/UNSW_2018_IoT_Botnet_Final_10_Best.csv",
    sep=';',
    low_memory=False
)

#Clean data
df = df.dropna()

#Reduce size (IMPORTANT for speed)
df = df.sample(50000, random_state=42)

#Encode categorical data
le = LabelEncoder()

df['proto'] = le.fit_transform(df['proto'])
df['category'] = le.fit_transform(df['category'])
df['subcategory'] = le.fit_transform(df['subcategory'])

#Keep only numeric columns
X = df.select_dtypes(include=['int64', 'float64'])

#Remove target from features
X = X.drop(['attack'], axis=1)

#Target
y = df['attack']

#Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

#Predict
y_pred = model.predict(X_test)

#Accuracy
print("Model Accuracy:", accuracy_score(y_test, y_pred))


#Prediction function
def predict_attack(sample):
    result = model.predict([sample])
    if result[0] == 1:
        return "⚠️ Attack Detected"
    else:
        return "✅ Normal Traffic"


#Test prediction
sample = X_test.iloc[0]
print("Sample Prediction:", predict_attack(sample))
