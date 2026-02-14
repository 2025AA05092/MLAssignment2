# MLAssignment2
Machine Learning Assignment 2
a) Problem Statement: To determine the diagnosis whether the patient cannot sleep due to the Stress.
b) DataSet Description: The Dataset contains the details of the patients, we chose 14 features related to health and sleep to use for the prediction task of whether the stress is keeping the user to not be able to sleep. There are no missing values in the data. The pre-processing of the data is already done and assigned the class label values for each of different categories for each feature. The dataset is downloaded from the Kaggle Website. and filename is NPHA-doctor-visits. There are no attriutes that corresponds or give any specific personal information of any patient that has been recorded here.
Models Used and their metrics comprsion
|ML Model Name|Accuracy|AUC|Precision|Recall|F1|MCC|
|:------------|:-------|:--|:--------|:-----|:-|:--|
|Logistic Regression|0.7063|0.7221|0.3913|0.2432|0.3|0.1325|
|Decision Tree|0.7413|0.6577|0.5|0.1622|0.2449|0.1667|
|kNN|0.7063|0.6105|0.3529|0.1622|0.2222|0.079|
|Naïve Bayes|0.6503|0.6486|0.3617|0.4595|0.4048|0.1645|
|Random Forest(Ensemble)|0.7063|0.6583|0.3333|0.1351|0.1923|0.0583|
|XGBoost(Ensemble)|0.6783|0.6662|0.2857|0.1622|0.2069|0.0256|



