import streamlit as slt
import pandas as pd
import pickle
import os
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, 
    f1_score, roc_auc_score, matthews_corrcoef
)
import seaborn as sns
import matplotlib.pyplot as plt

slt.set_page_config(page_title="Pickle Model Evaluator", layout="wide")
slt.title("Model Evaluation Dashboard (Pickle)")

# 1. Dataset Upload
slt.sidebar.header("1. Upload Test Data")
uploaded_file = slt.sidebar.file_uploader("Upload your test CSV", type=['csv'])

#1.1 Dataset Download
if uploaded_file is not None:
    # Read the file content for the download button
    file_bytes = uploaded_file.getvalue()
    
    slt.sidebar.download_button(
        label="Download Uploaded CSV",
        data=file_bytes,
        file_name=f"re_downloaded_{uploaded_file.name}",
        mime="text/csv"
    )

# 2. Model Selection
model_folder = "model"
# Filter for .pkl files specifically
model_files = [f for f in os.listdir(model_folder) if f.endswith('.pkl')]

slt.sidebar.header("2. Select Model")
selected_model_name = slt.sidebar.selectbox("Choose a pickle model", model_files)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    slt.write("### Test Data Preview", df.head())
    
    target_col = slt.selectbox("Select the target column", df.columns, index=len(df.columns)-1)
    X_test = df.drop(columns=['Stress Keeps Patient from Sleeping'])
    y_test = df['Stress Keeps Patient from Sleeping']

    if slt.button("Evaluate Model"):
        try:
            # Load selected model using Pickle
            model_path = os.path.join(model_folder, selected_model_name)
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            
            # Predictions
            y_pred = model.predict(X_test)
            try:
              y_probs = model.predict_proba(X_test)[:, 1]
            except:
              y_probs = y_pred
            
            # 3. & 4. Display Metrics & Visuals
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted')
            recall = recall_score(y_test, y_pred, average='weighted')
            f1 = f1_score(y_test, y_pred, average='weighted')
            mcc = matthews_corrcoef(y_test, y_pred)
            try:
              auc = roc_auc_score(y_test, y_probs)
            except:
              auc = 0.0

            slt.subheader("Key Performance Indicators")
            col1, col2, col3 = slt.columns(3)
            col4, col5, col6 = slt.columns(3)

            col1.metric("Accuracy", f"{accuracy:.4f}")
            col2.metric("AUC", f"{auc:.4f}")
            col3.metric("Precision", f"{precision:.4f}")
            col4.metric("Recall", f"{recall:.4f}")
            col5.metric("F1 Score", f"{f1:.4f}")
            col6.metric("MCC", f"{mcc:.4f}")
          
            col1, col2 = slt.columns(2)       
            with col1:
                slt.write("#### Confusion Matrix")
                fig, ax = plt.subplots()
                sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Greens', ax=ax)
                slt.pyplot(fig)
                
        except Exception as e:
            slt.error(f"Error: {e}. Ensure the model and test data features match.")
else:
    slt.info("Upload a test CSV file to begin.")
