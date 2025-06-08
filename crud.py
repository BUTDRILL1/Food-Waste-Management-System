from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv("PGADMIN_USER")
password = os.getenv("PGADMIN_PASSWORD")
db_url = f"postgresql://{user}:{password}@localhost:5432/food_waste_management"

engine = create_engine(db_url)

# PROVIDERS
def add_provider(name, type_, address, city, contact):
    query = """
        INSERT INTO providers (name, type, address, city, contact)
        VALUES (:name, :type, :address, :city, :contact)
        RETURNING provider_id;
    """
    with engine.begin() as conn:
        result = conn.execute(text(query), {
            "name": name,
            "type": type_,
            "address": address,
            "city": city,
            "contact": contact
        })
        return result.scalar()

def update_provider(provider_id, name=None, contact=None):
    updates = []
    params = {"provider_id": provider_id}
    if name:
        updates.append("name = :name")
        params["name"] = name
    if contact:
        updates.append("contact = :contact")
        params["contact"] = contact
    if not updates:
        return
    query = f"UPDATE providers SET {', '.join(updates)} WHERE provider_id = :provider_id"
    with engine.begin() as conn:
        conn.execute(text(query), params)

def delete_provider(provider_id):
    query = "DELETE FROM providers WHERE provider_id = :provider_id"
    with engine.begin() as conn:
        conn.execute(text(query), {"provider_id": provider_id})


# RECEIVERS
def add_receiver(name, type_, city, contact):
    query = """
        INSERT INTO receivers (name, type, city, contact)
        VALUES (:name, :type, :city, :contact)
        RETURNING receiver_id;
    """
    with engine.begin() as conn:
        result = conn.execute(text(query), {
            "name": name,
            "type": type_,
            "city": city,
            "contact": contact
        })
        return result.scalar()

def update_receiver(receiver_id, name=None, contact=None):
    updates = []
    params = {"receiver_id": receiver_id}
    if name:
        updates.append("name = :name")
        params["name"] = name
    if contact:
        updates.append("contact = :contact")
        params["contact"] = contact
    if not updates:
        return
    query = f"UPDATE receivers SET {', '.join(updates)} WHERE receiver_id = :receiver_id"
    with engine.begin() as conn:
        conn.execute(text(query), params)

def delete_receiver(receiver_id):
    query = "DELETE FROM receivers WHERE receiver_id = :receiver_id"
    with engine.begin() as conn:
        conn.execute(text(query), {"receiver_id": receiver_id})


# FOOD LISTINGS
def add_food(food_name, quantity, expiry_date, provider_id, provider_type, location, food_type, meal_type):
    query = """
        INSERT INTO food_listings (
            food_name, quantity, expiry_date,
            provider_id, provider_type, location,
            food_type, meal_type
        )
        VALUES (
            :food_name, :quantity, :expiry_date,
            :provider_id, :provider_type, :location,
            :food_type, :meal_type
        );
    """
    with engine.begin() as conn:
        conn.execute(text(query), {
            "food_name": food_name,
            "quantity": quantity,
            "expiry_date": expiry_date,
            "provider_id": provider_id,
            "provider_type": provider_type,
            "location": location,
            "food_type": food_type,
            "meal_type": meal_type
        })

def delete_food(food_id):
    query = "DELETE FROM food_listings WHERE food_id = :food_id"
    with engine.begin() as conn:
        conn.execute(text(query), {"food_id": food_id})


# CLAIMS 
def add_claim(food_id, receiver_id, status, timestamp):
    query = """
        INSERT INTO claims (food_id, receiver_id, status, timestamp)
        VALUES (:food_id, :receiver_id, :status, :timestamp);
    """
    with engine.begin() as conn:
        conn.execute(text(query), {
            "food_id": food_id,
            "receiver_id": receiver_id,
            "status": status,
            "timestamp": timestamp
        })

def update_claim_status(claim_id, new_status):
    query = "UPDATE claims SET status = :status WHERE claim_id = :claim_id"
    with engine.begin() as conn:
        conn.execute(text(query), {
            "claim_id": claim_id,
            "status": new_status
        })

def delete_claim(claim_id):
    query = "DELETE FROM claims WHERE claim_id = :claim_id"
    with engine.begin() as conn:
        conn.execute(text(query), {"claim_id": claim_id})