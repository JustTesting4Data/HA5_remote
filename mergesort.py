def merge_sort(list_to_sort):
	#Mergesort zerlegt alle Listen in Listen der Länge 1
    if (len(list_to_sort) > 1):
    
        mid = len(list_to_sort) // 2
        left_list = list_to_sort[:mid]
        right_list = list_to_sort[mid:]
	#die sukzessive Zerlegung erfolgt über Rekursion
        merge_sort(left_list)
        merge_sort(right_list)
	#Indizes der Listen: l für left, r für right und i für die zu bearbeitende Liste
        l = 0
        r = 0
        i = 0
	
	#nach der Rekursion werden die Teillisten in umgekehrter Reihenfolge wieder zusammengefügt und dabei sortiert
	#solange beide Listen Elemente enthalten, werden sukzessive die beiden durch l,r indizierten Elemente verglichen und das jeweils kleinere Element übernommen
        while l < len(left_list) and r < len(right_list):
            if left_list[l] <= right_list[r]:
                list_to_sort[i] = left_list[l]
                l += 1
            else:
            	list_to_sort[i] = right_list[r]
            	r += 1
            i += 1
	#wenn eine der zu mergenden Listen leer ist, wird der Rest der anderen Liste, falls nicht leer, übernommen
        while l < len(left_list):
            list_to_sort[i] = left_list[l]
            l += 1
            i += 1

        while r < len(right_list):
            list_to_sort[i] = right_list[r]
            r += 1
            i += 1


#Test
import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list)) 

plt.scatter(x, my_list)
plt.bar(x, my_list, width=0.16, align='center', alpha=0.5)
plt.xlabel('Indices')
plt.ylabel('List values')
plt.title('Unsorted List Values vs. Indices')
plt.grid(lw=.7)
plt.show()

merge_sort(my_list)

plt.scatter(x, my_list)
plt.bar(x, my_list, width=0.16, align='center', alpha=0.5)
plt.xlabel('Indices')
plt.ylabel('List values')
plt.title('Sorted List Values vs. Indices')
plt.grid(lw=.7)
plt.show()
