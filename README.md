# 🥗 Food Waste Management System

A full-stack, data-driven platform for managing food surplus distribution between providers (restaurants, supermarkets, etc.) and receivers (NGOs, shelters, etc.). Built using Python, PostgreSQL, and Streamlit.

---

## 🔧 Tech Stack

- 🐍 Python 3.9.13
- 📊 Streamlit 1.45.1 (Multipage UI)
- 🛢️ PostgreSQL (Relational Database)
- 🧮 SQLAlchemy (ORM + Query engine)
- 📈 Seaborn/Matplotlib/Plotly (EDA visuals)
- 📂 .env support for secure DB config

---

## 📁 Folder Structure

```bash
foodWasteManagement/
├── app.py / 0_Home.py # Main entry point (Home)
├── pages/
│ ├── 1_Dashboard.py
│ ├── 2_Food_Listings.py
│ ├── 3_Add_Entries.py
│ ├── 4_Claims.py
│ ├── 5_Analysis.py
│ └── 6_EDA.py
├── crud.py # All database insert/update/delete logic
├── engine_util.py # Loads DB connection via .env
├── eda_analysis.py # Offline EDA script
├── table_data_reset.sql # Resets test/dev records and sequences
├── .env # DB credentials (ignored in Git)
└── README.md
```

---

## 🗄️ Database Design (PostgreSQL)

- `providers(provider_id, name, type, address, city, contact)`
- `receivers(receiver_id, name, type, city, contact)`
- `food_listings(food_id, food_name, quantity, expiry_date, provider_id, location, food_type, meal_type)`
- `claims(claim_id, food_id, receiver_id, status, timestamp)`

All primary keys are auto-incrementing via SERIAL sequences. Foreign key relationships ensure referential integrity.

---

## 🚀 Features

- 📦 Add, edit & view: Providers, Receivers, Listings, Claims
- 📊 Dashboard with real-time metrics
- 📈 Analytical queries for trends & usage
- 🧪 Interactive EDA with visual insights
- 🔎 Filterable views by meal type, city, etc.
- ✅ Sequence-safe ID resets for dev/test data
- 🔐 .env-protected DB access

---

## ▶️ Running the App

1. Clone the repo

```bash
git clone https://github.com/BUTDRILL1/foodWasteManagement.git
cd foodWasteManagement
```

2. Create and activate your Python environment

```bash
pip install -r requirements.txt
```

3. Create a .env file with your DB credentials:

```bash
PGADMIN_USER = your_postgres_username
PGADMIN_PASSWORD = your_postgres_password
```

4. Launch the Streamlit app

```bash
python -m streamlit run 0_Home.py
```
---

## 🔄 Reset Development Data (Optional)

### ⚠️Warning: Only for development and testing

Use the bundled SQL script to delete all test entries above ID 1000 and reset sequences:

Use ```table_data_reset.sql``` to apply this across all 4 tables.