from flask import Flask
import joblib
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import FeatureUnion
import numpy as np

app = Flask(__name__)

randforest_clf = joblib.load('G:\ml_code\deloy_model\\app\models\\best_randforest_clf')
# randforest_clf = joblib.load('models/best_randforest_clf')

class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, feature_names):
        self.feature_names = feature_names
    def fit(self, dataframe, labels=None):
        return self
    def transform(self, dataframe):
        return dataframe[self.feature_names].values

num_feat_names=['age', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose', 'cigsPerDay']
bool_feat_names=['male', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'currentSmoker']

num_pipeline = Pipeline([
    ('selector', ColumnSelector(num_feat_names)),
    ('imputer', SimpleImputer(missing_values=np.nan, strategy="median", copy=True)),
    ('std_scaler', StandardScaler(with_mean=True, with_std=True, copy=True))
    ])

bool_pipeline = Pipeline([
    ('selector', ColumnSelector(bool_feat_names)),
    ('imputer', SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=0, copy=True))
    ])
full_pipeline = FeatureUnion(transformer_list=[
    ("num_pipeline", num_pipeline),
    ("cat_pipeline", bool_pipeline) ])
