import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

user = os.getenv("PGADMIN_USER")
password = os.getenv("PGADMIN_PASSWORD")

db_url = f"postgresql://{user}:{password}@localhost:5432/food_waste_management"

engine = create_engine(db_url)