from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

score = {"player": 0, "computer": 0}

def get_result(player, computer):
    if player == computer:
        return "tie"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "win"
    else:
        return "lose"

@app.route("/")
def index():
    return render_template("index.html", score=score)

@app.route("/play", methods=["POST"])
def play():
    player_choice = request.json["choice"]
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = get_result(player_choice, computer_choice)

    if result == "win":
        score["player"] += 1
    elif result == "lose":
        score["computer"] += 1

    return jsonify({
        "player": player_choice,
        "computer": computer_choice,
        "result": result,
        "score": score
    })

if __name__ == "__main__":
    app.run(debug=True)
