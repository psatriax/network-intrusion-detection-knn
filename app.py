import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset & Manual Name Column
columns = [
    'duration',
    'protocol_type',
    'service',
    'flag',
    'src_bytes',
    'dst_bytes',
    'land',
    'wrong_fragment',
    'urgent',
    'hot',
    'num_failed_logins',
    'logged_in',
    'num_compromised',
    'root_shell',
    'su_attempted',
    'num_root',
    'num_file_creations',
    'num_shells',
    'num_access_files',
    'num_outbound_cmds',
    'is_host_login',
    'is_guest_login',
    'count',
    'srv_count',
    'serror_rate',
    'srv_serror_rate',
    'rerror_rate',
    'srv_rerror_rate',
    'same_srv_rate',
    'diff_srv_rate',
    'srv_diff_host_rate',
    'dst_host_count',
    'dst_host_srv_count',
    'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate',
    'dst_host_srv_serror_rate',
    'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate',
    'label',
    'difficulty'
]

df = pd.read_csv(
    'network-intrusion-detection-knn/KDDTrain+.txt',
    header=None,
    names=columns
)

print(df.head())

# Backup dataframe sebelum encoding
raw_df = df.copy()

# Raw Protocol Distribution
raw_df['protocol_type'].value_counts().plot(kind='bar')
plt.title("Raw Protocol Distribution")
plt.xlabel("Protocol")
plt.ylabel("Count")
plt.show()

# Preprocessing
encoder = LabelEncoder()

df['protocol_type'] = encoder.fit_transform(df['protocol_type'])
df['service'] = encoder.fit_transform(df['service'])
df['flag'] = encoder.fit_transform(df['flag'])

# Binary Classification
df['label'] = df['label'].apply(
    lambda x: 'normal' if x == 'normal' else 'attack'
)

# Divide Feature & Label
X = df.drop(
    ['label', 'difficulty'],
    axis=1
)

y = df['label']

# Splitting Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Scaler
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Training Data
model = KNeighborsClassifier(n_neighbors=5)

model.fit(
    X_train,
    y_train
)

# Evaluation
pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

# Visualization

# NORMAL VS ATTACK
df['label'].value_counts().plot(
    kind='bar'
)

plt.title("Normal vs Attack Traffic")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()

# PROTOCOL TYPE (encoded)
df['protocol_type'].value_counts().plot(
    kind='bar'
)

plt.title("Protocol Distribution")
plt.xlabel("Protocol")
plt.ylabel("Count")
plt.show()

# TOP SERVICE
top_service = df['service'].value_counts().head(10)

top_service.plot(
    kind='bar'
)

plt.title("Top 10 Services")
plt.xlabel("Service")
plt.ylabel("Count")
plt.show()

# TOP ATTACK
df['label'].value_counts().head(10).plot(
    kind='bar'
)

plt.title("Top Attack Categories")
plt.xlabel("Attack Type")
plt.ylabel("Count")
plt.show()

# Heatmap Correlation
plt.figure(figsize=(12, 8))

sns.heatmap(
    df.select_dtypes(include=['int64', 'float64']).corr(),
    cmap='coolwarm'
)

plt.title("Feature Correlation Matrix")
plt.show()

# Accuracy Score Visual
acc = accuracy_score(
    y_test,
    pred
)

plt.bar(
    ['Accuracy'],
    [acc * 100]
)

plt.ylabel("Percentage")
plt.title("KNN Accuracy")
plt.show()

# Confusion Matrix
cm = confusion_matrix(
    y_test,
    pred
)

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    xticklabels=['Attack', 'Normal'],
    yticklabels=['Attack', 'Normal']
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()