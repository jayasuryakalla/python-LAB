def print_lines_in_reverse(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        for line in lines:
            print(line.strip()[::-1])
    except Exception as e:
        print(f"An error occurred: {e}")
file_name = 'input.txt'
print_lines_in_reverse(file_name)