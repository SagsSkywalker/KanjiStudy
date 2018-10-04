import random

def main():
	######################################################
	#	Variables de entorno
	######################################################
	records = readDataBase('bezdekIris.data.txt')
	#Se crea una matriz del tamaño suficiente para alojar
	#los valores de la BD
	items = getValuesMatrix(len(records), 4, records)
	#Se selecciona el número de centroides deseado
	#aleatoriamente
	print('Centroids:', end='\t')
	centNumber = input()
	print('Iterations:', end='\t')
	Iterations = input()
	

	######################################################
	#	Variables de entorno
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
	items = [[0]*cols]*rows
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
	return random.randint(1,int(lenght))

if __name__ == '__main__':
	main()