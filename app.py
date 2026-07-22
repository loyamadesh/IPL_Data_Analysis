from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
with open("models/match_predictor.pkl", "rb") as f:
    model, encoders, target_encoder = pickle.load(f)

# Load dataset to get dropdown values
df = pd.read_excel("ipl.xlsx")
matches = df.groupby("match_id").first().reset_index()

teams = sorted(matches["batting_team"].unique())
venues = sorted(matches["venue"].unique())

@app.route("/")
def home():
    return render_template("index.html", teams=teams, venues=venues)

@app.route("/predict", methods=["POST"])
def predict():
    batting_team = request.form["batting_team"]
    bowling_team = request.form["bowling_team"]
    toss_winner = request.form["toss_winner"]
    venue = request.form["venue"]

    input_data = pd.DataFrame([[batting_team, bowling_team, toss_winner, venue]],
                              columns=["batting_team", "bowling_team", "toss_winner", "venue"])

    # Encode
    for col in input_data.columns:
        input_data[col] = encoders[col].transform(input_data[col])

    prediction = model.predict(input_data)
    result = target_encoder.inverse_transform(prediction)[0]

    return render_template("index.html", teams=teams, venues=venues,
                           prediction=result)

if __name__ == "__main__":
    app.run(debug=True)