def compute_file_statistics(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = 0
            num_characters = 0
            
            for line in lines:
                num_words += len(line.split())
                num_characters += len(line)
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_characters}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = 'textfile.txt'
compute_file_statistics(file_name)
