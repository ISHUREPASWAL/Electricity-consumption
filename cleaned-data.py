from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dataset"

def clean_data():
    daily = pd.read_csv(DATA / "daily_electricity_consumption.csv")
    households = pd.read_csv(DATA / "households.csv")

    daily["date"] = pd.to_datetime(daily["date"], errors="coerce")
    daily["electricity_kwh"] = pd.to_numeric(daily["electricity_kwh"], errors="coerce")
    daily = daily.dropna(subset=["date", "electricity_kwh", "household_id"])
    daily = daily[daily["electricity_kwh"] >= 0]
    daily = daily.drop_duplicates()

    merged = daily.merge(households, on="household_id", how="left")
    merged["day_type"] = merged["date"].dt.dayofweek.map(
        lambda day: "Weekend" if day >= 5 else "Weekday"
    )
    merged["month"] = merged["date"].dt.strftime("%b")
    merged["month_number"] = merged["date"].dt.month
    merged.to_csv(DATA / "cleaned_electricity_data.csv", index=False)
    print(f"Cleaned records saved: {len(merged)}")
    print(f"Missing values remaining: {merged.isna().sum().sum()}")
    return merged

if __name__ == "__main__":
    clean_data()
