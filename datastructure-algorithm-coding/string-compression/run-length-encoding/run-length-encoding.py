def run_len_encode_str_compr (string):
    count = 1
    result = []
    for i in range(len(string)):
        if i == len(string) - 1:
            result.append([string[i], count])
        elif string[i] == string[i+1]:
            count += 1
        else:
            result.append([string[i], count])
            count = 1
