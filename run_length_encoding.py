def get_size(your_str):
    counts_of_symbol = ''
    prev = ''
    final_counts = 0
    for i in range(len(your_str)):
        if i == 0:
            prev = your_str[0]
        else:
            try:
                this = int(your_str[i])
            except:
                this = your_str[i]
            if type(prev) is str and type(this) is str:
                final_counts += 1
                counts_of_symbol = ''
            elif type(prev) is int and type(this) is str:
                final_counts += int(counts_of_symbol)
                counts_of_symbol = ''
            else:
                counts_of_symbol += str(your_str[i])
            prev = this
    if type(prev) == int:
        final_counts += int(counts_of_symbol)
    else:
        final_counts += 1
    return final_counts


if __name__ == '__main__':
    print(get_size(input()))
