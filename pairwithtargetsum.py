import itertools
class FindPairsWithSum:


    def itertools_implementation(self, arr, n, target):
        all_pairs = itertools.combinations(arr, 2)
        result = [pair for pair in all_pairs if sum(pair)==target]
        return result


    def set_implementation(self, arr, n, target):
        result = []
        seen = set()
        for value1 in arr:
            value2 = target - value1
            if value2 in seen:
                result.append((value1, value2))
            seen.add(value1)
        return result

    def list_traversal(self, arr, n, target):
        # Write your code here

        has_pairs = []
        right_pointer = 0
        left_pointer = len(arr)
        while left_pointer > right_pointer:
            total_sum = 0
            temp_arr = arr[:left_pointer]
            for i in range(right_pointer, left_pointer-1, 1):
                total_sum = temp_arr[i] + temp_arr[left_pointer-1]
                if total_sum == target:
                    has_pairs.append((temp_arr[i], temp_arr[left_pointer-1]))
                    break
            left_pointer -= 1
        if len(has_pairs) >= 1:
            return True
        else:
            return False


if __name__ == "__main__":
    finder = FindPairsWithSum()
    arr = [-2, -1, 5, 13, 17, 25, 40]
    target = 30
    # result = finder.list_traversal(arr, 5, target)
    # result = finder.set_implementation(arr, 5, target)
    result = finder.itertools_implementation(arr, 5, target)
    print(result)
