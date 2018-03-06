# Machine Learning Classification #

## Binary Classifiers ##
### Confusion Matrix: ###
- actual negative and predicted negative = True Negative (TN)
- actual negative but predicted positive = False Positive (FP)
- actual positive but predicted negative = False Negative (TN)
- actual positive and predicted positive = True Positive (TP)
- **accuracy** = (TP + TN) / (TP + FP + TN + FN)
    - a confusion matrix of [[3, 1], [2, 4]] has an accuracy rating of 70% or .7 (TN = 3, TP = 4)
- **precision** = TP / (TP + FP)
    - for a model to have high percision, it must have relatively small FP
    - a confusion matrix of [[3, 1], [2, 4]] has a precision rating of 80% or .8 
- **recall** = TP / (TP + FN)
    - for a model to have high recall, it must have relatively small FN
    - a confusion matrix of [[3, 1], [2, 4]] has a recall rating of 66% or 4/6 
- note that the upper left corner of the precision-recall curve corresponds to a high threshold value
    - high precision = high threshold
        - almost no FP
    - high recall = low threshold
        - almost no FN
    - use the percision-recall curve when you care more about the false positive than the false negatives
- when comparing confusion matrix plots, normalize the rows to standardize sample size

## Categorical Classifiers ##
- OVA (one-versus-all)
    - compare current category against all other categories (equal or not equal to)
- OVO (one-versus-one)
    - for each possible categorical pair, construct classifier to find difference between categories
- OVA is usually faster because you have to train more classifiers for OVO
    - if you have 10 classes (n = 10), you have to train n for OVA and n^2 for OVO

