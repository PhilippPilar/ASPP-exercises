import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
Nr = comm.Get_size()

Ns = 20000 #number of elements to sum
Nsi = int(Ns/Nr)


if rank == 0:
	sum_arr = np.random.rand(Ns)*100
	#sum_arr = np.linspace(0,31,Ns)
	print(sum_arr)
	print(sum_arr.shape)
	print('sum_0:',np.sum(sum_arr))
	 
	for i in range(0,Nr):
		if i < Nr-1:
			comm.Send(sum_arr[Nsi*i:Nsi*(i+1)], dest = i+1)
		else:
			sarr = sum_arr[Nsi*i:]
					
if rank != 0:
	sarr = np.zeros(Nsi)
	comm.Recv(sarr,source = 0)
	rs = np.sum(sarr)
	comm.Send(rs,dest=0)
	
if rank == 0:
	S = np.sum(sarr)
	for j in range(1,Nr):
		rs = np.zeros(1)
		comm.Recv(rs,source=j)
		S += rs
	
	print('sum_final',S[0])

