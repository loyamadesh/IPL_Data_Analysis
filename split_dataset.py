import pandas as pd
import os

print("Loading IPL dataset...")
df = pd.read_excel("ipl.xlsx")

print("Dataset Loaded!")
print("Creating data folder...")
os.makedirs("data", exist_ok=True)

# ==============================
# Create matches.csv
# ==============================

print("Creating matches.csv...")

matches = df.groupby("match_id").first().reset_index()

match_columns = [
    "match_id",
    "season",
    "match_type",
    "event_name",
    "venue",
    "city",
    "toss_winner",
    "toss_decision",
    "match_won_by",
    "win_outcome"
]

match_columns = [col for col in match_columns if col in matches.columns]

matches = matches[match_columns]

matches.to_csv("data/matches.csv", index=False)

print("matches.csv created!")

# ==============================
# Create deliveries.csv
# ==============================

print("Creating deliveries.csv...")

delivery_columns = [
    "match_id",
    "innings",
    "batting_team",
    "bowling_team",
    "over",
    "ball",
    "batter",
    "bowler",
    "runs_batter",
    "runs_extras",
    "runs_total",
    "wicket_kind"
]

delivery_columns = [col for col in delivery_columns if col in df.columns]

deliveries = df[delivery_columns]

deliveries.to_csv("data/deliveries.csv", index=False)

print("deliveries.csv created!")
print("DONE ✅")