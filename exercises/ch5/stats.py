import sys

scores_input = input("Enter your students scores, seperated by ' ': ").strip()

scores = []

try:
    scores = [float(score) for score in scores_input.split(" ")]
except ValueError:
    print("Error: You must enter valid numbers")
    exit(1)

print('max"',  max(scores))
print('min: ', min(scores))
print('avg: ', sum(scores)/len(scores))
