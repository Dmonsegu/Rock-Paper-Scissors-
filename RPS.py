import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # Default first move
    if prev_play == "":
        return "R"

    # Predict their next move based on their last 3
    guess = predict(opponent_history)

    # Return the move that beats the predicted one
    return counter_move(guess)


def predict(history):
    if len(history) < 3:
        return random.choice(["R", "P", "S"])

    # Basic pattern detection: last 3
    sequence = "".join(history[-3:])
    pattern_map = {}

    for i in range(len(history) - 3):
        key = "".join(history[i:i+3])
        next_move = history[i+3] if i+3 < len(history) else ""
        if key == sequence:
            if next_move in pattern_map:
                pattern_map[next_move] += 1
            else:
                pattern_map[next_move] = 1

    if pattern_map:
        # Return the most likely next move
        return max(pattern_map, key=pattern_map.get)
    else:
        return random.choice(["R", "P", "S"])


def counter_move(move):
    counters = {"R": "P", "P": "S", "S": "R"}
    return counters[move]

