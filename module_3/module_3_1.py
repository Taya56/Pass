calls = 0

def count_calls(calls):
    return calls

def string_info(string):
    global calls
    calls += 1
    tuple = (len(string), string.upper(), string.lower())
    return tuple

def is_contains(string, list_to_search):
    global calls
    calls += 1
    for i in list_to_search:
        tuple = []
        tuple.append(i.lower())
    if string.lower() in tuple:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



