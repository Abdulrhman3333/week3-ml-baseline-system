import os
import sys
import pandas as pd
import numpy as np
from pathlib import Path



def make_sample_feature_table(*, root: Path | None = None, n_users: int = 50, seed: int = 42) -> None:
    """Generate sample data files for testing purposes."""
    ROOT = Path(__file__).resolve().parents[1]
    SRC = ROOT / "src"
    if str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))
    (ROOT / 'data' / 'processed').mkdir(parents=True, exist_ok=True)


    rng = np.random.default_rng(seed)
    user_id = [f'u{str(i).zfill(3)}' for i in range(1, n_users + 1)]
    country = rng.choice(['US', 'GB', 'CA', 'AU', 'DE'], size=n_users, replace=True)
    n_orders = rng.integers(1, 10, size=n_users)
    avg_amount = rng.normal(loc=10,scale=3, size=n_users).clip(min=1)
    total_amount = (n_orders * avg_amount).round(2)

    is_high_value = (total_amount > 80).astype(int)

   # Create DataFrame
    df = pd.DataFrame({
        'user_id': user_id,
        'country': country,
        'n_orders': n_orders,
        'total_amount': total_amount,
        'is_high_value': is_high_value
    })

    output_path = ROOT / 'data' / 'processed' / 'features.csv'
    df.to_csv(output_path, index=False)
    print(f'Sample data saved to: {output_path}')
    return output_path
