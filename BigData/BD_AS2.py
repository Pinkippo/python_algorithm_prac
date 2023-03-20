import time


def get_summary(filename):
  file = open(filename, "r")
  lines = file.readlines()
  file.close()

  lines = [line.rstrip().lower().split(',') for line in lines]

  num_questions = len(lines[0])
  num_students = len(lines) - 1
  total_score = sum(
    sum(4 for x, y in zip(student_scores, lines[0]) if x == y)
    for student_scores in lines[1:])
  best_score = max(
    sum(4 for x, y in zip(student_scores, lines[0]) if x == y)
    for student_scores in lines[1:])

  return (num_questions, num_students, total_score, best_score)


start = time.time()
num_q, num_s, total, best = get_summary("data/answers.csv")
end = time.time()

print(f"{end - start:.5f} sec")
print(f"# of questions: {num_q}")
print(f"# of students: {num_s}")
print(f"total score: {total}")
print(f"best score: {best}")
