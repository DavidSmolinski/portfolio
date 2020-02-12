
### **Django code for [this site](https://moresomervillehappinessapp.herokuapp.com/home)**
___
<br>
Changes that would have to be made for other people to make the site work:

1. Add the images. I removed them for Github.
2. Customize msh/settings.py
3. This version uses a pickle to run the machine learning model. This didn't work on Heroku. I hope to make pickles work in the future. In the ratings folder, I made these changes to avoid the pickle.
    - In views.py, I removed "model = load(r'ratings\static\ratings\happy_somerville.joblib')" from predict_happy_view. 
    - I added code from make_model.py to views.py in order to create the model.
