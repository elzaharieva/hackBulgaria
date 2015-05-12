def count_substrings(haystack, needle):
    count = 0
    while haystack != "":  # ot 0 do 5
        if needle == haystack[:len(needle)]:
            count += 1
            haystack = haystack[len(needle):]
        else:
            haystack = haystack[1:]
    return count
