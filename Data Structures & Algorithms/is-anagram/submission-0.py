class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Create hashmap where the letters will be counted as key and value
        #We can use length to eliminate cases when the words have different sizes
        len_s = len(s)
        len_t = len(t)
        if(len_s != len_t):
            return False

        dictionary = {}
        #Countingt all letters in the first word
        for letter in s:
            if letter not in dictionary:
                dictionary[letter] = 1
            else:
                dictionary[letter] += 1
        #Counting letters in the second word
        for letter in t:
            if letter not in dictionary:
                return False
            else:
                dictionary[letter] -= 1
        
        for key in dictionary:
            if dictionary.get(key) != 0:
                return False
        
        return True
        