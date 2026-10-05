# Rock Paper Scissors AI

A Python-based Rock Paper Scissors strategy that analyzes an opponent's previous moves, identifies recurring patterns, and predicts their next move.

## Overview

This project was built as a strategy agent for a Rock Paper Scissors game. Instead of selecting moves completely at random, the player keeps track of the opponent's move history and looks for previously observed sequences.

The strategy uses the opponent's most recent three moves as a pattern. If that same sequence has appeared previously, the program looks at what move the opponent played immediately afterward and uses the most common follow-up move as its prediction.

The player then selects the move that counters that prediction.

## How It Works

The strategy follows four main steps:

1. **Track opponent history**

   * Stores each move made by the opponent.
   * Uses the history to identify recurring sequences.

2. **Detect patterns**

   * Looks at the opponent's most recent three moves.
   * Searches the previous game history for the same sequence.

3. **Predict the next move**

   * If the pattern has appeared before, the program determines which move most frequently followed it.
   * If there is not enough historical information, it selects a random move.

4. **Counter the prediction**

   * Rock → Paper
   * Paper → Scissors
   * Scissors → Rock

## Example

If an opponent repeatedly follows:

```text
R → P → R → S
```

and the same `RPS` sequence appears again, the program can use the historical response to predict what the opponent is likely to play next.

It then chooses the move that beats that prediction.

## Performance

The strategy was tested against four different opponents over **1,000 rounds each**.

| Opponent | Player 1 Wins | Player 2 Wins | Ties |  Win Rate |
| -------- | ------------: | ------------: | ---: | --------: |
| Quincy   |           994 |             2 |    4 | **99.8%** |
| Abbey    |           403 |           308 |  289 | **56.7%** |
| Kris     |           464 |           215 |  321 | **68.3%** |
| Mrugesh  |           721 |           188 |   91 | **79.3%** |

The results show that the strategy performs particularly well against opponents whose behavior can be exploited through recurring patterns.

## Testing

Automated tests were created using Python's `unittest` framework.

Each test runs the player against one of the four opponents for 1,000 rounds and checks that the strategy reaches the required performance threshold.

```python
actual = play(player, quincy, 1000) >= 60
self.assertTrue(actual)
```

The same validation approach was used for Abbey, Kris, and Mrugesh.

## Technologies

* **Python**
* `random`
* `unittest`
* Algorithmic pattern detection
* Historical sequence analysis

## Key Skills

* Python programming
* Algorithm design
* Pattern recognition
* Conditional logic
* Probability-based decision making
* Automated testing
* Performance evaluation

## Project Takeaway

This project demonstrates how historical behavioral data can be used to make predictions and guide decisions. Although the strategy is relatively simple, it provides a practical example of using pattern detection and feedback to build an adaptive decision-making system.
