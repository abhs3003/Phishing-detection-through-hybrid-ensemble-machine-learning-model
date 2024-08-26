# Purpose - Receive the call for testing a page from the Chrome extension and return the result (SAFE/PHISHING)
# for display. This file calls all the different components of the project (The ML model, features_extraction) and
# consolidates the result.

import joblib
import feature
import sys
import numpy as np

from feature import *


def get_prediction_from_url(test_url):
    features_test = extract_features(test_url)
    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    #features_test = np.array(features_test).reshape((1, -1))
    clf = joblib.load(LOCALHOST_PATH + DIRECTORY_NAME + '/classifier/ensemble_model.pkl')
    probabilities = clf.predict_proba([features_test])[0][1] 
    #pred=probabilities[0] # Predict probabilities for each class
    phishing_probability =probabilities  # Probability of being classified as phishing
    threshold = 0.4
    is_phishing = phishing_probability>= threshold
    print(phishing_probability)
    # Classify as phishing if probability is above a threshold

    return is_phishing


def main():
    url = sys.argv[1]
    prediction = get_prediction_from_url(url)

    # Print the probability of prediction (if needed)
    # prob = clf.predict_proba(features_test)
    # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

    if prediction == False:
        # print "The website is safe to browse"
        print("SAFE")
    elif prediction == True:
        # print "The website has phishing features. DO NOT VISIT!"
        print("PHISHING")

        # print 'Error -', features_test


if __name__ == "__main__":
    main()