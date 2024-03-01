is_palindrome = lambda s: s == s[::-1]

original_list = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palindromes = list(filter(is_palindrome, original_list))

print("Original list of strings:", original_list)
print("List of palindromes:", palindromes)
