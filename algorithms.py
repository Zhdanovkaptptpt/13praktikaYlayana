from exceptions import EmptyDataError, InvalidValueError, UnknownAlgorithmError


class BubbleSort:
    def __init__(self, data):
        self.data = data
    def sort(self):
        arr = self.data[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

class SelectionSort:
    def __init__(self, data):
        self.data = data
    def sort(self):
        arr = self.data[:]
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

class QuickSort:
    def __init__(self, data):
        self.data = data
    def sort(self):
        arr = self.data[:]
        def _qs(items):
            if len(items) <= 1:
                return items
            pivot = items[len(items)//2]
            left  = [x for x in items if x < pivot]
            mid   = [x for x in items if x == pivot]
            right = [x for x in items if x > pivot]
            return _qs(left) + mid + _qs(right)
        return _qs(arr)
def create_algorithm(name, data):
    if not data:
        raise EmptyDataError()
    if not all(isinstance(x, (int, float)) for x in data):
        raise InvalidValueError()

    algorithms = {
        "bubble":    BubbleSort,
        "selection": SelectionSort,
        "quick":     QuickSort
    }
    if name not in algorithms:
        raise UnknownAlgorithmError()

    return algorithms[name](data)
