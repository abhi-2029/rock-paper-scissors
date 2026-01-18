from flask import Flask, render_template, request, jsonify
import random

# Create Flask application
app = Flask(__name__)

# Dictionary to store player and computer scores
score = {"player": 0, "computer": 0}

def get_result(player, computer):
    """
    Decide the result of the game based on player and computer choices.
    Returns: 'win', 'lose', or 'tie'
    """
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
    """
    Home page route.
    Loads the main game interface and passes the current score.
    """
    return render_template("index.html", score=score)

@app.route("/play", methods=["POST"])
def play():
    """
    Handles the game logic when the user selects
    Rock, Paper, or Scissors.
    """
    # Get player's choice from frontend request
    player_choice = request.json["choice"]

    # Randomly select computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine game result
    result = get_result(player_choice, computer_choice)

    # Update scores based on result
    if result == "win":
        score["player"] += 1
    elif result == "lose":
        score["computer"] += 1

    # Send response back to frontend
    return jsonify({
        "player": player_choice,
        "computer": computer_choice,
        "result": result,
        "score": score
    })

# Start the Flask server
# host="0.0.0.0" is required for deployment platforms like Render
# port=10000 is commonly used for free deployments
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
