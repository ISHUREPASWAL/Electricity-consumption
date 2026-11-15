from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dataset"
OUT = ROOT / "visualizations"

def main():
    df = pd.read_csv(DATA / "cleaned_electricity_data.csv")
    household = df.groupby(["household_id","city","family_size"], as_index=False)["electricity_kwh"].sum()
    household = household.sort_values("electricity_kwh", ascending=False).head(10)
    plt.figure(figsize=(10,5))
    sns.barplot(data=household, x="household_id", y="electricity_kwh", hue="city", dodge=False)
    plt.title("Top 10 Households by Total Electricity Consumption")
    plt.xlabel("Household"); plt.ylabel("Total consumption (kWh)")
    plt.xticks(rotation=45); plt.legend(title="City", bbox_to_anchor=(1.02,1), loc="upper left")
    plt.tight_layout()
    plt.savefig(OUT / "top_households.png", dpi=150)
    plt.close()

    family = df.groupby(["household_id","family_size"], as_index=False)["electricity_kwh"].mean()
    plt.figure(figsize=(8,5))
    sns.regplot(data=family, x="family_size", y="electricity_kwh", scatter_kws={"alpha":0.7})
    plt.title("Family Size and Average Daily Electricity Consumption")
    plt.xlabel("Family size (people)"); plt.ylabel("Average daily consumption (kWh)")
    plt.tight_layout()
    plt.savefig(OUT / "family_size_analysis.png", dpi=150)
    plt.close()
    print("Top 10 households:")
    print(household[["household_id","city","electricity_kwh"]].to_string(index=False))

if __name__ == "__main__":
    main()
