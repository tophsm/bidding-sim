import pandas as pd
import numpy as np

np.random.seed(42)

#simulated data
n = 10000
data = pd.DataFrame({
    "user_age": np.random.randint(18, 65, n),
    "ad_quality": np.random.randint(n),
    "device": np.random.choice(["mobile", "desktop"], n),
    "hour": np.random.randint(0, 24, n), 
    "clicked": np.random.binomial(1, 0.15, n)
})

#encode device
data["device"] = data["device"].map({"mobile": 0, "desktop": 1})