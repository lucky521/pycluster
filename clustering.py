# --coding=utf8-- 
# TODO:input 
cluster_num = 2
v_num = 60
filename = "vector"+ str(v_num) +".txt"
########################################################################
import math
import numpy
from numpy.random import random
import scipy
import sklearn
########################################################################
# compute similarity of two vectors
def get_distance(v1, v2):
	dis = 0.0
	if v1 == v2:
		return dis
	if len(v1) != len(v2):
		print 'Error input!!!'
	for i in range(0, len(v1)):
		dis += (v1[i]-v2[i])*(v1[i]-v2[i])
	dis = math.sqrt(dis)
	return dis
########################################################################
f1 = file(filename)
v_matrix = []
for line in f1:
	v_tmp = line.split(" ")
	v1 = []
	for i in v_tmp:
		if len(i) > 2:
			v1.append(float(i))
	v_matrix.append(v1)
f1.close()

print "向量的个数 ", str(len(v_matrix))
print "每个向量的维度 ", str(len(v_matrix[0]))
########################################################################
dis_m = []
for j in range(0, v_num):
	row = []
	for i in range(0, v_num):
		tmp_dis = get_distance(v_matrix[j], v_matrix[i])
		row.append(tmp_dis)
	dis_m.append(row)
source = numpy.array(dis_m)
########################################################################
'''
source = numpy.array([
			[0.0, 1.0, 5.0, 7.0, 9.0],
			[1.0, 0.0, 5.0, 7.0, 9.0],
			[5.0, 5.0, 0.0, 5.0, 5.0],
			[7.0, 7.0, 5.0, 0.0, 1.0],
			[9.0, 9.0, 5.0, 1.0, 0.0],
			])
'''
# 将二维数组形式的矩阵表达 转换为 (x,y)->value形式的矩阵表达
s = scipy.sparse.coo_matrix(source)
data = s.tocsr()
#print data
#########################################################################
def one_cluster(Algorithm):
	print "Algorithm = " + str(Algorithm)
	# 编号对应的算法在注释里面
	if Algorithm == 1:  #KMeans
		kmeans = sklearn.cluster.KMeans(n_clusters=cluster_num, n_init=10)
		kmeans.fit(data)
		cluster = kmeans.predict(data)
	
	elif Algorithm == 2: #MeanShift
		meanshift = sklearn.cluster.MeanShift()
		meanshift.fit(source)
		cluster = meanshift.predict(source)
	
	elif Algorithm == 3: #AgglomerativeClustering
		agg = sklearn.cluster.AgglomerativeClustering(n_clusters=cluster_num)
		agg.fit(source)
		cluster = agg.fit_predict(source)
	
	elif  Algorithm == 4: #DBSCAN
		kmeans = sklearn.cluster.DBSCAN()
		kmeans.fit(source)
		cluster = kmeans.fit_predict(source)
	
	elif  Algorithm == 5:  #SpectralClustering
		kmeans = sklearn.cluster.SpectralClustering(n_clusters=cluster_num)
		kmeans.fit(source)
		cluster = kmeans.fit_predict(source)
	
	elif  Algorithm == 6: #Birch
		kmeans = sklearn.cluster.Birch(n_clusters=cluster_num)
		kmeans.fit(source)
		cluster = kmeans.fit_predict(source)
	
	elif  Algorithm == 7: #AffinityPropagation
		kmeans = sklearn.cluster.AffinityPropagation()
		kmeans.fit(source)
		cluster = kmeans.fit_predict(source)
	#########################################################################
	# 输出结果
	print "Clustering Result:"
	result = ""
	for i in range(0, len(cluster)):
		result += str(i) + "("+ str(cluster[i]) +")" + "  \n"
	
	print result
	file_result = file(filename[:-4] + "_Algorithm_" + str(Algorithm) + "_result.txt","w")
	file_result.write(result)
	file_result.close()


for i in range(1,8):
	one_cluster(i)
