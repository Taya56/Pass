calls = 0

while True:
    string = input("Введите слово: ")

    def count_calls(calls):
        calls += 1
        return calls
    
    def string_info(string):
        count_calls(calls)
        tuple = []
        for i in range(0, 3):
            tuple.append(i)
        tuple[0] = len(string)
        tuple[1] = string.upper()
        tuple[2] = string.lower()
        return tuple

    list_to_search = string_info(string)

    def is_contains(list_to_search, string):
        count_calls(calls)
        lst = {}
        for i in range(0, len(list_to_search)):
            if list_to_search[i] == string:
                lst[list_to_search[i]] = True
            else:
                lst[list_to_search[i]] = False
        calls_true = 0
        for i in lst:
            if lst[i] == True:
                calls_true +=1
            if lst[i] == 0:
                counter = string.lower()
                for i in range(0, len(list_to_search)):
                    if list_to_search[i] == counter:
                        calls_true +=1
        if calls_true >= 1:
            return True
        else:
            return False
    
    print(string_info(string))
    print(is_contains(list_to_search, string))
    print(calls)


