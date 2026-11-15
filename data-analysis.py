from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dataset"

def main():
    df = pd.read_csv(DATA / "cleaned_electricity_data.csv")
    total = df["electricity_kwh"].sum()
    print("\n--- Overall Electricity Summary ---")
    print(f"Households: {df['household_id'].nunique()}")
    print(f"Daily records: {len(df)}")
    print(f"Total sample consumption: {total:,.2f} kWh")
    print(f"Average daily household consumption: {df['electricity_kwh'].mean():.2f} kWh")
    print(f"Highest daily record: {df['electricity_kwh'].max():.2f} kWh")
    print(f"Lowest daily record: {df['electricity_kwh'].min():.2f} kWh")

if __name__ == "__main__":
    main()
