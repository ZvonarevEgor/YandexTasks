# Get the conditions and fill the array.
def input_info():
    a = []
    n = int(input())
    m = int(input())
    k = int(input())
    for i in range(n):
        a.append(input())
    return a, n, m, k


def main(array, m, n, k):
    bad_ip = set()
    for i, ip in enumerate(array):
        if ip in bad_ip:
            continue
        count = 1
        for idx in range(i + 1, min(i + m, len(array))):
            if ip == array[idx]:
                count += 1
        if count >= k:
            bad_ip.add(ip)
    bad_ip = sorted(bad_ip)
    return bad_ip


if __name__ == '__main__':
    a, n, m, k = input_info()
    bad_ip = main(a, n, m, k)
    print(bad_ip, sep='\n')

