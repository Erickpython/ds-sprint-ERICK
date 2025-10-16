# QUESTION 1: LISTS AND LOOPS
daily_temp = [29, 30, 28, 31, 32, 27, 30]

average_temp = sum(daily_temp) / len(daily_temp)
print("Average Temperature:", average_temp)

days_above_30 = [temp for temp in daily_temp if temp > 30]
print(f"Days with temperature above 30°C: {days_above_30} and they are {len(days_above_30)} days")

max_temp = max(daily_temp)
min_temp = min(daily_temp)
print(f"Maximum Temperature: {max_temp} °C and Minimum Temperature: {min_temp} °C")

# QUESTION 2: DICTIONARIES 
students = {
    "ERICK":[85, 90, 78],
    "MARY":[88, 79, 92],
    "JOHN":[75, 80, 85]
}

def calculate_average(grades):
    for student, scores in grades.items():
        avg_score = sum(scores) / len(scores)
        print(f"{student}'s average score: {avg_score:.2f}")    

calculate_average(students)

student_with_highest_avg = max(students, key=lambda student: sum(students[student]) / len(students[student]))
print(f"Student with the highest average score: {student_with_highest_avg}")

# QUESTION 3: TEXT FILE ANALYSIS
with open("sample.txt", "r") as file:
    text = file.read()

# count how many times each word appears
word_count = {}
words = text.split()
for word in words:
    word = word.lower().strip('.,!?;"()[]{}')  # Normalize the word
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1            
print("Word Count:", word_count)




