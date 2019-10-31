#!/usr/bin/env python
import copy


def quick_sorted(raw_list):
    sorted_list = copy.deepcopy(raw_list)

    def _partition(data, start, end):
        pivot = start
        for i in range(start + 1, end + 1):
            if data[i] <= data[start]:
                pivot += 1
                data[i], data[pivot] = data[pivot], data[i]
        data[pivot], data[start] = data[start], data[pivot]
        return pivot

    def _quick_sort(data, start, end):
        if start >= end:
            return
        pivot = _partition(data, start, end)
        _quick_sort(data, start, pivot - 1)
        _quick_sort(data, pivot + 1, end)

    _quick_sort(sorted_list, 0, len(sorted_list) - 1)
    return sorted_list


if __name__ == '__main__':
    test_data = [1, 22, 15, 3, 19, 55, -5, 78, -65, 33, -33]
    print(f"Test data: {test_data}")
    print(f"Sorted data: {quick_sorted(test_data)}")
