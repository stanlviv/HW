def list_animals(animals):
    result = ''
    for x in range(len(animals)):
        result += "{}. {}\n".format(x+1, animals[x])
    return result