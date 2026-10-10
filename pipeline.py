import os
import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

def run_pipeline():
    print(f" Pipeline started at {datetime.now()}")
    
    # 1. EXTRACT
    url = "https://fakestoreapi.com/products"
    try:
        response = requests.get(url)
        response.raise_for_status()
        raw_data = response.json()
    except Exception as e:
        print(f" Extraction failed: {e}")
        return

    # 2. TRANSFORM
    df = pd.DataFrame(raw_data)
    df['rating_score'] = df['rating'].apply(lambda x: x['rate'])
    df['review_count'] = df['rating'].apply(lambda x: x['count'])
    
    df_clean = df[['id', 'title', 'price', 'category', 'rating_score', 'review_count']].copy()
    df_clean['price'] = df_clean['price'].astype(float)
    df_clean['review_count'] = df_clean['review_count'].astype(int)
    
    # Add a timestamp so we know when this batch was loaded!
    df_clean['loaded_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 3. LOAD
    # GitHub Actions uses Environment Variables instead of Colab Secrets
    DATABASE_URL = os.environ.get("DATABASE_URL")
    if not DATABASE_URL:
        print(" DATABASE_URL environment variable not set!")
        return
        
    engine = create_engine(DATABASE_URL)
    
    # Note: We use 'replace' here. In a real client scenario with millions of rows, 
    # you would use 'append' and write logic to handle duplicates (Upsert).
    df_clean.to_sql(
        name="products_table",
        con=engine,
        if_exists="replace", 
        index=False
    )
    print(f" Success! Loaded {len(df_clean)} rows into Neon Cloud.")

if __name__ == "__main__":
    run_pipeline()