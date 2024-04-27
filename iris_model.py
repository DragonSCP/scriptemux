import sys
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib  # Usado para salvar e carregar o modelo

# Carregar e preparar os dados
data = load_iris()
X = data['data']
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinar o modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
joblib.dump(model, 'iris_model.pkl')  # Salvar o modelo

# Predizer a partir de inputs
def predict(features):
    model_loaded = joblib.load('iris_model.pkl')
    prediction = model_loaded.predict([features])
    return data['target_names'][prediction[0]]

if __name__ == '__main__':
    input_features = np.array(sys.argv[1:5], dtype=np.float64)  # Converter argumentos em array de floats
    result = predict(input_features)
    print("Predicted species:", result)

