import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve,f1_score, precision_score, recall_score,precision_score,recall_score,recall_score


data={
    'hours_studied':[1,2,3,4,5,6,7,8,9,10],
    'previous_score':[50,55,60,65,70,75,80,85,90,95],
    'passed':[0,0,0,0,1,1,1,1,1,1]
}
df = pd.DataFrame(data)

x=df[['hours_studied','previous_score']]
y=df['passed']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
y_pred_proba=model.predict_proba(x_test)[:,1]

conf_matrix=(confusion_matrix(y_test,y_pred))
acc=accuracy_score(y_test,y_pred)
precision =precision_score(y_test,y_pred)
rec=recall_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
roc_auc=roc_auc_score(y_test,y_pred)
print(f"confusion matrix:\n{conf_matrix}")
print(f"accuracy:{acc}")
print(f"precision:{precision}")
print(f"recall:{rec}")
print(f"f1:{f1}")
print(f"roc_auc:{roc_auc}")

fpr,tpr,threshold=roc_curve(y_test,y_pred)
plt.plot(fpr,tpr,label=f'AUC={roc_auc:.2f}')
plt.plot([0,1],[0,1],'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title("Roc Curve")
plt.legend()
plt.show()