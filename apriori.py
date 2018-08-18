# алгоритм поиска математического супермножества
# возвращает множества {} в виде списка списков [[],...]
# для множества {'a', 'b', 'c', 'd'} вернет:
# [[], ['a'], ['b'], ['c'], ['d'], ['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd'], ['c', 'd'], ['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'b', 'c', 'd']]
# Статьи вдохновившие на написание алгоритма:
# https://devcolibri.com/%D0%BC%D0%BE%D0%B8-%D0%BB%D1%8E%D0%B1%D0%B8%D0%BC%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE/
# https://basegroup.ru/community/articles/apriori (помогла увидеть зависимость для алгоритма)
# цель применения пока не ясна (возможно, для тестирования по аргументам или графов)

a = set([chr(x) for x in range(ord('a'), ord('d')+1)]) # простое множество
a = [x for x in range(0,100)] # простое множество 1000 элементов - 20 секунд


def groups(lst, start):
	"""
	Возвращает подмножества супермножества начиная с 2-го размера
	Смешивает начало нового подмножества с каждым единичным элементам справа (основная логика)
	"""
	first=[] 
	for n in range(0, start):
		if len(lst)!=0:
			first+=[lst.pop(0)] # формирование начала подмножества
	return  ([first + [i] for i in lst]) # добавление концовок подмножества

def find_super_set(aset):
	"""
	Основной алгоритм поиска супермножества
	принимает простое множество set(...)
	"""
	# часть I
	result =[[]] # инициализация результата пустым "множеством"-списком
	lst = sorted(list(a)) # конвертирование множества в список
	count = len(lst) 	  # размер множества 
	for i in range(count): 
		result +=[[lst[i]]] # одиночные элементы

	# часть II	
	for k in range(1,count): # k+1-тые элементы
		copylst = list(lst) # сохранение копии (длительная операция копирования)
		part=groups(lst,k)
		while len(lst)!=0:
			result+=part
			part=groups(lst,k)
		lst=copylst
	return result

#print(a)
#print(find_super_set(a))
q=find_super_set(a)
print(len(q))