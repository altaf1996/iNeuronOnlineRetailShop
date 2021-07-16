from types import ModuleType
import pandas as pd
import numpy as np
#import matplolib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import pickle

def load_model(path):
    with open(path, 'rb') as pickle_file:
        model = pickle.load(pickle_file)
    return model


def load_csv(path1, path2):
    print("Loading a product_features_df")
    product_features_df = pd.read_csv(path1, low_memory=False)
    print("Loading a product_df")
    product_df =  pd.read_csv(path2, low_memory=False)
    print("Loading Completed")
    print("Loading Datasets Completed")
    return product_features_df, product_df

product_features_df, product_df = load_csv(path1="Datasets/title_asin_df.csv", path2="Datasets/product_df.csv")
print(product_features_df.head())
print(product_df.head())

def product_recommend(name):
  print("Loading Model")
  # Load the model
  path = "final_model.sav"
  model_knn = load_model(path=path)
  print("moidel Loaded")
  # Calculate the distances and indices
  print("Calculating distancesand indices") 
  distances, indices = model_knn.kneighbors(product_features_df.loc[name].values.reshape(1,-1), n_neighbors=6)
  # Get the recommendation
  print("Calculated")
  for i in range(0, len(distances.flatten())):
    if i==0:
      print("Recommendations for {0}:\n".format(product_features_df.loc[name].name))
    else:
      print(f"{i}: {product_features_df.iloc[indices.flatten()[i]].name}, with distance of : {distances.flatten()[i]}")
      print(product_df["imageURLHighRes"][product_features_df.index[indices.flatten()[i]]==product_df["title"]].iloc[0])

#print(product_df["imageURLHighRes"][product_features_df.index[indices.flatten()[0]]==product_df["title"]].iloc[0])
#product_recommend(name="Buxton Heiress Pik-Me-Up Framed Case")

"""  load & print the model
path = "final_model.sav"
model = load_model(path=path)
print(model)
"""