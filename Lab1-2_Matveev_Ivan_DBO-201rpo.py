def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def unique_elements(lst):
    return list(set(lst))

def letter_frequency(s):
    return {char: s.count(char) for char in set(s)}

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = [x for x in lst[1:] if x < pivot]
    right = [x for x in lst[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

def sum_numbers_in_string(s):
    return sum(int(num) for num in s.split() if num.isdigit())

def list_to_dict(lst):
    return {item: lst.count(item) for item in lst}

def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes

def days_until(date_str):
    from datetime import datetime
    target_date = datetime.strptime(date_str, "%Y-%m-%d")
    today = datetime.today()
    delta = target_date - today
    return delta.days

def generate_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

def sort_by_two_keys(lst, key1, key2):
    return sorted(lst, key=lambda x: (x[key1], x[key2]))

def merge_lists(lst1, lst2):
    return list(set(lst1 + lst2))

def find_anagrams(word, word_list):
    from collections import Counter
    word_counter = Counter(word)
    return [w for w in word_list if Counter(w) == word_counter]

def count_unique_words(text):
    words = text.split()
    return len(set(words))

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

def compress_string(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{s[i - 1]}{count}")
            count = 1
    compressed.append(f"{s[-1]}{count}")
    return ''.join(compressed)

def substring_frequency(s, k):
    freq = {}
    for i in range(len(s) - k + 1):
        sub = s[i:i + k]
        freq[sub] = freq.get(sub, 0) + 1
    return freq

if __name__ == "__main__":
    print("1. Факториал числа:")
    print(factorial(5))
    print("\n2. Числа Фибоначчи:")
    print(fibonacci(10))
    print("\n3. Уникальные элементы:")
    print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
    print("\n4. Частота букв:")
    print(letter_frequency("hello world"))
    print("\n5. Переворот строки:")
    print(reverse_string("hello"))
    print("\n6. Проверка на палиндром:")
    print(is_palindrome("radar"))
    print("\n7. Быстрая сортировка:")
    print(quicksort([3, 6, 8, 10, 1, 2, 1]))
    print("\n8. Сумма чисел в строке:")
    print(sum_numbers_in_string("12 and 15 are numbers"))
    print("\n9. Словарь из списка:")
    print(list_to_dict(["apple", "banana", "apple", "orange", "banana", "banana"]))
    print("\n10. Простые числа до n:")
    print(sieve_of_eratosthenes(20))
    print("\n11. Дни до указанной даты:")
    print(days_until("2025-12-31"))
    print("\n12. Генерация пароля:")
    print(generate_password(12))
    print("\n13. Сумма квадратов:")
    print(sum_of_squares([1, 2, 3, 4, 5]))
    print("\n14. Сортировка по двум ключам:")
    sample_list = [{"a": 2, "b": 3}, {"a": 1, "b": 2}, {"a": 1, "b": 1}]
    print(sort_by_two_keys(sample_list, "a", "b"))
    print("\n15. Объединение списков:")
    print(merge_lists([1, 2, 3], [3, 4, 5]))
    print("\n16. Поиск анаграмм:")
    print(find_anagrams("listen", ["enlist", "google", "inlets", "banana"]))
    print("\n17. Подсчет уникальных слов:")
    print(count_unique_words("hello world hello"))
    print("\n18. Задача о рюкзаке:")
    print(knapsack([60, 100, 120], [10, 20, 30], 50))
    print("\n19. Сжатие строки:")
    print(compress_string("aaabbc"))
    print("\n20. Частота подстрок:")
    print(substring_frequency("abcabcabc", 3))
