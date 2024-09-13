n = int(input())

scores = []
for _ in range(n):
    score = int(input())
    scores.append(score)

scores.sort(reverse=True)
silver_score = scores[1]

print(f"Silver = {silver_score}")
