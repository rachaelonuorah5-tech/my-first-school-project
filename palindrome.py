def palindrome_checker(word):
    is_palindrome = True

    for number in range(len(word) // 2):
        if word[number] != word[len(word) - 1 - number]:
            is_palindrome = False
            break
    return is_palindrome

print(palindrome_checker("racecar"))
