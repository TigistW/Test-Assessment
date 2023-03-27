# change elements of a string inot upper character, 
# if element is an alphabet else just continue with it.

def to_upper(string):
    if not isinstance(string, (str)):
        raise TypeError("inputs should be string")
    result = []
    for char in string:
        if 97 <= ord(char) <= 122:
            result.append(chr(ord(char) - 32))
        else:
            result.append(char)

    return "".join(result)

# change elements of a string inot small character, 
# if element is an alphabet else just continue with it.

def to_lower(string):
    if not isinstance(string, (str)):
            raise TypeError("inputs should be string")
    result = []
    for char in string:
        if 65 <= ord(char) <= 90:
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)
            
    return "".join(result)

#capitalizes the first letter of the string and lower the rest
def capitalize(string):
    if not isinstance(string, (str)):
        raise TypeError("inputs should be string")
    result = ""
    if string:
        result += to_upper(string[0])
        if len(string) > 1:
            result += to_lower(string[1:])
    return result
