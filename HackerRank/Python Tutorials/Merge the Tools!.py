def merge_the_tools(string, k):
    for i in range (0, len(string), k):
        text = string[i:i+k]
        seen = set()
        for word in text:
            if word not in seen:
                print (word, end="")
                seen.add(word)

        print ()



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)