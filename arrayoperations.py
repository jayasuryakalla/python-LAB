def display_array(arr):
    print("Current array:", arr)
def append_to_array(arr, item):
    arr.append(item)
    print(f"Appended '{item}' to the array.")
def insert_to_array(arr, index, item):
    arr.insert(index, item)
    print(f"Inserted '{item}' at index {index}.")
def reverse_array(arr):
    arr.reverse()
    print("Reversed the array.")
def main():
    array = []
    display_array(array)
    append_to_array(array, 'apple')
    append_to_array(array, 'banana')
    display_array(array)
    insert_to_array(array, 1, 'orange')
    display_array(array)
    reverse_array(array)
    display_array(array)
if __name__ == "__main__":
    main()