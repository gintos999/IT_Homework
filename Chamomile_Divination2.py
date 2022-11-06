def chamomile_divine(petal_numbers, divination_start):
    ans = []
    total = sum(petal_numbers)
    for i in range(total // 2):
        if divination_start == 'любит':
            ans.append('любит')
            ans.append('не любит')
        else:
            ans.append('не любит')
            ans.append('любит')
    if total % 2 == 1:
        if ans[-1] == 'любит':
            ans.append('не любит')
        else:
            ans.append('любит')
    return ans




for guess in chamomile_divine(petal_numbers=[5, 2, 3], divination_start="не любит"):
    print(guess)
