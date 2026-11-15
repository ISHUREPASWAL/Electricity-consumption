from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dataset"
OUT = ROOT / "visualizations"

def main():
    df = pd.read_csv(DATA / "appliance_usage.csv")
    summary = df.groupby("appliance", as_index=False)["estimated_monthly_kwh"].sum()
    summary = summary.sort_values("estimated_monthly_kwh", ascending=False)
    plt.figure(figsize=(9,5))
    sns.barplot(data=summary, x="estimated_monthly_kwh", y="appliance", color="darkorange")
    plt.title("Estimated Electricity Use by Appliance")
    plt.xlabel("Estimated monthly consumption (kWh)"); plt.ylabel("Appliance")
    plt.tight_layout()
    plt.savefig(OUT / "appliance_analysis.png", dpi=150)
    plt.close()
    print(summary.to_string(index=False))

if __name__ == "__main__":
    main()
