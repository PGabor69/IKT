import csv

def read_data_from_file(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

def list_all_data(data):
    for record in data:
        print(record)

def write_data_to_file(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def filter_data_by_time_range(data, start_year, end_year):
    filtered_data = [record for record in data if start_year <= int(record['Year']) <= end_year]
    return filtered_data

def quiz(data):
    import random

    question_year = random.choice([record['Year'] for record in data])
    correct_answers = random.sample([record['Achievement'] for record in data if record['Year'] == question_year], 3)
    correct_answer = random.choice(correct_answers)

    print(f"\nIn the year {question_year}, which achievement is correct?")
    for i, answer in enumerate(correct_answers):
        print(f"{i+1}. {answer}")

    user_answer = input("Your answer (1, 2, or 3): ")
    if correct_answers[int(user_answer) - 1] == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")

if __name__ == "__main__":
    file_path = "asd.CSV"  # Change this to your actual data file path
    data = read_data_from_file(file_path)

    while True:
        print("\nMenu:")
        print("1. List all data on the screen")
        print("2. List all data to a file")
        print("3. List achievements in a given time range")
        print("4. Quiz (optional)")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            list_all_data(data)
        elif choice == '2':
            output_file = input("Enter the output file name: ")
            write_data_to_file(data, output_file)
            print(f"Data has been written to {output_file}")
        elif choice == '3':
            start_year = int(input("Enter the start year: "))
            end_year = int(input("Enter the end year: "))
            filtered_data = filter_data_by_time_range(data, start_year, end_year)
            list_all_data(filtered_data)
        elif choice == '4':
            quiz(data)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        
        another_operation = input("\nDo you want to perform another operation? (y/n): ")
        if another_operation.lower() != 'y':
            break