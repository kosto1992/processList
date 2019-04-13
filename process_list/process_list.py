def process_list(input_list):
    positive_sum = 0
    negative_count = 0
    try:
        for num in input_list:
            num = int(num)
            if num < 0:
                negative_count += 1
            else:
                positive_sum += num
    except Exception:
        print("Wrong intput")
        return []
    return [positive_sum, negative_count]
