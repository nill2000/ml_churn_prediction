import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    precision_recall_curve,
    PrecisionRecallDisplay,
    roc_curve,
    RocCurveDisplay,
    auc,
)

def main():
    
    """
    get_dummies method changes anything non-int related to binary representation for data. drop_first drops the first column when analyzing the data. For example, since there are three subscriptions and the first one gets dropped, when shown premium and standard are 0, customer must have basic because of process of elimination.
    """
    
    # === Gathering and Fine-Tuning Data === START
    
    df = pd.read_csv("customer_churn.csv")
    print(df.isnull().sum())                #Check for Null Values
    print(df["Churn"].value_counts())       #Check if labels are balanced; 33900 Stayed and 30500 Churned
    df = pd.get_dummies(df, columns=["Subscription Type", "Contract Length"], drop_first=True) #Checks for non-int values to make classfication - turning into binary values
    df.drop_duplicates(inplace=True)        #Remove Dupes to Improve Data Accuracy
    print(df.columns)                       #Check new columns after getting dummies
    
    # === Gathering and Fine-Tuning Data === END
 
    # === Separate, Train, Test Data === START
    
    X = df[[ #Gather Important Columns for Data
     "Tenure", 
     "Usage Frequency", 
     "Support Calls", 
     "Payment Delay",
     "Subscription Type_Premium",
     "Subscription Type_Standard",
     "Contract Length_Monthly",
     "Contract Length_Quarterly",
     "Total Spend",
     "Last Interaction"]]
 
    y = df["Churn"] #The Labels
    
    xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=40)
    
    model = LogisticRegression()
    model.fit(xtrain, ytrain)
    
    ypreds = model.predict(xtest)
    
    # === Separate, Train, Test Data === END
    
    #Confusion Matrix Plot
    conf_matrix = confusion_matrix(ytest, ypreds, labels=model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=model.classes_)
    disp.plot()
    plt.title("Confusion Matrix Display")
    plt.show()
    
    #Recall Plot
    precision, recall, pr_thresholds = precision_recall_curve(ytest, ypreds)
    disp = PrecisionRecallDisplay(precision=precision, recall=recall)
    disp.plot()
    plt.title("Recall Display")
    plt.show()
    
    #ROC Plot
    fpr, tpr, roc_thresholds = roc_curve(ytest, ypreds)
    roc_auc = auc(fpr, tpr)
    disp = RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name="Estimate")
    disp.plot()
    plt.title("ROC Display")
    plt.show()
    
    #Get Features or Coefficients
    coef = model.coef_
    feature_names = X.columns
    importances = coef[0] #Returns a 2d Array so grab the first
    print(importances)
    
    plt.barh(feature_names, importances)
    plt.title("Feature Importances")
    plt.xlabel("Coeffecient Values")
    plt.axvline(0, linestyle="--")
    plt.tight_layout() #Shows Everything; No overflow
    plt.show()
    
    #Prediction Distribution
    sns.countplot(x=ypreds) #Input the name of data along x or y axis not the name
    plt.title("Churn Prediction Distribution")
    plt.xlabel("Churn Predictions (0=No 1=Yes)")
    plt.ylabel("Customer Count")
    plt.tight_layout()
    plt.show()
    
    churn_accuracy = accuracy_score(ytest, ypreds)
    churn_precision = precision_score(ytest, ypreds)
    churn_recallscore = recall_score(ytest, ypreds)
    churn_f1score = f1_score(ytest, ypreds)
    churn_class_report = classification_report(ytest, ypreds)
    churn_conf_matrix = confusion_matrix(ytest, ypreds)
    
    print(f"""
          Accuracy: {churn_accuracy}
          Precision: {churn_precision}
          Recall: {churn_recallscore}
          F1_Score: {churn_f1score}
          Confusion Matrix: \n{churn_conf_matrix}
          Classification Report: \n{churn_class_report}
          """)
    
    

if __name__ == "__main__":
    main()