def reverse(*input):
    i = len(input)
    result = []

    while i >= 1:
        result.append(input[i-1])
        i = i - 1

    print(result)

reverse(1, 3, 6, 8, 13)