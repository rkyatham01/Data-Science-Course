import numpy as np
a = np.array([5,6,9])
a = np.array([[1,2], [3,4], [5,6]], dtype=np.float64) # 2 dimensional np array
a.ndim #gets whats the dimensions
a.itemsize #gets total number of elements (int : 4 bytes)
a.size #total number of elements
a.shape #provides information on dimensions
zeroArr = np.zeros((3,4)) #provide it dimensions to get 0 array
oneArr = np.ones((3,4)) #provide it dimensions to get 0 array
arrRange = np.arange(1,5,2) #creates arrays from 1-4 (Inclusive), 3rd parameter is the step
linSpaceArr = np.linspace(1,5,10) #linear spaces numbers inbetween (from 1-5)
reShapeArr = a.reshape(2,3) #reshapes it into other dimensions as long as total dimensions match 2d : 2d ; 3d : 3d
flattenArr = a.ravel() #flattens array to 1 dimension
colArrSummed = a.sum(axis=1)
rowArrSummed = a.sum(axis=0)
#multiply, add , a.dot which is multiplying by dot product can be done
#just have to make sure the dimensions match