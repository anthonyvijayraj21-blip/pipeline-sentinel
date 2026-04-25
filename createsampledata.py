import pandas as pd
import numpy as np
import random
import os

random.seed(42)
np.random.seed(42)

os.makedirs("data", exist_ok=True)

n = 1000

# Generate realistic order values with a few outliers injected
normal_values = list(np.random.lognormal(mean=4, sigma=0.8, size=n - 5))
outlier_values = [9999.0, 8500.0, 0.01, -50.0, 7200.0]  # intentional anomalies
payment_values = normal_values + outlier_values
random.shuffle(payment_values)

data = {
    "orderid": [f"ORD{str(i).zfill(5)}" for i in range(1, n + 1)],
    "customerid": [f"CUST{random.randint(1000, 9999)}" for _ in range(n)],
    "paymentvalue": [round(v, 2) for v in payment_values],
    "freightvalue": [round(v, 2) for v in np.random.uniform(5, 200, n)],
    "orderstatus": random.choices(
        ["delivered", "shipped", "cancelled", "processing"],
        weights=[70, 15, 10, 5],
        k=n
    )
}

source_df = pd.DataFrame(data)
source_df.to_csv("data/orders_source.csv", index=False)

# Target has 2 fewer rows to simulate data loss in the pipeline
target_df = source_df.iloc[:-2].copy()
target_df.to_csv("data/orders_target.csv", index=False)

print(f"Created orders_source.csv - {len(source_df)} rows")
print(f"Created orders_target.csv - {len(target_df)} rows")
print("Note: target is missing 2 rows to simulate pipeline data loss")
print("Note: 5 outlier payment values are injected for anomaly detection")
