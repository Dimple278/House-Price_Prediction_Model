from joblib import dump, load
import numpy as np
model,my_pipeline = load('Dragon.joblib')
a=int(input(a,b,c,d,e,f,g,h,i,j,k,l,m]])
X_test_prepared = my_pipeline.transform(a)
final_predictions = model.predict(X_test_prepared)
print("The price of the house is expected to be: ",int(final_predictions))