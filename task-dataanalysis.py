import csv

def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

def calculate_average(column, data):
    total = sum(float(row[column]) for row in data)
    return total / len(data)

def find_maximum(column, data):
    max_value = max(float(row[column]) for row in data)
    return max_value

def find_minimum(column, data):
    min_value = min(float(row[column]) for row in data)
    return min_value

def display_data(data):
    print("\nContents of csv file:")
    for row in data:
        print(row)

def main():
    file_name = input("Enter the CSV file name: ")
    data = read_csv_file(file_name)
    
    display_data(data)
    
    while True:
        print("\nChoose an action:")
        print("1 - Calculate Average")
        print("2 - Find Maximum")
        print("3 - Find Minimum")
        print("4 - Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            column = input("Enter the column name for which you want to calculate the average: ")
            try:
                average = calculate_average(column, data)
                print(f"Average {column}: {average}")
            except ValueError:
                print(f"Invalid column name: {column}")
        elif choice == '2':
            column = input("Enter the column name for which you want to find the maximum: ")
            try:
                maximum = find_maximum(column, data)
                print(f"Maximum {column}: {maximum}")
            except ValueError:
                print(f"Invalid column name: {column}")
        elif choice == '3':
            column = input("Enter the column name for which you want to find the minimum: ")
            try:
                minimum = find_minimum(column, data)
                print(f"Minimum {column}: {minimum}")
            except ValueError:
                print(f"Invalid column name: {column}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
