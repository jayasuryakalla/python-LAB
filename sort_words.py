def sort_words_in_file(source_file, output_file):
    try:
        with open(source_file, 'r') as file:
            words = file.read().split()
        lower_case_words = [word.lower() for word in words]
        sorted_words = sorted(set(lower_case_words))
        with open(output_file, 'w') as file:
            for word in sorted_words:
                file.write(f"{word}\n")
        print(f"Sorted words written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

sort_words_in_file('source_file.txt', 'output_file.txt')