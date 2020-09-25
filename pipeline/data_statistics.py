import pandas as pd
import numpy as np

data_path = "trial_data.csv"
with open(data_path, encoding="utf-8") as data_file:
    df = pd.read_csv(data_file)

print(df.head(10))
print(df.describe())

texts = list(df["text"])
text_lengths = list(map(len, texts))
print("number of characters- avg:", np.mean(text_lengths), "min:", np.min(text_lengths), "med:", np.median(text_lengths), "max:", np.max(text_lengths))
text_num_words = list(map(lambda t: len(t.split()), texts))
print("number of tokens (split whitespace)- avg:", np.mean(text_num_words), "min:", np.min(text_num_words), "med:", np.median(text_num_words), "max:", np.max(text_num_words))


print("total characters:", sum(text_lengths))
print("total tokens (split whitespace):", sum(text_num_words))
