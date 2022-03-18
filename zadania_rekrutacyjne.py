# # odwracanie listy:
# lista1 = [-5,0,1,56,78,144,1212]
# print(lista1)
# lista1.reverse()
# print(lista1)

# sortowanie listy:
# lista2 = [242,2,29,-123,]
# print(lista2)
# lista2.sort()
# print(lista2)

# # slowniki:
# dict1 = {
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1997
# }
# print(dict1)
# dict1["year"] = 2019
# print(dict1)

# sortowanie babelkowe
def sortowanie_babelkowe(lista):
    n =len(lista)
    while n >1:
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l],lista[l+1] = lista[l+1],lista[l]
        n -=1
        print(lista)




print(sortowanie_babelkowe([2,5,20,1,-2,-8]))

