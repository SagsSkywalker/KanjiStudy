import random
import decimal as dc
import math as m

def main():
	######################################################
	#	Variables de entorno
	######################################################
	records = readDataBase('bezdekIris.data.txt')
	#Se crea una matriz del tamaño suficiente para alojar
	#los valores de la BD
	items = getValuesMatrix(len(records), 4, records)
	#Centroides e iteraciones
	centroids = [0]
	i = 0
	weights = 0
	dp = 0
	x = 0
	highestWeight = 0

	######################################################
	#	Variables de entorno
	######################################################

	######################################################
	#	Developement
	######################################################

	print('Centroids:', end='\t')
	#Se selecciona el número de centroides deseado
	#aleatoriamente y se regresa un arreglo con los
	#números de los centroides
	centroids = getWeightsPosition(len(records))
	print('Iterations:', end='\t')
	i = input()

	#Se asigna un namaño apropiado para alojar los
	#valores de los pesos según los centroides aleatorios
	#generados anteriormente
	weights = [[0 for i in range(4)] for j in range(len(centroids))]
	dp = weights

	#Obtener los pesos según los indices de los centroides 
	#que se eligieron aleatoriamente
	for ix, x in enumerate(centroids):
		for y in range(4):
			weights[ix][y] = items[x][y]

	for n in range(int(i)):		
		#Se asigna un valor a x obteniendo aleatoriamente
		#de la base de datos un registro
		x = getRandomX(items)

		#Se calcula el producto punto de cada uno de los
		#registros de los pesos seleccionados con x
		dp = dotProduct(weights, x)

		#Se obtiene el índice del peso mayor a partir del
		#producto punto y la suma de cada registro en la lista
		#del mismo
		highestWeight = getHighestWeight(dp, weightsSum(dp))

		#print(f'weights =\t{weights}\nX =\t\t{x}\ndotProd =\t{dp}\nhighest =\t{weights[highestWeight]}\n')

		#Se hace la suma del peso mayor con x, respectivamente,
		#y se asigna el nuevo valor (normalizado) al peso en la 
		#lista de pesos
		weights[highestWeight] = sumHighestAndX(weights[highestWeight], x)
	print(f'{weights}\nOK')

	######################################################
	#	Developement
	######################################################

#Se lee el archivo txt de la base de datos
#y se retorna un array con las lineas que contiene
#la BD. El parámetro name recibe el nombre del
#documento que se leerá
def readDataBase(name):
	t = open(str(name), "r")
	return t.readlines()

#Se obtienen los valores de un arreglo con los registros
#de la base de datos. El parámetro rows es para asignar
#un número de filas al arreglo, cols se usa para asignar
#un número de columnas al arreglo, records es un arreglo
#que contiene los registros de la BD
def getValuesMatrix(rows, cols, records):
	#Se crea la matriz de rows x cols
	items = [[0 for i in range(cols)] for j in range(rows)]
	for x in range(rows):
		#Se obtienen los registros uno a uno y se guardan
		#en record
		record = records[x].split(',')
		for y in range(cols):
			#Se asigna el valor de record a la matriz
			#según su posición *no se ordena*
			items[x][y] = float(record[y])
	#Una vez construida la matriz, se retorna con todos
	#los registros
	return items

#Se selecciona un número al azar el número de veces
#específicado para obtener los centroides
def getRandom(lenght):
	return random.randint(0,int(lenght-1))

def getWeightsPosition(lenght):
	number = input()
	weights = [0]*int(number)
	for x in range(int(number)):
		weights[x] = getRandom(lenght)
	return weights

def getRandomX(records):
	random = getRandom(len(records))
	x = [0 for i in range(4)]
	for i in range(len(x)):
		x[i] = float(records[random][i])
	return x

def dotProduct(w, x):
	result = [[0 for i in range(len(x))] for j in range(len(w))]
	for i in range(len(w)):
		for j in range(4):
			result[i][j] = (float(w[i][j]) * float(x[j]))
	return result

def weightsSum(dp):
	result = [[0] for i in range(4)]
	result = [sum(x) for x in dp]
	return result

def getHighestWeight(dp, wsum):
	x = max(wsum)
	for ix, i in enumerate(wsum):
		if i == x:
			return ix

def sumHighestAndX(highest, x):
	result = [0 for i in range(len(x))]
	for ix, i in enumerate(highest):
		result[ix] = (float(i) + float(x[ix]))
	return normalize(result)

def normalize(arr):
	square = []
	[square.append(pow(i, 2)) for i in arr]
	square = float(m.sqrt(sum(square)))
	for ix, i in enumerate(arr):
		arr[ix] = (float(i) / float(square))
	return arr

#def quickSort(arr):
#	if len(arr) == 0:
#		return []
#	left = []
#	right = []
#	p = [arr[0]]
#
#	for i in range(1, len(arr)):
#		left.append(arr[i]) if arr[i] < p[0] else right.append(arr[i])
#
#	return quickSort(left) + p + quickSort(right);

if __name__ == '__main__':
	main()