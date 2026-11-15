from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dataset"
OUT = ROOT / "visualizations"
MONTH_ORDER = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def main():
    df = pd.read_csv(DATA / "cleaned_electricity_data.csv")
    summary = df.groupby(["month", "month_number"], as_index=False)["electricity_kwh"].sum()
    summary = summary.sort_values("month_number")
    plt.figure(figsize=(9,5))
    sns.barplot(data=summary, x="month", y="electricity_kwh", color="steelblue")
    plt.title("Total Electricity Consumption by Month")
    plt.xlabel("Month"); plt.ylabel("Electricity consumption (kWh)")
    plt.tight_layout()
    plt.savefig(OUT / "monthly_consumption.png", dpi=150)
    plt.close()
    print(summary[["month","electricity_kwh"]].to_string(index=False))

if __name__ == "__main__":
    main()
