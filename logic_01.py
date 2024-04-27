import logging

logging.basicConfig(level=logging.INFO)


def fix_scores(scores: list[int]) -> list[int]:
    result = []
    for score in scores:
        score_str = str(score)
        if score_str != "100":
            flip_score = f"{score_str[-1]}{score_str[0]}"
            result.append(int(flip_score))
        else:
            result.append(score)
    return result


if __name__ == "__main__":
    student_scores = [35, 46, 57, 91, 29]
    fix_result = fix_scores(student_scores)
    logging.info(f"The correct result are: {fix_result}")
