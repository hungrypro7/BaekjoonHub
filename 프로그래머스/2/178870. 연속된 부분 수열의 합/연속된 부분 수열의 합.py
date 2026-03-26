def solution(sequence, k):
    left = 0
    current_sum = 0
    best_len = float('inf')
    answer = [0, 0]

    for right in range(len(sequence)):
        current_sum += sequence[right]

        while current_sum > k:
            current_sum -= sequence[left]
            left += 1

        if current_sum == k:
            if right - left < best_len:
                best_len = right - left
                answer = [left, right]

    return answer