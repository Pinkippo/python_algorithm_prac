import time

def get_summary(filename):
  num_questions = 0
  num_students = 0
  total_score = 0
  best_score = 0

  file = open(filename, "r")
  lines = file.readlines()
  file.close()

  lines = [line.rstrip().lower().split(',') for line in lines]

  for i, student_scores in enumerate(lines[1:], start=1):
    sum_score = sum(4 for x, y in zip(student_scores, lines[0]) if x == y)
    total_score += sum_score
    best_score = max(best_score, sum_score)
  num_questions = len(lines[0])
  num_students = len(lines) - 1
  return (num_questions, num_students, total_score, best_score)


start = time.time()
num_q, num_s, total, best = get_summary("data/answers.csv")
end = time.time()

print(f"{end - start:.5f} sec")
print(f"# of questions: {num_q}")
print(f"# of students: {num_s}")
print(f"total score: {total}")
print(f"best score: {best}")

#시간복잡도를 줄이는데 있어서 조금 더 연습을 해야할 것 같다.
