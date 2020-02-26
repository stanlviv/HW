sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps(sheep):
    tr = []
    for t in sheep:
        if t == True:
            tr.append(t)
    tr = len(tr)
    return tr
  