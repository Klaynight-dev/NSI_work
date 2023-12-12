def reverse(tableau, start=0, end=None):
    """Prend un tableau rager dans l'ordre """
    print(f'tab={tableau}, start={start}, end={end}')
    if end is None:
        end = len(tableau) - 1
    if start >= end:
        return tableau
    tableau[start], tableau[end] = tableau[end], tableau[start]
    return reverse(tableau, start + 1, end - 1)

tab=[1,2,3,4,5,6,7,8,9]
reverse(tab)
print(tab)