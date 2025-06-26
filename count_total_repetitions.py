"""
Given a paragraph, identify all words that are repeated. 
For each repeated word appearing n times, count the repetitions as n - 1. 

Return only the total sum of all these repetition counts as an integer.

Example:
Input: "Wow! Wow! Wow! This is amazing, amazing—truly incredible!"
Output: 3
"""
import re
from collections import Counter
def count_total_repetitions(paragraph: str) -> int:
    clean_string = re.findall(r'\w+', para)
    word_count = Counter(clean_string)
    total_sum = sum((count-1) for count in word_count.values() if count >1)
    return(total_sum)

para="Wow! Wow! Wow! This is amazing, amazing—truly incredible!Given a paragraph, identify all words that are repeated consecutively.For each repeated word appearing n times consecutively, count the repetitions"
print(count_total_repetitions(para))