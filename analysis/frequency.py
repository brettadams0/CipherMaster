from collections import Counter

def frequency_analysis(ciphertext):
    filtered_text = ''.join(filter(str.isalpha, ciphertext)).upper()
    return dict(Counter(filtered_text))
