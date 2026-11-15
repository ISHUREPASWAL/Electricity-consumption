from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dataset"
OUT = ROOT / "visualizations"

def main():
    df = pd.read_csv(DATA / "cleaned_electricity_data.csv")
    summary = df.groupby("day_type", as_index=False)["electricity_kwh"].mean()
    plt.figure(figsize=(7,5))
    sns.barplot(data=summary, x="day_type", y="electricity_kwh", hue="day_type", legend=False)
    plt.title("Average Daily Electricity Consumption: Weekday vs Weekend")
    plt.xlabel("Day type"); plt.ylabel("Average consumption per household (kWh)")
    plt.tight_layout()
    plt.savefig(OUT / "weekday_weekend_analysis.png", dpi=150)
    plt.close()
    print(summary.to_string(index=False))

if __name__ == "__main__":
    main()
