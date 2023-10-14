import csv
import json

# Define the input and output file paths
input_csv_file = './input.csv'
output_json_file = './output.json'

# Initialize a dictionary to store the data
data = {
    "questions": []
}

# Read the CSV file and convert it to the desired JSON format
with open(input_csv_file, mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the first three rows
    for _ in range(3):
        next(csv_reader)
    
    for row in csv_reader:
        if len(row) >= 3:
            question = row[1]  # Second column contains the questions
            answer = row[2]    # Third column contains the answers

            # Create a dictionary for each question-answer pair
            qa_pair = {
                "question": question,
                "answer": answer
            }

            # Add the pair to the "questions" list
            data["questions"].append(qa_pair)

# Write the data to a JSON file
with open(output_json_file, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f'CSV file "{input_csv_file}" has been converted to JSON file "{output_json_file}".')
