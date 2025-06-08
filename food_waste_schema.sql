CREATE TABLE providers (
    provider_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT,
    address TEXT,
    city TEXT,
    contact TEXT
);

CREATE TABLE receivers (
    receiver_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT,
    city TEXT,
    contact TEXT
);

CREATE TABLE food_listings (
    food_id SERIAL PRIMARY KEY,
    food_name TEXT NOT NULL,
    quantity INT NOT NULL,
    expiry_date DATE,
    provider_id INT REFERENCES providers(provider_id) ON DELETE CASCADE,
    provider_type TEXT,
    location TEXT,
    food_type TEXT,
    meal_type TEXT
);

CREATE TABLE claims (
    claim_id SERIAL PRIMARY KEY,
    food_id INT REFERENCES food_listings(food_id) ON DELETE CASCADE,
    receiver_id INT REFERENCES receivers(receiver_id) ON DELETE CASCADE,
    status TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);