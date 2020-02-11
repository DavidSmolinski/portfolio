from django.shortcuts import render

import pickle
import numpy as np
from joblib import load

from .forms import (Survey_Form,
                    Predict_Survey_Form)
from .models import Rating


# not a view
def get_client_ip(request):
    try:
        # ip addresses: 'client,proxy1,proxy2'
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ''
    return ip


def home_view(request):
    return render(request, "ratings/home.html")


def submit_happiness(request):
    form = Survey_Form(request.POST or None)
    ip = str(get_client_ip(request))
    saved_ip_query = Rating.objects.filter(ip=ip)
    message = False
    if saved_ip_query:
        message = ('I already have a survey from IP address '
                   f'{ip}. You might have submitted a survey.')
    if form.is_valid():
        new_rating = form.save(commit=False)
        new_rating.ip = ip
        form.save()
        form = Survey_Form()  # clears the user's form input
    context = {
        'form': form, 'message': message
    }
    return render(request, "ratings/submit_happiness.html", context)





def predict_happy_view(request):
    form = Predict_Survey_Form(request.POST)
    if form.is_valid():
        # with open(r'ratings\static\ratings\happy_somerville.pkl', 'rb') as f:
        #     model = pickle.load(f)
        model = load(r'ratings\static\ratings\happy_somerville.joblib') 

        ratings = form.cleaned_data
        ratings = ratings.values()
        ratings = [int(e) for e in ratings]
        ratings = np.array(ratings).reshape(1, -1)
        y_pred_prob = model.predict_proba(ratings)
        form = Predict_Survey_Form()
        percent_happy_prob = (f'There is a {y_pred_prob[0][1]*100:.2f}% '
                              'probability that you are happy.')

    else:
        percent_happy_prob = ''

    context = {
        'form': form, 'percent_happy_prob': percent_happy_prob,
    }
    return render(request, "ratings/predict_happiness.html", context)
