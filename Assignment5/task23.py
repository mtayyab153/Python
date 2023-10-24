def find_second_lowest_grade(nested_list):
    # list of scores
    score_list = [score for name, score in nested_list]

    # Sort the score list and remove duplicates
    sorted_unique_scores = sorted(list(set(score_list)))

    # second lowest grade
    second_lowest_grade = sorted_unique_scores[1]

    # Find names with the second lowest grade
    names_with_second_lowest_grade = [
        name for name, score in nested_list if score == second_lowest_grade
    ]

    return sorted_unique_scores, second_lowest_grade, names_with_second_lowest_grade


nested_list = [["Alice", 85], ["Bob", 90], ["John", 78], ["Emma", 88], ["Sam", 75]]

print("Nested List:", nested_list)
scores, second_lowest_grade, names = find_second_lowest_grade(nested_list)
print("Score List:", scores)
print("Sorted Score List with Unique Elements:", sorted(scores))
print("Second Lowest Grade:", second_lowest_grade)
print("Names with Second Lowest Grade:", names)
