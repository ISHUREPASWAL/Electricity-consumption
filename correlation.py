from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dataset"
OUT = ROOT / "visualizations"

def main():
    df = pd.read_csv(DATA / "cleaned_electricity_data.csv")
    household = df.groupby(["household_id","family_size"], as_index=False)["electricity_kwh"].mean()
    corr = household[["family_size","electricity_kwh"]].corr()
    plt.figure(figsize=(6,4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
    plt.title("Correlation: Family Size and Average Daily Consumption")
    plt.tight_layout()
    plt.savefig(OUT / "correlation_heatmap.png", dpi=150)
    plt.close()
    print(f"Correlation coefficient: {corr.loc['family_size','electricity_kwh']:.3f}")

if __name__ == "__main__":
    main()
