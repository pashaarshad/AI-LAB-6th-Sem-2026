import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("Iris.csv")

x = data.iloc[:,1:-1].values
y = data.iloc[:,-1].values

x_train,x_test,y_train,y_test = train_test_split(x,y)

model = KNeighborsClassifier()

model.fit(x_train,y_train)

pred = model.predict(x_test)

print("Accuracy : ",accuracy_score(pred,y_test))


