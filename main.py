from process_list.process_list import process_list

if __name__ == "__main__":
    # Write input, e.g: 1,2,3,-4,-5
    input_list = eval(input("Write list of numbers."))
    print(process_list(input_list))
