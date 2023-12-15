import random

participants = ["Alice", "Bob", "Charlie", "David", "Eve"]

random.shuffle(participants)

for i in range(len(participants)):
    giver = participants[i]
    receiver = participants[(i + 1) % len(participants)]
    print(giver, "is the Secret Santa for",receiver)