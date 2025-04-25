# Project Overview:
- Predict customer churn rates using logistic regression based on real world data

## Confusion Matrix:
- The confusion matrix graph shows the distribution of TP, TN, FP, and FN 
- TN - 5457, TP - 4991, FP - 1314, FN - 1113
- Meaning:
  - 5457 were correctly predicted to churn and 4991 were correctly predicted to not churn
  - 1314 were predicted to churn but stayed and 1113 were predicted to stay but churned
  
![Screenshot 2025-04-21 at 11 15 49 AM](https://github.com/user-attachments/assets/2e7fc872-c71d-408e-a2f6-3d8dc48d82e4)

## Recall Plot:
- The graph shows a recall vs precision graph as thresholds changes
- Precision: Of the people "predicted" to churn, how many did? TP / (TP + FP)
- Recall: Of "all" the people who churned, how many were predicted or caught? TP / (TP + FN)
- Precision Scenario: You are a doctor and have 100 total patients.  You diagnose that 3 people are sick but only 2 are actually sick; 2/3 = 66% precision. Precision is the sick people out of "all sick people you chose"
- Recall Scenario: Same scenario as previous. You diagnose that 2 people are sick but 5 are actually sick in the 100. 2/5 = 40% recall. Recall is the sick people out of "all the sick people in the group". Precision in this case is 100% because you chose 2 people and those 2 are sick 2/2 = 100%

![Screenshot 2025-04-21 at 11 16 06 AM](https://github.com/user-attachments/assets/b1cdf9f9-a7b5-43eb-a490-e091597868e4)

## ROC Plot:
- The graph shows the a FP vs TP as thresholds change
- The auc is 0.8, meaning there is an 80% chance that the model will choose the positive to be selected than the negative
![Screenshot 2025-04-21 at 11 16 19 AM](https://github.com/user-attachments/assets/26aece05-1b97-4f4d-8950-86fc66d35ff8)

## Features Plot:
- Graph shows which features contributed to deciding churners or non-churners
- Those with monthly contract lengths, payment lengths, and support calls the most tended to churn
- Those with standard subscription, premium subscription, and usage frequency tended to not churn
  
![Screenshot 2025-04-21 at 11 16 57 AM](https://github.com/user-attachments/assets/fbb480c8-7115-4a3c-a068-b6f2710854c3)

## Prediction Distribution:
- Graph shows the amount of churners and non-churners to check if there is a balance
![Screenshot 2025-04-21 at 11 17 11 AM](https://github.com/user-attachments/assets/fba1fe02-da46-4097-a5d9-309e69e6e424)

## Percent Summary:
- Accuracy: 81.1%
- Precision: 79.2%
- Recall: 81.8%
- F1 Score: 80.4%
  
![Screenshot 2025-04-25 at 11 56 18 AM](https://github.com/user-attachments/assets/1bbd40f6-5cc4-43e7-8a33-04818674b2b6)
