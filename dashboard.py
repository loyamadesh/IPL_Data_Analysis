import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ipl.xlsx")

# Top run scorers
top_batters = df.groupby("batter")["runs_batter"].sum().sort_values(ascending=False).head(10)

plt.figure()
top_batters.plot(kind="bar")
plt.title("Top 10 Run Scorers in IPL")
plt.xlabel("Player")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top wicket takers
top_bowlers = df["bowler_wicket"].value_counts().head(10)

plt.figure()
top_bowlers.plot(kind="bar")
plt.title("Top 10 Wicket Takers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()