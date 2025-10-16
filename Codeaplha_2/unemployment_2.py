import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\\Users\\Admin\\Desktop\\Codeaplha_2\\Unemployment in India.csv")

df.columns = df.columns.str.strip()
df = df.rename(columns={
    "Estimated Unemployment Rate (%)": "UnemploymentRate",
    "Estimated Employed": "Employed",
    "Estimated Labour Participation Rate (%)": "LPR"
})

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")

df = df.dropna()

plt.figure(figsize=(10,6))
sns.lineplot(x="Date", y="UnemploymentRate", data=df)
plt.title("Unemployment Rate in India (2019–2020)")
plt.show()