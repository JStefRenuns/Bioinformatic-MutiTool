import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

cancer = load_breast_cancer()
X, y, target_names = cancer.data, cancer.target, cancer.target_names
df_raw = pd.DataFrame(X, columns=cancer.feature_names)
df_raw['diagnosis'] = [target_names[i] for i in y]

# Filter to keep only relevant data
filtered_df = df_raw[df_raw['mean radius'] > 11.0]
filtered_df.to_csv('filtered_biomarkers.csv', index=False)
