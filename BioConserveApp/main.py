# from fastapi import FastAPI, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
# from .database import get_db
# app = FastAPI()
#
# @app.get("/")
# async def test_db_connection(db: AsyncSession = Depends(get_db)):
#     return {"message": "Database connection is working!"}
# @app.get("/healthy")
# def health_check():
#     return {"status": "healthy"}

import yaml
from extract_csv import extract_csv
from transform_data import transform_data
from load_to_database import load_to_database

if __name__ == "__main__":
    # Load configuration
    with open("config/settings.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Extract
    print("Extracting data...")
    raw_data = extract_csv(config["data"]["csv_path"])

    if raw_data is not None:
        # Transform
        print("Transforming data...")
        cleaned_data = transform_data(raw_data)

        # Load
        print("Loading data into the database...")
        load_to_database(cleaned_data)
    else:
        print("Extraction failed. Pipeline terminated.")