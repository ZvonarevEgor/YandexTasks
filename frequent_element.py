from collections import Counter


def input_array():
    n = int(input())
    a = [int(i) for i in input().split()]
    return a


def get_max_count(array):
    # The array can have the same number of some elements.
    same_counts = []
    result = (Counter(a).most_common(len(set(array))))
    max_count = result[0][1]
    for item in result:
        if max_count in item:
            same_counts.append(item[0])
    max_number = max(same_counts)
    return max_number


if __name__ == '__main__':
    a = input_array()
    print(get_max_count(a))
