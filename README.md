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

|ML Model Name|Observaton about Model Performance|
|:------------|:---------------------------------|
|Logistic Regression|The model has the best ability to distinguish between classes across various thresholds. It maintains a relatively balanced performance across other metrics like accuracy, AUC etc|
|Decision Tree|TheDecision Tree achieves the highest accuracy of 0.7413 and highest precision of 0.5 which indicates it is reliable to make correct positive predictions, but low recall also poses it may not capture all positive cases|
|kNN|it matches the accuracy of Logistic Regression and Random Forest (0.7063), it lacks a standout strength. Its AUC and MCC are relatively low, suggesting it is less effective at handling class imbalances or distinguishing between classes than Logistic Regression.|
|Naïve Bayes|This model hs the highest Recall (0.4595) and highest F1-score (0.4048). It is the most effective at identifying positive cases, though it has the lowest overall accuracy (0.6503), indicating a higher rate of false positives.|
|Random Forest(Ensemble)| Despite being an ensemble method, it underperforms in this specific dataset, yielding the lowest Recall (0.1351). It struggles significantly to capture positive instances.|
|XGBoost(Ensemble)|This model shows the weakest performance in MCC (0.0256) and Precision (0.2857). An MCC close to zero suggests its predictions are not much better than random guessing for this particular problem.|



