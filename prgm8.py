import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split

dataset=load_iris()
model=SVC(kernel='linear')
X_train,X_test,y_train,y_test=train_test_split(dataset.data,dataset.target,test_size=0.2)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
acc=accuracy_score(y_test,y_pred)
print(acc)
print("y_test:", y_test)
print("y_pred:", y_pred)
cm=confusion_matrix(y_test,y_pred)
print(cm)
