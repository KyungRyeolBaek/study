def solution(n, arr1, arr2):
    return [((n-len(format(i|j, 'b')))*'0'+format(i|j, 'b')).replace('1', '#').replace('0', ' ') for i, j in zip(arr1, arr2)]
