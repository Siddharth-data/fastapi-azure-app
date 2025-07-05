from faker import Faker
import pandas as pd
import random

fake = Faker()
Faker.seed(42)

def generate_order_data(n=1000):
    data = []
    for _ in range(n):
        data.append({
            "order_id": fake.uuid4(),
            "customer_name": fake.name(),
            "email": fake.email(),
            "product": random.choice(["Laptop", "Phone", "Headphones", "Camera"]),
            "category": random.choice(["Electronics", "Accessories"]),
            "amount": round(random.uniform(20.0, 2000.0), 2),
            "purchase_date": fake.date_this_year(),
            "country": fake.country()
        })
    return pd.DataFrame(data)

df = generate_order_data(500)
df.to_csv("fake_orders.csv", index=False)

from fastapi import FastAPI
import pandas as pd

app = FastAPI()
df = pd.read_csv("fake_orders.csv")

@app.get("/")
def root():
    return {"message": "Fake Orders API is running."}

@app.get("/orders")
def get_orders(limit: int = 10):
    return df.head(limit).to_dict(orient="records")