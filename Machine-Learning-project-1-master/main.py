from joblib import dump, load
import numpy as np
model,my_pipeline = load('Dragon.joblib')
a=int(input("Enter the CRIM: "e=int(input("Enter the NOX: "))
f=int(input("Enter the RM: "))
g=int(input("Enter the AGE: "))
h=int(input("Enter the DIS: "))
i=int(input("Enter the RAD: "))
j=int(input("Enter the TAX: "))
k=int(input("Enter the PTRATIO: "))
l=int(input("Enter the B: "))


a=np.array([[a,b,c,d,e,f,g,h,i,j,k,l,m]])
X_test_prepared = my_pipeline.transform(a)
final_predictions = model.predict(X_test_prepared)
print("The price of the house is expected to be: ",int(final_predictions))