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
- Precision: Of the people "predicted" to churn, how many did? (TP + FP)
- Recall: Of "all" the people who churned, how many were predicted or caught? (TP + FN)

![Screenshot 2025-04-21 at 11 16 06 AM](https://github.com/user-attachments/assets/b1cdf9f9-a7b5-43eb-a490-e091597868e4)

## ROC Plot:
- The graph shows the a FP vs TP as thresholds change
- The auc is 0.8, meaning there is an 80% chance that the model will choose the positive to be selected than the negative
![Screenshot 2025-04-21 at 11 16 19 AM](https://github.com/user-attachments/assets/26aece05-1b97-4f4d-8950-86fc66d35ff8)

## Features Plot:
![Screenshot 2025-04-21 at 11 16 57 AM](https://github.com/user-attachments/assets/fbb480c8-7115-4a3c-a068-b6f2710854c3)

## Prediction Distribution:
![Screenshot 2025-04-21 at 11 17 11 AM](https://github.com/user-attachments/assets/fba1fe02-da46-4097-a5d9-309e69e6e424)
