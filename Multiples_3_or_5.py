def solution(number):
    lst35 = []
    for x in range(1,number):
        if x%3==0:
            lst35.append(x)
        elif x%5==0:
            lst35.append(x)
    return sum(lst35)
  