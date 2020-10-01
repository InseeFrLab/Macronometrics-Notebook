import numpy as np
from math import log, exp

import numpy as np

# Nombre de blocs du modèle
n_blocks = 27 

# Liste des noms de variables
coln = ['compet', 'd11_d5_cale', 'd41_s14s3_cale', 'd4z_s14s3_cale', 'd5_s143_cale', 'emps_d7_cale', 'p3a_d5_cale', 'p3g_d5_cale', 'p3m_d1_cale', 'p3m_d5_cale', 'p51g_d5_cale', 'p51m_d1_cale', 'p51m_d5_cale', 'p51t_d1_cale', 'p51t_d5_cale', 'p523_d1_cale', 'p523_d3_cale', 'p6_d1_cale', 'p6_d5_cale', 'p7_d1_cale', 'p7_d5_cale', 'pint_d5_cale', 'tc_d11_d3', 'tc_d11_s14r3', 'tc_d1_d3', 'tc_d61s_s14e3', 'tc_d62_s14r3', 'tc_d7_s14s3', 'tc_emp_d1', 'tc_uc_d5', 'tc_ulc_d5', 'tcho', 'td_b2_s143', 'td_b6_s143', 'td_b6_s143a', 'td_b6taxable_s14r3', 'td_dint_d1', 'td_dint_dhs1', 'td_p3a_d1', 'td_p3a_d3', 'td_p3g_d3', 'td_p3m_d3', 'td_p51_d1', 'td_p51_d3', 'td_p51_d5', 'td_p51g_d3', 'td_p51m_d3', 'td_p51t_d3', 'td_p6_d3', 'td_p7_d3', 'td_pib1', 'td_pib3', 'td_pib5', 'td_ratio_p7', 'b2_part', 'ct_d61ss14', 'ct_tdp3ad3', 'demmon', 'dum_1982q1', 'dum_1982q3', 'dum_1983q1', 'dum_1984q1', 'dum_1990q1', 'dum_1999q4', 'inter', 'pd7s14', 'petfm', 'petfx', 'r10a', 'r3m', 'ratio_d11', 'ratio_d29_39', 'ratio_part', 'ratio_soc', 'tc_d11_d5', 'tc_d41_s14s3', 'tc_d4z_s14s3', 'tc_d5_s14e3', 'tc_d62_s14r1', 'tc_empns_d1', 'tc_emps_d7', 'tc_ls_d1', 'td_p3a_d5', 'td_p3g_d1', 'td_p3g_d5', 'td_p3m_d1', 'td_p3m_d5', 'td_p51g_d1', 'td_p51g_d5', 'td_p51m_d1', 'td_p51m_d5', 'td_p51t_d1', 'td_p51t_d5', 'td_p523_d1', 'td_p523_d3', 'td_p6_d1', 'td_p6_d5', 'td_p7_d1', 'td_p7_d5', 'td_pint_d5', 'time', 'trim1', 'trim2', 'trim3', 'trim4', 'tuc'] 

# Dictionnaire de correspondance des noms de variables
dicovar = {'compet': 0, 'd11_d5_cale': 1, 'd41_s14s3_cale': 2, 'd4z_s14s3_cale': 3, 'd5_s143_cale': 4, 'emps_d7_cale': 5, 'p3a_d5_cale': 6, 'p3g_d5_cale': 7, 'p3m_d1_cale': 8, 'p3m_d5_cale': 9, 'p51g_d5_cale': 10, 'p51m_d1_cale': 11, 'p51m_d5_cale': 12, 'p51t_d1_cale': 13, 'p51t_d5_cale': 14, 'p523_d1_cale': 15, 'p523_d3_cale': 16, 'p6_d1_cale': 17, 'p6_d5_cale': 18, 'p7_d1_cale': 19, 'p7_d5_cale': 20, 'pint_d5_cale': 21, 'tc_d11_d3': 22, 'tc_d11_s14r3': 23, 'tc_d1_d3': 24, 'tc_d61s_s14e3': 25, 'tc_d62_s14r3': 26, 'tc_d7_s14s3': 27, 'tc_emp_d1': 28, 'tc_uc_d5': 29, 'tc_ulc_d5': 30, 'tcho': 31, 'td_b2_s143': 32, 'td_b6_s143': 33, 'td_b6_s143a': 34, 'td_b6taxable_s14r3': 35, 'td_dint_d1': 36, 'td_dint_dhs1': 37, 'td_p3a_d1': 38, 'td_p3a_d3': 39, 'td_p3g_d3': 40, 'td_p3m_d3': 41, 'td_p51_d1': 42, 'td_p51_d3': 43, 'td_p51_d5': 44, 'td_p51g_d3': 45, 'td_p51m_d3': 46, 'td_p51t_d3': 47, 'td_p6_d3': 48, 'td_p7_d3': 49, 'td_pib1': 50, 'td_pib3': 51, 'td_pib5': 52, 'td_ratio_p7': 53, 'b2_part': 54, 'ct_d61ss14': 55, 'ct_tdp3ad3': 56, 'demmon': 57, 'dum_1982q1': 58, 'dum_1982q3': 59, 'dum_1983q1': 60, 'dum_1984q1': 61, 'dum_1990q1': 62, 'dum_1999q4': 63, 'inter': 64, 'pd7s14': 65, 'petfm': 66, 'petfx': 67, 'r10a': 68, 'r3m': 69, 'ratio_d11': 70, 'ratio_d29_39': 71, 'ratio_part': 72, 'ratio_soc': 73, 'tc_d11_d5': 74, 'tc_d41_s14s3': 75, 'tc_d4z_s14s3': 76, 'tc_d5_s14e3': 77, 'tc_d62_s14r1': 78, 'tc_empns_d1': 79, 'tc_emps_d7': 80, 'tc_ls_d1': 81, 'td_p3a_d5': 82, 'td_p3g_d1': 83, 'td_p3g_d5': 84, 'td_p3m_d1': 85, 'td_p3m_d5': 86, 'td_p51g_d1': 87, 'td_p51g_d5': 88, 'td_p51m_d1': 89, 'td_p51m_d5': 90, 'td_p51t_d1': 91, 'td_p51t_d5': 92, 'td_p523_d1': 93, 'td_p523_d3': 94, 'td_p6_d1': 95, 'td_p6_d5': 96, 'td_p7_d1': 97, 'td_p7_d5': 98, 'td_pint_d5': 99, 'time': 100, 'trim1': 101, 'trim2': 102, 'trim3': 103, 'trim4': 104, 'tuc': 105} 

# Liste des noms de coefficients
coeffs = ['ac1d4zs143', 'ar1d11d5', 'ar1d4zs143', 'ar1empsd7', 'ar1p3ad5', 'ar1p3gd5', 'ar1p3md5', 'ar1p51gd5', 'ar1p51md1', 'ar1p51td5', 'ar1p523d1', 'ar1p7d5', 'ar2p3ad5', 'ar2p3gd5', 'ar2p3md5', 'ar2p51td1', 'ar2p6d5', 'ard41s14s3', 'c0d11d5', 'c0d14s14s3', 'c0empsd7', 'c0p3ad5', 'c0p3gd5', 'c0p3md1', 'c0p3md5', 'c0p51gd5', 'c0p51md1', 'c0p51md5', 'c0p51td1', 'c0p51td5', 'c0p523d1', 'c0p6d5', 'c0p7d5', 'c1empsd7', 'c1p3md1', 'c1p51md1', 'c1p523d1', 'c1p6d1', 'c1p7d1', 'c2p3md1', 'c2p523d1', 'c3d11dim5', 'c3p3md1', 'c3p523d1', 'c3p6d1', 'c4p3md1', 'c5p3md1', 'c6p3md1', 'clt0p6d1', 'clt0p7d1', 'clt1p6d5', 'clt1p7d5', 'clt2p6d1', 'clt2p7d1', 'cltp3ad5', 'cltp3gd5', 'cltp3md5', 'cltp51gd5', 'cltp51md5', 'cltp51td5', 'ctlp51md1', 'dum1d11d5', 'dum1p3dmd5', 'dum1p3gd5', 'dum1p51gd5', 'dum1p51md5', 'dum1p6d5gd5', 'mu0p51td1', 'mu1p51td1', 'mup3md1', 'mup51md1', 'mup6d1', 'mup7d1', 'p1d5s14', 'p70p3ad5', 'p70p3md5', 'p70p51gd5', 'p70p51td5', 'p71p3ad5', 'p7d50p7d1', 'pc0d11d5', 'petfm0p7d5', 'petfx0p6d5', 'petfx1p6d5', 'pib0p51td1', 'r3md41s14s3', 'rl0d41s14s3', 'ulc0p3g5', 'ulc0p3m5', 'ulc0p51gg5', 'ulc0p51m5', 'ulc0p51td5', 'ulc0p6d5', 'ulc0p7d1', 'ulc1p3a5', 'ulc1p3g5', 'ulc1p3m5', 'ulc1p51m5', 'ulc1p51td5', 'ulc1p7d1'] 

def colibri_inv_varendo(num_block): 
	"""
 	Fonction produite automatiquement pour la résolution du modèle 

	Détermine les endogènes associées à chaque bloc 
	
	Arguments : 
		num_block : numéro du bloc (décomposition de Dulmage-Mendelsohn) 
	
	""" 
	list_block_varendo = [['td_p51_d3', 'tcho', 'tc_ulc_d5', 'tc_d61s_s14e3', 'td_p3a_d1', 'td_p3m_d3', 'td_p3g_d3', 'tc_d11_d3', 'tc_d1_d3', 'td_pib3', 'td_p3a_d3', 'td_b6_s143', 'td_ratio_p7', 'td_p6_d3', 'tc_uc_d5', 'td_p51t_d3', 'td_p7_d3', 'td_p51_d1', 'td_b6taxable_s14r3', 'td_b2_s143', 'td_p51g_d3', 'tc_d7_s14s3', 'td_p51m_d3', 'tc_d11_s14r3', 'td_pib1', 'tc_emp_d1', 'tc_d62_s14r3'] , \
		['p3m_d1_cale'] , \
		['p3m_d5_cale'] , \
		['p3g_d5_cale'] , \
		['p3a_d5_cale'] , \
		['p51m_d1_cale'] , \
		['p51m_d5_cale'] , \
		['td_pib5'] , \
		['p51t_d1_cale'] , \
		['p51t_d5_cale'] , \
		['p51g_d5_cale'] , \
		['td_p51_d5'] , \
		['p6_d1_cale'] , \
		['p6_d5_cale'] , \
		['compet', 'td_dint_dhs1'] , \
		['p523_d1_cale'] , \
		['p523_d3_cale'] , \
		['pint_d5_cale'] , \
		['td_dint_d1'] , \
		['p7_d1_cale'] , \
		['p7_d5_cale'] , \
		['emps_d7_cale'] , \
		['d11_d5_cale'] , \
		['d41_s14s3_cale'] , \
		['d4z_s14s3_cale'] , \
		['td_b6_s143a'] , \
		['d5_s143_cale'] , \
		] 
	return list_block_varendo[num_block] 

def colibri_inv_dicoendo(num_block): 
	"""
 	Fonction produite automatiquement pour la résolution du modèle 

	Détermine les correspondances des endogènes associées à chaque bloc 
	
	Arguments : 
		num_block : numéro du bloc (décomposition de Dulmage-Mendelsohn) 
	
	""" 
	list_block_dicoendo = [{'td_p51_d3': 43, 'tcho': 31, 'tc_ulc_d5': 30, 'tc_d61s_s14e3': 25, 'td_p3a_d1': 38, 'td_p3m_d3': 41, 'td_p3g_d3': 40, 'tc_d11_d3': 22, 'tc_d1_d3': 24, 'td_pib3': 51, 'td_p3a_d3': 39, 'td_b6_s143': 33, 'td_ratio_p7': 53, 'td_p6_d3': 48, 'tc_uc_d5': 29, 'td_p51t_d3': 47, 'td_p7_d3': 49, 'td_p51_d1': 42, 'td_b6taxable_s14r3': 35, 'td_b2_s143': 32, 'td_p51g_d3': 45, 'tc_d7_s14s3': 27, 'td_p51m_d3': 46, 'tc_d11_s14r3': 23, 'td_pib1': 50, 'tc_emp_d1': 28, 'tc_d62_s14r3': 26} , \
		{'p3m_d1_cale': 8} , \
		{'p3m_d5_cale': 9} , \
		{'p3g_d5_cale': 7} , \
		{'p3a_d5_cale': 6} , \
		{'p51m_d1_cale': 11} , \
		{'p51m_d5_cale': 12} , \
		{'td_pib5': 52} , \
		{'p51t_d1_cale': 13} , \
		{'p51t_d5_cale': 14} , \
		{'p51g_d5_cale': 10} , \
		{'td_p51_d5': 44} , \
		{'p6_d1_cale': 17} , \
		{'p6_d5_cale': 18} , \
		{'compet': 0, 'td_dint_dhs1': 37} , \
		{'p523_d1_cale': 15} , \
		{'p523_d3_cale': 16} , \
		{'pint_d5_cale': 21} , \
		{'td_dint_d1': 36} , \
		{'p7_d1_cale': 19} , \
		{'p7_d5_cale': 20} , \
		{'emps_d7_cale': 5} , \
		{'d11_d5_cale': 1} , \
		{'d41_s14s3_cale': 2} , \
		{'d4z_s14s3_cale': 3} , \
		{'td_b6_s143a': 34} , \
		{'d5_s143_cale': 4} , \
		] 
	return list_block_dicoendo[num_block] 

def colibri_inv_0(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(27,dtype=np.float64)
	f[0] = (x[7])-((data[t-0,74])*(data[t-0,80]))
	f[1] = (x[8])-((x[7])*(((1)+(data[t-0,73]))))
	f[2] = (x[23])-((x[7])*(data[t-0,70]))
	f[3] = (x[3])-((data[t-0,55])*(x[23]))
	f[4] = (x[26])-(((0.25)*(((((data[t-1,86])+(data[t-2,86]))+(data[t-3,86]))+(data[t-4,86]))))*(data[t-0,78]))
	f[5] = (x[6])-((data[t-0,83])*(data[t-0,84]))
	f[6] = (x[5])-((data[t-0,85])*(data[t-0,86]))
	f[7] = (x[20])-((data[t-0,87])*(data[t-0,88]))
	f[8] = (x[22])-((data[t-0,89])*(data[t-0,90]))
	f[9] = (x[15])-((data[t-0,91])*(data[t-0,92]))
	f[10] = (x[0])-(((x[22])+(x[15]))+(x[20]))
	f[11] = (x[13])-((data[t-0,95])*(data[t-0,96]))
	f[12] = (x[16])-((data[t-0,97])*(data[t-0,98]))
	f[13] = (x[9])-(((((((x[5])+(x[0]))+(x[6]))+(x[10]))+(x[13]))+(data[t-0,94]))-(x[16]))
	f[14] = (x[21])-((data[t-0,65])*(x[9]))
	f[15] = (x[19])-((data[t-0,54])*(x[9]))
	f[16] = (x[18])-(((((((x[19])+(x[23]))+(data[t-0,75]))+(data[t-0,76]))-(x[3]))+(x[26]))+(x[21]))
	f[17] = (x[11])-((x[18])-(data[t-0,77]))
	f[18] = (x[10])-((data[t-0,56])*(x[11]))
	f[19] = (x[4])-((x[10])/(data[t-0,82]))
	f[20] = (x[17])-(((data[t-0,89])+(data[t-0,91]))+(data[t-0,87]))
	f[21] = (x[24])-(((((((data[t-0,85])+(x[17]))+(data[t-0,83]))+(x[4]))+(data[t-0,95]))+(data[t-0,93]))-(data[t-0,97]))
	f[22] = (x[2])-(((x[8])*(((1)-(data[t-0,71]))))/(x[24]))
	f[23] = (x[12])-((x[16])/(((((x[16])+(x[9]))-(x[6]))-(x[22]))))
	f[24] = (x[14])-(((x[12])*(data[t-0,98]))+(((((1)-(x[12])))*(x[2]))/(0.47)))
	f[25] = (x[25])-(((data[t-0,80])/(((1)-(data[t-0,72]))))+(data[t-0,79]))
	f[26] = (x[1])-(((((data[t-0,81])-(x[25])))/(data[t-0,81]))*(100))
	return f

def colibri_inv_0_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((27,27),dtype=np.float64)
	df[0][7] = (1)
	df[1][7] = -(((1)+(data[t-0,73])))
	df[1][8] = (1)
	df[2][7] = -(data[t-0,70])
	df[2][23] = (1)
	df[3][3] = (1)
	df[3][23] = -(data[t-0,55])
	df[4][26] = (1)
	df[5][6] = (1)
	df[6][5] = (1)
	df[7][20] = (1)
	df[8][22] = (1)
	df[9][15] = (1)
	df[10][0] = (1)
	df[10][15] = -(1)
	df[10][20] = -(1)
	df[10][22] = -(1)
	df[11][13] = (1)
	df[12][16] = (1)
	df[13][0] = -((1))
	df[13][5] = -((1))
	df[13][6] = -((1))
	df[13][9] = (1)
	df[13][10] = -((1))
	df[13][13] = -((1))
	df[13][16] = -(-(1))
	df[14][9] = -(data[t-0,65])
	df[14][21] = (1)
	df[15][9] = -(data[t-0,54])
	df[15][19] = (1)
	df[16][3] = -(-(1))
	df[16][18] = (1)
	df[16][19] = -((1))
	df[16][21] = -(1)
	df[16][23] = -((1))
	df[16][26] = -(1)
	df[17][11] = (1)
	df[17][18] = -(1)
	df[18][10] = (1)
	df[18][11] = -(data[t-0,56])
	df[19][4] = (1)
	df[19][10] = -(1/(data[t-0,82]))
	df[20][17] = (1)
	df[21][4] = -(1)
	df[21][17] = -(1)
	df[21][24] = (1)
	df[22][2] = (1)
	df[22][8] = -(((((1)-(data[t-0,71])))/(x[24])))
	df[22][24] = -(-((((x[8])*(((1)-(data[t-0,71]))))/(x[24]))*(1/(x[24]))))
	df[23][6] = -(-(((x[16])/(((((x[16])+(x[9]))-(x[6]))-(x[22]))))*((((-(1))))/(((((x[16])+(x[9]))-(x[6]))-(x[22]))))))
	df[23][9] = -(-(((x[16])/(((((x[16])+(x[9]))-(x[6]))-(x[22]))))*(((((1))))/(((((x[16])+(x[9]))-(x[6]))-(x[22]))))))
	df[23][12] = (1)
	df[23][16] = -((1/(((((x[16])+(x[9]))-(x[6]))-(x[22]))))-(((x[16])/(((((x[16])+(x[9]))-(x[6]))-(x[22]))))*(((((1))))/(((((x[16])+(x[9]))-(x[6]))-(x[22]))))))
	df[23][22] = -(-(((x[16])/(((((x[16])+(x[9]))-(x[6]))-(x[22]))))*(((-(1)))/(((((x[16])+(x[9]))-(x[6]))-(x[22]))))))
	df[24][2] = -((((1)-(x[12])))/(0.47))
	df[24][12] = -((data[t-0,98])+((((-(1)))*(x[2]))/(0.47)))
	df[24][14] = (1)
	df[25][25] = (1)
	df[26][1] = (1)
	df[26][25] = -((((-1))/(data[t-0,81]))*(100))
	return df

def colibri_inv_1(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,85])- (log(data[t-1,85]))))-((((((((((coeff['c1p3md1'])*((log((data[t-0,33])/(data[t-0,86]))- (log((data[t-1,33])/(data[t-1,86]))))))+((coeff['c2p3md1'])*((log((data[t-1,33])/(data[t-1,86]))- (log((data[t-2,33])/(data[t-2,86])))))))+((coeff['c3p3md1'])*((log((data[t-2,33])/(data[t-2,86]))- (log((data[t-3,33])/(data[t-3,86])))))))+((coeff['c4p3md1'])*((log((data[t-3,33])/(data[t-3,86]))- (log((data[t-4,33])/(data[t-4,86])))))))+((coeff['c5p3md1'])*(((data[t-2,69])-(((((data[t-2,86])/(data[t-6,86]))-(1)))*(100))- ((data[t-3,69])-(((((data[t-3,86])/(data[t-7,86]))-(1)))*(100)))))))+((coeff['c6p3md1'])*((data[t-0,31]- (data[t-1,31])))))+((coeff['mup3md1'])*(log(((data[t-1,85])/(data[t-0,33]))*(data[t-1,86])))))+(coeff['c0p3md1']))+(x[0]))
	return f

def colibri_inv_1_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_2(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,86])- (log(data[t-1,86]))))-((((((((((coeff['ar1p3md5'])*((log(data[t-1,86])- (log(data[t-2,86])))))+((coeff['ar2p3md5'])*((log(data[t-2,86])- (log(data[t-3,86]))))))+((coeff['p70p3md5'])*((log(data[t-0,98])- (log(data[t-1,98]))))))+((coeff['ulc0p3m5'])*((log(data[t-0,30])- (log(data[t-1,30]))))))+((coeff['ulc1p3m5'])*((log(data[t-1,30])- (log(data[t-2,30]))))))+((coeff['cltp3md5'])*(log((data[t-2,86])/(data[t-2,29])))))+(coeff['c0p3md5']))+((coeff['dum1p3dmd5'])*(data[t-0,59])))+(x[0]))
	return f

def colibri_inv_2_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_3(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,84])- (log(data[t-1,84]))))-(((((((((coeff['ar1p3gd5'])*((log(data[t-1,84])- (log(data[t-2,84])))))+((coeff['ar2p3gd5'])*((log(data[t-2,84])- (log(data[t-3,84]))))))+((coeff['ulc0p3g5'])*((log(data[t-0,30])- (log(data[t-1,30]))))))+((coeff['ulc1p3g5'])*((log(data[t-1,30])- (log(data[t-2,30]))))))+((coeff['cltp3gd5'])*(log((data[t-2,84])/(data[t-2,30])))))+(coeff['c0p3gd5']))+((coeff['dum1p3gd5'])*(data[t-0,62])))+(x[0]))
	return f

def colibri_inv_3_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_4(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,82])- (log(data[t-1,82]))))-(((((((((coeff['ar1p3ad5'])*((log(data[t-1,82])- (log(data[t-2,82])))))+((coeff['ar2p3ad5'])*((log(data[t-2,82])- (log(data[t-3,82]))))))+((coeff['p70p3ad5'])*((log(data[t-0,98])- (log(data[t-1,98]))))))+((coeff['p71p3ad5'])*((log(data[t-1,98])- (log(data[t-2,98]))))))+((coeff['ulc1p3a5'])*((log(data[t-1,30])- (log(data[t-2,30]))))))+((coeff['cltp3ad5'])*(log((data[t-2,82])/(data[t-2,29])))))+(coeff['c0p3ad5']))+(x[0]))
	return f

def colibri_inv_4_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_5(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,89])- (log(data[t-1,89]))))-((((((coeff['c0p51md1'])+((coeff['ar1p51md1'])*((log(data[t-1,89])- (log(data[t-2,89]))))))+((coeff['c1p51md1'])*((log(data[t-1,90])- (log(data[t-2,90]))))))+((coeff['mup51md1'])*(((log(data[t-1,89]))-(log(((data[t-1,33])/(data[t-1,90]))*(100)))))))+((coeff['ctlp51md1'])*(((data[t-1,68])-(((((data[t-1,90])/(data[t-5,90]))-(1)))*(100))))))+(x[0]))
	return f

def colibri_inv_5_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_6(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,90])- (log(data[t-1,90]))))-(((((((coeff['ulc0p51m5'])*((log(data[t-0,30])- (log(data[t-1,30])))))+((coeff['ulc1p51m5'])*((log(data[t-1,30])- (log(data[t-2,30]))))))+((coeff['cltp51md5'])*(log((data[t-1,90])/(data[t-1,30])))))+(coeff['c0p51md5']))+((coeff['dum1p51md5'])*(data[t-0,63])))+(x[0]))
	return f

def colibri_inv_6_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_7(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = (x[0])-((data[t-0,51])/(data[t-0,50]))
	return f

def colibri_inv_7_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = (1)
	return df

def colibri_inv_8(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,91])- (log(data[t-1,91]))))-((((((coeff['c0p51td1'])+((coeff['ar2p51td1'])*((log(data[t-2,91])- (log(data[t-3,91]))))))+((coeff['pib0p51td1'])*((log(data[t-0,50])- (log(data[t-1,50]))))))+((coeff['mu0p51td1'])*(log(((data[t-1,91])/(data[t-1,50]))))))+((coeff['mu1p51td1'])*(((log(((data[t-1,92])/(data[t-1,52]))))+(log((((data[t-0,68])/(100))+(0.08))-(log((data[t-1,92])/(data[t-4,92])))))))))+(x[0]))
	return f

def colibri_inv_8_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_9(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,92])- (log(data[t-1,92]))))-((((((((coeff['ar1p51td5'])*((log(data[t-1,92])- (log(data[t-2,92])))))+((coeff['p70p51td5'])*((log(data[t-0,98])- (log(data[t-1,98]))))))+((coeff['ulc0p51td5'])*((log(data[t-0,30])- (log(data[t-1,30]))))))+((coeff['ulc1p51td5'])*((log(data[t-1,30])- (log(data[t-2,30]))))))+((coeff['cltp51td5'])*(log(((data[t-1,90])/(data[t-1,29]))))))+(coeff['c0p51td5']))+(x[0]))
	return f

def colibri_inv_9_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_10(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,88])- (log(data[t-1,88]))))-((((((((coeff['ar1p51gd5'])*((log(data[t-1,88])- (log(data[t-2,88])))))+((coeff['p70p51gd5'])*((log(data[t-0,98])- (log(data[t-1,98]))))))+((coeff['ulc0p51gg5'])*((log(data[t-0,30])- (log(data[t-1,30]))))))+((coeff['cltp51gd5'])*(log((data[t-1,88])/(data[t-1,29])))))+(coeff['c0p51gd5']))+((coeff['dum1p51gd5'])*(data[t-0,58])))+(x[0]))
	return f

def colibri_inv_10_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_11(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = (x[0])-((data[t-0,43])/(data[t-0,42]))
	return f

def colibri_inv_11_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = (1)
	return df

def colibri_inv_12(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,95])- (log(data[t-1,95]))))-(((((((((coeff['c1p6d1'])*((log(data[t-0,57])- (log(data[t-1,57])))))+((((1)-(coeff['c1p6d1'])))*((log(data[t-1,57])- (log(data[t-2,57]))))))+((coeff['c3p6d1'])*((((log((data[t-0,96])/(data[t-0,67]))- (log((data[t-1,96])/(data[t-1,67])))))+((log((data[t-1,96])/(data[t-1,67]))- (log((data[t-2,96])/(data[t-2,67])))))))))+((coeff['mup6d1'])*(log((data[t-1,95])/(data[t-1,57])))))-((((2)*(coeff['mup6d1']))*(coeff['c3p6d1']))*(log((data[t-1,96])/(data[t-1,67])))))+((coeff['clt2p6d1'])*(data[t-0,64])))+(coeff['clt0p6d1']))+(x[0]))
	return f

def colibri_inv_12_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_13(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,96])- (log(data[t-1,96]))))-(((((((((coeff['ar2p6d5'])*((log(data[t-2,96])- (log(data[t-3,96])))))+((coeff['petfx0p6d5'])*((log(data[t-0,67])- (log(data[t-1,67]))))))+((coeff['petfx1p6d5'])*((log(data[t-1,67])- (log(data[t-2,67]))))))+((coeff['ulc0p6d5'])*((log(data[t-0,30])- (log(data[t-1,30]))))))+((coeff['clt1p6d5'])*(((log((data[t-2,96])/(data[t-2,67])))-((0.3)*(log((data[t-2,30])/(data[t-2,67]))))))))+(coeff['c0p6d5']))+((coeff['dum1p6d5gd5'])*(data[t-0,61])))+(x[0]))
	return f

def colibri_inv_13_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_14(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(2,dtype=np.float64)
	f[0] = (x[0])-((data[t-0,67])/(data[t-0,96]))
	f[1] = (x[1])-(((((data[t-0,85])+(data[t-0,42]))+(data[t-0,83]))+(data[t-0,38]))+(data[t-0,95]))
	return f

def colibri_inv_14_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((2,2),dtype=np.float64)
	df[0][0] = (1)
	df[1][1] = (1)
	return df

def colibri_inv_15(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = (data[t-0,93])-((((((coeff['c0p523d1'])+((coeff['ar1p523d1'])*(data[t-1,93])))+((coeff['c1p523d1'])*((data[t-0,37]- (data[t-1,37])))))+((coeff['c2p523d1'])*((data[t-1,37]- (data[t-2,37])))))+(((coeff['c3p523d1'])*(data[t-1,37]))*(((data[t-1,69])-((100)*((((data[t-1,52])/(data[t-5,52]))-(1))))- ((data[t-2,69])-((100)*((((data[t-2,52])/(data[t-6,52]))-(1)))))))))+(x[0]))
	return f

def colibri_inv_15_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_16(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = (data[t-0,94])-((((((((((data[t-1,41])+(data[t-1,43]))+(data[t-1,40]))+(data[t-1,39]))+(data[t-1,48])))/((((((data[t-1,85])+(data[t-1,42]))+(data[t-1,83]))+(data[t-1,38]))+(data[t-1,95])))))*(data[t-0,93]))+(x[0]))
	return f

def colibri_inv_16_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_17(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,99])- (log(data[t-1,99]))))-(x[0])
	return f

def colibri_inv_17_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_18(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = (x[0])-((data[t-0,37])+(data[t-0,93]))
	return f

def colibri_inv_18_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = (1)
	return df

def colibri_inv_19(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,97])- (log(data[t-1,97]))))-(((((((((coeff['c1p7d1'])*((log((data[t-0,36])+(data[t-0,95]))- (log((data[t-1,36])+(data[t-1,95]))))))+((coeff['ulc0p7d1'])*((log(data[t-0,30])- (log(data[t-1,30]))))))+((coeff['ulc1p7d1'])*((log(data[t-1,30])- (log(data[t-2,30]))))))+((coeff['p7d50p7d1'])*((log(data[t-0,98])- (log(data[t-1,98]))))))+((coeff['mup7d1'])*(((log(((data[t-1,97])/(((data[t-1,36])+(data[t-1,95]))))))+((((coeff['ulc0p7d1'])+(coeff['ulc1p7d1'])))*(log(((data[t-2,98])/(data[t-2,30])))))))))+((coeff['clt2p7d1'])*(data[t-1,64])))+(coeff['clt0p7d1']))+(x[0]))
	return f

def colibri_inv_19_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_20(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,98])- (log(data[t-1,98]))))-(((((((coeff['ar1p7d5'])*((log(data[t-1,98])- (log(data[t-2,98])))))+((coeff['petfm0p7d5'])*((log(data[t-0,66])- (log(data[t-1,66]))))))+(((((1)-(coeff['ar1p7d5']))-(coeff['petfm0p7d5'])))*((log(data[t-1,66])- (log(data[t-2,66]))))))+((coeff['clt1p7d5'])*(log((data[t-2,98])/(data[t-2,66])))))+(coeff['c0p7d5']))+(x[0]))
	return f

def colibri_inv_20_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_21(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,80])- (log(data[t-1,80]))))-(((((coeff['c0empsd7'])+((coeff['ar1empsd7'])*((log(data[t-1,80])- (log(data[t-2,80]))))))+((((1)-(coeff['ar1empsd7'])))*((log(data[t-0,50])- (log(data[t-1,50]))))))+((coeff['c1empsd7'])*((((log(((data[t-0,74])/(data[t-0,52]))*(100))- (log(((data[t-1,74])/(data[t-1,52]))*(100)))))+((log(((data[t-1,74])/(data[t-1,52]))*(100))- (log(((data[t-2,74])/(data[t-2,52]))*(100)))))))))+(x[0]))
	return f

def colibri_inv_21_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_22(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,74])- (log(data[t-1,74]))))-((((((coeff['c0d11d5'])+((coeff['ar1d11d5'])*((log(data[t-1,74])- (log(data[t-2,74]))))))+((coeff['pc0d11d5'])*((log(data[t-0,86])- (log(data[t-1,86]))))))+((coeff['dum1d11d5'])*(((data[t-0,59])-(data[t-0,60])))))+((coeff['c3d11dim5'])*(log(data[t-0,31]))))+(x[0]))
	return f

def colibri_inv_22_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_23(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((data[t-0,75])/(data[t-1,33]))-(((((coeff['c0d14s14s3'])+(((coeff['ard41s14s3'])*(data[t-1,75]))/(data[t-2,33])))+((coeff['rl0d41s14s3'])*(data[t-0,68])))+((coeff['r3md41s14s3'])*(((data[t-0,69])-((coeff['ard41s14s3'])*(data[t-1,69]))))))+(x[0]))
	return f

def colibri_inv_23_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_24(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((data[t-0,76]- (data[t-1,76])))-((((coeff['ar1d4zs143'])*((data[t-1,76]- (data[t-2,76]))))+((coeff['ac1d4zs143'])*((data[t-1,51]- (data[t-2,51])))))+(x[0]))
	return f

def colibri_inv_24_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

def colibri_inv_25(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = (x[0])-(((((data[t-0,101])*(((((data[t-1,33])+(data[t-2,33]))+(data[t-3,33]))+(data[t-4,33]))))+((data[t-0,102])*(((((data[t-2,33])+(data[t-3,33]))+(data[t-4,33]))+(data[t-4,33])))))+((data[t-0,103])*(((((data[t-3,33])+(data[t-4,33]))+(data[t-4,33]))+(data[t-5,33])))))+((data[t-0,104])*(((((data[t-4,33])+(data[t-4,33]))+(data[t-5,33]))+(data[t-6,33])))))
	return f

def colibri_inv_25_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = (1)
	return df

def colibri_inv_26(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(1,dtype=np.float64)
	f[0] = ((log(data[t-0,77])- (log(data[t-1,77]))))-(((((coeff['p1d5s14'])*(1.9))*((log(data[t-0,34])- (log(data[t-1,34])))))+((((1)-(coeff['p1d5s14'])))*((log(data[t-0,35])- (log(data[t-1,35]))))))+(x[0]))
	return f

def colibri_inv_26_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((1,1),dtype=np.float64)
	df[0][0] = 0
	return df

