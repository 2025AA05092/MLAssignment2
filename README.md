# MLAssignment2  
Machine Learning Assignment 2  
a) Problem Statement: To determine the diagnosis whether the patient cannot sleep due to the Stress.  
b) DataSet Description: The Dataset contains the details of the patients, we chose 14 features related to health and sleep to use for the prediction task of whether the stress is keeping the user to not be able to sleep. There are no missing values in the data. The pre-processing of the data is already done and assigned the class label values for each of different categories for each feature. The dataset is downloaded from the Kaggle Website. and filename is NPHA-doctor-visits. There are no attriutes that corresponds or give any specific personal information of any patient that has been recorded here.  
Models Used and their metrics comprsion  
|ML Model Name|Accuracy|AUC|Precision|Recall|F1|MCC|
|:------------|:-------|:--|:--------|:-----|:-|:--|
|Logistic Regression|0.7413|0.7323|0.5495|0.7413|0.6311|0|
|Decision Tree|0.7413|0.6577|0.6952|0.7413|0.6889|0.1667|
|kNN|0.7273|0.6364|0.5467|0.7273|0.6242|-0.0704|
|Naïve Bayes|0.6503|0.6486|0.6804|0.6503|0.6625|0.1645|
|Random Forest(Ensemble)|0.7063|0.6583|0.6422|0.7063|0.658|0.0583|
|XGBoost(Ensemble)|0.6783|0.6662|0.6268|0.6783|0.6452|0.0256|

|ML Model Name|Observaton about Model Performance|
|:------------|:---------------------------------|
|Logistic Regression|The model achieves highest accuracy, highest AUC indicating it is good at detectig the positive cases, but MCC of 0 means its clssification results are no better than random guessing|
|Decision Tree|The model achieves highest accuracy, highest precision, MCC which indictes model is more balanced at correctly identifying positive and negative classes|
|kNN|The model has good accuracy, but the negative MCC which indicates model predictions are worse than random guessing|
|Naïve Bayes|The model has relatively less accuracy, but the precision, MCC score indicates the high chance that the predicted positive result is correct|
|Random Forest(Ensemble)|The model performance metrics are relatively good, but the MCC score indicates weak coorelation for the given dataset|
|XGBoost(Ensemble)|The model metrics shows the inefficient complexity and low predictive value for the given dataset|
