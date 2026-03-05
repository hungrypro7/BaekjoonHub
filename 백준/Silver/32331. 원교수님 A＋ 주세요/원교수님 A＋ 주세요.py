import sys
N, M, X, Y = map(int, input().split())

kim_id, kim_score = input().split()

scores = []
for i in range(N-1):
    stu_id, stu_score = input().split()

    if stu_id[:4] == "2024":
        scores.append(int(stu_score))

if len(scores) < M:
    print("YES")
    print(0)
    sys.exit(0)

final_scores = []
for i in scores:
    final_s = Y - (X - i)
    if final_s < 0:
        final_s = 0
    final_scores.append(final_s)

all_score = []
for idx, j in enumerate(final_scores):
    all_score.append(j + scores[idx])

tmp = sorted(all_score, reverse=True)

if tmp[M-1] > (int(kim_score) + Y):
    print("NO")
else:
    print("YES")
    print(max(tmp[M-1] - int(kim_score), 0))
