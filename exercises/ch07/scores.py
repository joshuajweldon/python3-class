file_name = '../../py3intro/DATA/testscores.dat'
scores = {}

grade_scale = (
    (95, 'A'),
    (89, 'B'),
    (83, 'C'),
    (75, 'D'),
    (0, 'F')
)

try:
    file = open(file_name)
except IOError:
    print("ERROR: Could not open file", file_name)

for line in file:
    name, score = line.split(':')
    score = int(score)
    letter = 'F'

    # Calculate letter
    for min_score, curr_letter in grade_scale:
        if score >= min_score:
            letter = curr_letter
            break

    scores[name] = {
        'score': score,
        'letter': letter
    }


for student, info in sorted(scores.items()):
    print(student, info['score'], info['letter'])

