
def verify_anagrams(first_word, second_word):
	return sorted(first_word.replace(" ", "").lower()) == sorted(second_word.replace(" ", "").lower())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
