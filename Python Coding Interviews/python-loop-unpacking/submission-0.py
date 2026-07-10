from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highest_scorer = scores[0][0]
    highest_score = scores[0][1]
    for student_name, student_score in scores:
        if student_score > highest_score:
            highest_score = student_score
            highest_scorer = student_name

    return highest_scorer


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
