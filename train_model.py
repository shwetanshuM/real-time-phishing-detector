import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('phishing.csv')
print("\nDataset Columns:\n")
print(df.columns.tolist())
selected_features = [
    'having_IPhaving_IP_Address',
    'URLURL_Length',
    'Shortining_Service',
    'having_At_Symbol',
    'Prefix_Suffix',
    'having_Sub_Domain',
    'SSLfinal_State'
]

X = df[selected_features]
y = df['Result'].map({-1: 0, 1: 1})
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =========================
# TRAIN MODEL
# =========================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)
print("\naccuracy:", accuracy)

with open('backend/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('backend/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("\nmodel saved")