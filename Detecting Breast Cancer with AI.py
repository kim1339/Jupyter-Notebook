
# coding: utf-8

# # Can AI help with medical imaging?
# 

# In[9]:


#For this classification project, I used a toy dataset from scikit-learn (so I didn't download any external files from other websites)
import sklearn
from sklearn import datasets

cancer = datasets.load_breast_cancer() # Load the breast cancer diagnostic dataset from scikit-learn

print("Names of Features")
print(cancer.feature_names) 

print("Names of Classes")
print(cancer.target_names)

# We find that either a tumor is 'malignant' or it is 'benign'.


# # Descision Tree Classifier
# Using the decision tree model which, given a supposed breast cancer tumor, we can label it as malignant or benign. Descision tree classifiers. A decision tree is a tree-like model where each node represents a feature, each link represents a decision and each leaf represents an outcome (label).

# In[12]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Create the training and testing datasets (you must have both training and testing data to create a machine learning classification model)
X = cancer.data # X, what we're using to predict, aka the features like tumor texture, radius, etc.
y = cancer.target # y, what we're predicting, aka the classes/labels (malignant or benign)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20) # We split the data into 'train' and 'test', test size is 20% of the data

# Train a classifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train) # Put these into the classifier

# Use the trained classifier to predict whether a new piece of data is benign or malignant
prediction = classifier.predict(X_test)

# Note that these predictions aren't necessarily correct, 1 is cancer (true), 0 is not (false)
prediction


# In[29]:


correct = 0 
for i in range(0, len(y_test)): # Iterate through all of our predictions
        if (y_test[i] == prediction[i]):
            correct += 1 

num_correct = correct
num_pred = (len(y_test))
accuracy = num_correct / num_pred

print(num_correct)
print(num_pred)
print(accuracy)

