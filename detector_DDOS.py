from collections import Counter


# Get the conditions and fill the array.
def input_info():
    a = []
    n = int(input())
    m = int(input())
    k = int(input())
    for i in range(n):
        a.append(input())
    return a, n, m, k


# Pass through the array checking the M elements for shift.
def several_indexes(m, this_index):
    list_with_indexes = []
    for i in range(m):
        list_with_indexes.append(i + this_index)
    return list_with_indexes


# Get bad addresses from M elements.
def get_bad_ip(m_elements, k):
    bad_ip = []
    result = Counter(m_elements).most_common(len(m_elements))
    for ip in result:
        if ip[1] >= k:
            bad_ip.append(ip[0])
    return bad_ip


# Addresses in this list can be repeated.
def get_m_elements(a, n, m, this_index):
    m_elements = []
    list_with_indexes = several_indexes(m, this_index)
    for index in list_with_indexes:
        if index < n:
            m_elements.append(a[index])
    return m_elements



# Get bad addresses from the whole array, eliminating repetition.
def get_final_list(a, n, m, k):
    final_ip_list = []
    for i in range(len(a)):
        m_elements = get_m_elements(a, n, m, i)
        list_with_bad_ip = (get_bad_ip(m_elements, k))
        for ip in list_with_bad_ip:
            if ip not in final_ip_list:
                final_ip_list.append(ip)
    return final_ip_list

def output_info(ip_list):
    output = ''
    for ip in ip_list:
        output += '{}\n'.format(ip)
    return output


def main():
    a, n, m, k = input_info()
    bad_ip_list = get_final_list(a, n, m, k)
    bad_ip_list.sort(key=lambda element: int(element[-1]))
    output_str = output_info(bad_ip_list)
    return output_str


if __name__ == '__main__':
    print(main())



