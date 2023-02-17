import sys

def str_to_groups(string, group_size):
    return [string[i:i+group_size] for i in range(0, len(string), group_size)]

def perform_xor(string_groups):
    while len(string_groups) > 1:
        new_groups = []
        for i in range(0, len(string_groups), 2):
            if i+1 < len(string_groups):
                new_groups.append(int(string_groups[i], 16) ^ int(string_groups[i+1], 16))
            else:
                new_groups.append(int(string_groups[i], 16))
        string_groups = new_groups
    return string_groups[0]

def perform_nearby_xor(string, group_size, step=1):
    string_groups = str_to_groups(string, group_size)
    result = 0
    for i in range(0, len(string_groups)-step, step):
        group_a = string_groups[i]
        group_b = string_groups[i+step]
        result ^= perform_xor([group_a, group_b])
    return result

def text_to_dec_groups(text):
    # Convert text string to decimal string
    dec_string = ''.join(str(ord(c)) for c in text)
    
    # Group decimal string into chunks of 8
    dec_groups = [dec_string[i:i+8] for i in range(0, len(dec_string), 8)]
    
    return dec_groups

def apply_function_to_groups(groups, func):
    # Apply the given function to each group and convert the result to a string
    results = [str(format(func(int(group)), '.50f'))[25:] for group in groups]
    
    return results

def text_to_result(text, func):
    # Convert text to decimal groups
    dec_groups = text_to_dec_groups(text)
    
    # Apply the function to each decimal group
    results = apply_function_to_groups(dec_groups, func)
    
    # Join the results into a single string and return it
    return ''.join(results)

text = ""
for line in sys.stdin:
    text = text + line

result = text_to_result(text, lambda n: (n*(n*25))%(n/(n*25)))
string = result
group_size = int(sys.argv[1])
result = perform_nearby_xor(string, group_size)
#print(result)
print(hex(result))
