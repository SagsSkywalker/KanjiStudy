from PIL import Image as image
import numpy as np
import matplotlib.pyplot as plt
import random as rand
import math as m

def main():
	im = image.open('jaus.jpg')
	imarr = np.array(im, dtype=np.float32)
	dp = 0
	cent = 0
	
	######################################################
	#	Developement
	######################################################

	print('Centroids:', end='\t')
	#Se selecciona el número de centroides deseado
	#aleatoriamente y se regresa un arreglo con los
	#números de los centroides
	centroids = input()
	print('Iterations:', end='\t')
	itera = input()

	cent = [[0 for i in range(3)] for i in range(int(centroids))]
	cent = getCentroids(cent, imarr)

	print(cent)

	for n in range(int(itera)):		
		#Se asigna un valor a x obteniendo aleatoriamente
		#de la base de datos un registro
		x = imarr[rand.randint(0, int(len(imarr)-1))][rand.randint(0, int(len(imarr[0])-1))]

		#Se calcula el producto punto de cada uno de los
		#registros de los pesos seleccionados con x
		dp = [[0 for x in range(len(cent[0]))] for y in range(len(cent))]
		for i in range(len(cent)):
			for j in range(len(x)):
				dp[i][j] = cent[i][j] * x[j]

		#Se obtiene el índice del peso mayor a partir del
		#producto punto y la suma de cada registro en la lista
		#del mismo
		highestWeight = getHighestWeight(dp, weightsSum(dp))

		#print(f'weights =\t{weights}\nX =\t\t{x}\ndotProd =\t{dp}\nhighest =\t{weights[highestWeight]}\n')

		#Se hace la suma del peso mayor con x, respectivamente,
		#y se asigna el nuevo valor (normalizado) al peso en la 
		#lista de pesos
		cent[highestWeight] = sumHighestAndX(cent[highestWeight], x)

	#DP para ver a que grupo se pertenece
	rgb = [[0 for i in range(3)] for i in range(int(centroids))]
	ite = [0 for i in range(int(centroids))]
	rgb = np.array(rgb, dtype=np.float32)
	ite = np.array(ite, dtype=np.float32)
	actual = [0 for i in range(3)]
	for i in range(len(imarr)):
		for j in range(len(imarr[0])):
			actual = imarr[i][j]
			for k in range(len(cent)):
				for l in range(len(cent[0])):
					dp[k][l] = cent[k][l] * actual[l]
			highestWeight = getHighestWeight(dp, weightsSum(dp))
			rgb[highestWeight] += actual
			ite[highestWeight] += 1.0

	for i in range(len(rgb)):
		for j in range(len(rgb[0])):
			rgb[i][j] = rgb[i][j] / ite[i]

	for i in range(len(imarr)):
		for j in range(len(imarr[0])):
			actual = imarr[i][j]
			for k in range(len(cent)):
				for l in range(len(cent[0])):
					dp[k][l] = cent[k][l] * actual[l]
			highestWeight = getHighestWeight(dp, weightsSum(dp))
			imarr[i][j] = rgb[highestWeight]

	im = image.fromarray(imarr.astype(np.uint8))
	plt.figure()
	plt.imshow(im)
	plt.show()


	######################################################
	#	Developement
	######################################################

def getCentroids(cent, arr):
	for i in range(len(cent)):
		cent[i] = arr[rand.randint(0, int(len(arr)-1))][rand.randint(0, int(len(arr[0])-1))]
	return cent

def weightsSum(dp):
	result = [[0] for i in range(3)]
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
	square = m.sqrt(sum(square))
	for ix, i in enumerate(arr):
		arr[ix] = (float(i) / float(square))
	return arr

	print(im.size)
	#im.show()


if __name__ == '__main__':
	main()