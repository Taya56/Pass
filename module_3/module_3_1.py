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

    def is_contains(string, list_to_search):
        count_calls(calls)
        lst = {}
        for i in range(0, len(list_to_search)):
            if list_to_search[i] == string:
                lst[list_to_search[i]] = True
            else:
                lst[list_to_search [i]] = False
        counter = 0
        for i in lst:
            sorting = lst.get(i)
            if sorting == True:
                counter +=1
        if 1 == counter:
            return True
        else:
            return False

    print(string_info(string))
    print(is_contains(string, list_to_search))

