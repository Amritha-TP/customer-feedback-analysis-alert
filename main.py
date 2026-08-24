# from tqdm import tqdm
# from src.data.load_data import load_data
# from src.data.preprocess import create_sentiment

# tqdm.pandas()

# df = load_data("data/raw/Reviews.csv")
# df["sentiment"] = df["Text"].progress_apply(create_sentiment)

# print(df[["Text", "sentiment"]].head())

#______________________________________________________________________

# from src.data.preprocess import clean_text

# print(clean_text("I don't like this product www.example.com ! It's terrible."))

#_______________________________________________________________________

from src.data.process_dataset import process_dataset


process_dataset()