# End-To-End Machine Learning Process #

## PreData: ##
    - For all ML algos, we should ask ourselves:
        - why are we doing this?
        - should we be doing this?
        - what kind of problem is it?
    - Check all assumptions 
    - Performance Measures
        - Root Mean Squared Error (RMSE):
            - sqrt[1/m * Sum[h(x^i) - y^i]^2]
            - more common choice of error measure
            - differentiable
        - Mean Absolute Error (MAE):
            - 1/m * Sum[abs(h(x^i) - y^i]^)]

## Get Data: ##
    - automate as much as you can
    - be aware of privacy concerns
    - examine data structure
        - how many attributes do you have
        - what types of attributes do you have
        - plot a histogram of all attributes
    - create a test set and set it aside (don't look at it until end)
        - pick random points

## Pandas: ##
    - a DataFrame object is like a spreadsheet
    - provides data manipulation features:
        - read in CSV files with column headers
        - plot histograms of all attributes
        - clean data (fill all empty values in a column with the medium value of that attribute)

## Explore Data: ##
    - visualize
        - plot various attributes against each other
        - do some dimensionality reduction
        - look for trends and outliers
    - consider creating new features

## Prepare Data: ##
    - data cleaning
        - missing features
    - converting categorical attributes
        - one hot vector
            - has as many elements as there are choices
            - red = (1, 0, 0)
            - yellow = (0, 1, 0)
            - blue = (0, 0, 1)
    - scaling
        - minimax
        - standardization
            - N(0, 1)

## Train Model: ##
    - set hyper parameters
        - how many layers in a neural network
        - how many degrees in polynomial
    - avoid data snooping
        - don't "try out" your model on your test set
        - set aside a third set of data for validation
            - "try out" your model on this validation set
    - validation
        - data can be expensive given availability
        - cross-validation
            - firstly, set aside your test set
            - divide rest of data into 3 sets 
            - train model on first 2/3 of data and validate on last 1/3
            - train model on last 2/3 of data and validate on first 1/3

## Fine-Tune Model: ##
    - grid search
    - randomized search
    - evaluate system on test set



