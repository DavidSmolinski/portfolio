# This makes the model pickle file for making predictions. I ran this here to 
# use the project's sklearn version and avoid this error: 
# "ValueError: Buffer dtype mismatch, expected 'ITYPE_t' but got 'long long'"
# I used a different file to find the model params.

import pandas as pd
import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from joblib import dump, load

df = pd.read_csv(r'https://archive.ics.uci.edu/ml/machine-learning-databases/00479/' + 
                 r'SomervilleHappinessSurvey2015.csv', 
                 encoding="'UTF-16'")
df = df.rename(columns={'D':'happy', 'X1':'info', 'X2':'housing', 'X3':'schools', 
                        'X4':'police', 'X5':'streets', 'X6':'events',})
feature_cols = list(df.columns)
feature_cols.remove('happy')
x = df[feature_cols] # Features (inputs)
y = df.happy # Response (prediction, output) 
model = KNeighborsClassifier(n_neighbors=4)
model.fit(x,y)

# save the pickle file    
dump(model, r'ratings\static\ratings\happy_somerville.joblib') 
# with open('r'ratings\static\ratings\happy_somerville.pkl', 'wb') as f:
#     pickle.dump(model, f)


# test the pickle file 
   
# with open('r'ratings\static\ratings\happy_somerville.pkl', 'rb') as f:
#     model = pickle.load(f)    
model = load(r'ratings\static\ratings\happy_somerville.joblib') 

unit = {'info': '1', 'housing': '1', 'schools': '4', 'police': '5', 'streets': '5', 'events': '5'}
unit = unit.values()
unit = [int(e) for e in unit]
unit = np.array(unit).reshape(1,-1)
y_pred_prob = model.predict_proba(unit)
print(f'{y_pred_prob[0][1]*100:.2f}')  
