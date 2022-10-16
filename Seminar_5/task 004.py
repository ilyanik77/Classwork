# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.


    
list = [1, 5, 2, 3, 4, 6, 1, 7]
list_res=[]
for j in range(1, len(list)):
    list_temp = [list[0]]
    for i in range(j, len(list)):
        if list[i] > list_temp[-1]:
            list_temp.append(list[i])
    list_res.append(list_temp)
print(list, list_res)