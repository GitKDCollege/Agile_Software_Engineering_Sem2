#Using the Naive Bayes Algorithm
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("./Data/diabetes.csv")
df.head()
x=df.drop('diabetes',axis=1)
y=df['diabetes']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)
model=GaussianNB()
model.fit(x_train,y_train)
uinp_glucose=int(input("Enter the Blood Glucose Level: "))
uinp_bloodpressure=int(input("Enter the Pressure: "))
dict={'glucose':0, 'bloodpressure':0}
dict['glucose']=(uinp_glucose)
dict['bloodpressure']=(uinp_bloodpressure)
x_test=pd.DataFrame(data=dict,index=[0])
y_pred = model.predict(x_test)
print(f"Given your Blood Glucose Level {uinp_glucose} and Blood Pressure {uinp_bloodpressure}",end=' ')
if(y_pred):
    print(": You are Diabetic")
else:
    print(": You are not Diabetic")