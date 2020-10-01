import numpy as np
from math import log, exp

import numpy as np

# Nombre de blocs du modèle
n_blocks = 1 

# Liste des noms de variables
coln = ['compet', 'tc_d11_d3', 'tc_d11_d5', 'tc_d11_s14r3', 'tc_d1_d3', 'tc_d41_s14s3', 'tc_d4z_s14s3', 'tc_d5_s14e3', 'tc_d61s_s14e3', 'tc_d62_s14r3', 'tc_d7_s14s3', 'tc_emp_d1', 'tc_emps_d7', 'tc_uc_d5', 'tc_ulc_d5', 'tcho', 'td_b2_s143', 'td_b6_s143', 'td_b6_s143a', 'td_b6taxable_s14r3', 'td_dint_d1', 'td_dint_dhs1', 'td_p3a_d1', 'td_p3a_d3', 'td_p3a_d5', 'td_p3g_d3', 'td_p3g_d5', 'td_p3m_d1', 'td_p3m_d3', 'td_p3m_d5', 'td_p51_d1', 'td_p51_d3', 'td_p51_d5', 'td_p51g_d3', 'td_p51g_d5', 'td_p51m_d1', 'td_p51m_d3', 'td_p51m_d5', 'td_p51t_d1', 'td_p51t_d3', 'td_p51t_d5', 'td_p523_d1', 'td_p523_d3', 'td_p6_d1', 'td_p6_d3', 'td_p6_d5', 'td_p7_d1', 'td_p7_d3', 'td_p7_d5', 'td_pib1', 'td_pib3', 'td_pib5', 'td_pint_d5', 'td_ratio_p7', 'b2_part', 'ct_d61ss14', 'ct_tdp3ad3', 'demmon', 'dum_1982q1', 'dum_1982q3', 'dum_1983q1', 'dum_1984q1', 'dum_1990q1', 'dum_1999q4', 'inter', 'pd7s14', 'petfm', 'petfx', 'r10a', 'r3m', 'ratio_d11', 'ratio_d29_39', 'ratio_part', 'ratio_soc', 'tc_d62_s14r1', 'tc_empns_d1', 'tc_ls_d1', 'td_p3g_d1', 'td_p51g_d1', 'time', 'trim1', 'trim2', 'trim3', 'trim4', 'tuc', 'd11_d5_cale', 'd41_s14s3_cale', 'd4z_s14s3_cale', 'd5_s143_cale', 'emps_d7_cale', 'p3a_d5_cale', 'p3g_d5_cale', 'p3m_d1_cale', 'p3m_d5_cale', 'p51g_d5_cale', 'p51m_d1_cale', 'p51m_d5_cale', 'p51t_d1_cale', 'p51t_d5_cale', 'p523_d1_cale', 'p523_d3_cale', 'p6_d1_cale', 'p6_d5_cale', 'p7_d1_cale', 'p7_d5_cale', 'pint_d5_cale'] 

# Dictionnaire de correspondance des noms de variables
dicovar = {'compet': 0, 'tc_d11_d3': 1, 'tc_d11_d5': 2, 'tc_d11_s14r3': 3, 'tc_d1_d3': 4, 'tc_d41_s14s3': 5, 'tc_d4z_s14s3': 6, 'tc_d5_s14e3': 7, 'tc_d61s_s14e3': 8, 'tc_d62_s14r3': 9, 'tc_d7_s14s3': 10, 'tc_emp_d1': 11, 'tc_emps_d7': 12, 'tc_uc_d5': 13, 'tc_ulc_d5': 14, 'tcho': 15, 'td_b2_s143': 16, 'td_b6_s143': 17, 'td_b6_s143a': 18, 'td_b6taxable_s14r3': 19, 'td_dint_d1': 20, 'td_dint_dhs1': 21, 'td_p3a_d1': 22, 'td_p3a_d3': 23, 'td_p3a_d5': 24, 'td_p3g_d3': 25, 'td_p3g_d5': 26, 'td_p3m_d1': 27, 'td_p3m_d3': 28, 'td_p3m_d5': 29, 'td_p51_d1': 30, 'td_p51_d3': 31, 'td_p51_d5': 32, 'td_p51g_d3': 33, 'td_p51g_d5': 34, 'td_p51m_d1': 35, 'td_p51m_d3': 36, 'td_p51m_d5': 37, 'td_p51t_d1': 38, 'td_p51t_d3': 39, 'td_p51t_d5': 40, 'td_p523_d1': 41, 'td_p523_d3': 42, 'td_p6_d1': 43, 'td_p6_d3': 44, 'td_p6_d5': 45, 'td_p7_d1': 46, 'td_p7_d3': 47, 'td_p7_d5': 48, 'td_pib1': 49, 'td_pib3': 50, 'td_pib5': 51, 'td_pint_d5': 52, 'td_ratio_p7': 53, 'b2_part': 54, 'ct_d61ss14': 55, 'ct_tdp3ad3': 56, 'demmon': 57, 'dum_1982q1': 58, 'dum_1982q3': 59, 'dum_1983q1': 60, 'dum_1984q1': 61, 'dum_1990q1': 62, 'dum_1999q4': 63, 'inter': 64, 'pd7s14': 65, 'petfm': 66, 'petfx': 67, 'r10a': 68, 'r3m': 69, 'ratio_d11': 70, 'ratio_d29_39': 71, 'ratio_part': 72, 'ratio_soc': 73, 'tc_d62_s14r1': 74, 'tc_empns_d1': 75, 'tc_ls_d1': 76, 'td_p3g_d1': 77, 'td_p51g_d1': 78, 'time': 79, 'trim1': 80, 'trim2': 81, 'trim3': 82, 'trim4': 83, 'tuc': 84, 'd11_d5_cale': 85, 'd41_s14s3_cale': 86, 'd4z_s14s3_cale': 87, 'd5_s143_cale': 88, 'emps_d7_cale': 89, 'p3a_d5_cale': 90, 'p3g_d5_cale': 91, 'p3m_d1_cale': 92, 'p3m_d5_cale': 93, 'p51g_d5_cale': 94, 'p51m_d1_cale': 95, 'p51m_d5_cale': 96, 'p51t_d1_cale': 97, 'p51t_d5_cale': 98, 'p523_d1_cale': 99, 'p523_d3_cale': 100, 'p6_d1_cale': 101, 'p6_d5_cale': 102, 'p7_d1_cale': 103, 'p7_d5_cale': 104, 'pint_d5_cale': 105} 

# Liste des noms de coefficients
coeffs = ['ac1d4zs143', 'ar1d11d5', 'ar1d4zs143', 'ar1empsd7', 'ar1p3ad5', 'ar1p3gd5', 'ar1p3md5', 'ar1p51gd5', 'ar1p51md1', 'ar1p51td5', 'ar1p523d1', 'ar1p7d5', 'ar2p3ad5', 'ar2p3gd5', 'ar2p3md5', 'ar2p51td1', 'ar2p6d5', 'ard41s14s3', 'c0d11d5', 'c0d14s14s3', 'c0empsd7', 'c0p3ad5', 'c0p3gd5', 'c0p3md1', 'c0p3md5', 'c0p51gd5', 'c0p51md1', 'c0p51md5', 'c0p51td1', 'c0p51td5', 'c0p523d1', 'c0p6d5', 'c0p7d5', 'c1empsd7', 'c1p3md1', 'c1p51md1', 'c1p523d1', 'c1p6d1', 'c1p7d1', 'c2p3md1', 'c2p523d1', 'c3d11dim5', 'c3p3md1', 'c3p523d1', 'c3p6d1', 'c4p3md1', 'c5p3md1', 'c6p3md1', 'clt0p6d1', 'clt0p7d1', 'clt1p6d5', 'clt1p7d5', 'clt2p6d1', 'clt2p7d1', 'cltp3ad5', 'cltp3gd5', 'cltp3md5', 'cltp51gd5', 'cltp51md5', 'cltp51td5', 'ctlp51md1', 'dum1d11d5', 'dum1p3dmd5', 'dum1p3gd5', 'dum1p51gd5', 'dum1p51md5', 'dum1p6d5gd5', 'mu0p51td1', 'mu1p51td1', 'mup3md1', 'mup51md1', 'mup6d1', 'mup7d1', 'p1d5s14', 'p70p3ad5', 'p70p3md5', 'p70p51gd5', 'p70p51td5', 'p71p3ad5', 'p7d50p7d1', 'pc0d11d5', 'petfm0p7d5', 'petfx0p6d5', 'petfx1p6d5', 'pib0p51td1', 'r3md41s14s3', 'rl0d41s14s3', 'ulc0p3g5', 'ulc0p3m5', 'ulc0p51gg5', 'ulc0p51m5', 'ulc0p51td5', 'ulc0p6d5', 'ulc0p7d1', 'ulc1p3a5', 'ulc1p3g5', 'ulc1p3m5', 'ulc1p51m5', 'ulc1p51td5', 'ulc1p7d1'] 

def colibri_varendo(num_block): 
	"""
 	Fonction produite automatiquement pour la résolution du modèle 

	Détermine les endogènes associées à chaque bloc 
	
	Arguments : 
		num_block : numéro du bloc (décomposition de Dulmage-Mendelsohn) 
	
	""" 
	list_block_varendo = [['td_p51m_d5', 'td_b6_s143a', 'td_p51_d3', 'tcho', 'td_p3a_d5', 'td_p523_d3', 'tc_ulc_d5', 'tc_d61s_s14e3', 'td_p3a_d1', 'td_p3m_d3', 'td_p3m_d5', 'tc_d11_d5', 'td_p3m_d1', 'td_pint_d5', 'td_p3g_d3', 'td_p523_d1', 'td_p6_d5', 'tc_d11_d3', 'tc_d1_d3', 'td_pib3', 'td_p3a_d3', 'td_dint_d1', 'td_b6_s143', 'td_p51_d5', 'tc_emps_d7', 'td_p6_d3', 'td_ratio_p7', 'td_p7_d1', 'td_p51g_d5', 'td_p51m_d1', 'tc_uc_d5', 'td_p51t_d3', 'tc_d41_s14s3', 'td_p7_d3', 'td_p51t_d1', 'tc_d5_s14e3', 'td_p51_d1', 'td_dint_dhs1', 'td_p51t_d5', 'td_b6taxable_s14r3', 'td_b2_s143', 'td_p51g_d3', 'tc_d7_s14s3', 'compet', 'td_p3g_d5', 'td_p51m_d3', 'tc_d11_s14r3', 'td_pib5', 'td_pib1', 'tc_emp_d1', 'tc_d4z_s14s3', 'tc_d62_s14r3', 'td_p7_d5', 'td_p6_d1'] , \
		] 
	return list_block_varendo[num_block] 

def colibri_dicoendo(num_block): 
	"""
 	Fonction produite automatiquement pour la résolution du modèle 

	Détermine les correspondances des endogènes associées à chaque bloc 
	
	Arguments : 
		num_block : numéro du bloc (décomposition de Dulmage-Mendelsohn) 
	
	""" 
	list_block_dicoendo = [{'td_p51m_d5': 37, 'td_b6_s143a': 18, 'td_p51_d3': 31, 'tcho': 15, 'td_p3a_d5': 24, 'td_p523_d3': 42, 'tc_ulc_d5': 14, 'tc_d61s_s14e3': 8, 'td_p3a_d1': 22, 'td_p3m_d3': 28, 'td_p3m_d5': 29, 'tc_d11_d5': 2, 'td_p3m_d1': 27, 'td_pint_d5': 52, 'td_p3g_d3': 25, 'td_p523_d1': 41, 'td_p6_d5': 45, 'tc_d11_d3': 1, 'tc_d1_d3': 4, 'td_pib3': 50, 'td_p3a_d3': 23, 'td_dint_d1': 20, 'td_b6_s143': 17, 'td_p51_d5': 32, 'tc_emps_d7': 12, 'td_p6_d3': 44, 'td_ratio_p7': 53, 'td_p7_d1': 46, 'td_p51g_d5': 34, 'td_p51m_d1': 35, 'tc_uc_d5': 13, 'td_p51t_d3': 39, 'tc_d41_s14s3': 5, 'td_p7_d3': 47, 'td_p51t_d1': 38, 'tc_d5_s14e3': 7, 'td_p51_d1': 30, 'td_dint_dhs1': 21, 'td_p51t_d5': 40, 'td_b6taxable_s14r3': 19, 'td_b2_s143': 16, 'td_p51g_d3': 33, 'tc_d7_s14s3': 10, 'compet': 0, 'td_p3g_d5': 26, 'td_p51m_d3': 36, 'tc_d11_s14r3': 3, 'td_pib5': 51, 'td_pib1': 49, 'tc_emp_d1': 11, 'tc_d4z_s14s3': 6, 'tc_d62_s14r3': 9, 'td_p7_d5': 48, 'td_p6_d1': 43} , \
		] 
	return list_block_dicoendo[num_block] 

def colibri_0(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Bloc représenté par la fonction F telle que F(x)=0 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	f = np.zeros(54,dtype=np.float64)
	f[0] = ((log(x[52])- (log(data[t-1,48]))))-(((((((coeff['ar1p7d5'])*((log(data[t-1,48])- (log(data[t-2,48])))))+((coeff['petfm0p7d5'])*((log(data[t-0,66])- (log(data[t-1,66]))))))+(((((1)-(coeff['ar1p7d5']))-(coeff['petfm0p7d5'])))*((log(data[t-1,66])- (log(data[t-2,66]))))))+((coeff['clt1p7d5'])*(log((data[t-2,48])/(data[t-2,66])))))+(coeff['c0p7d5']))+(data[t-0,104]))
	f[1] = (x[17])-((x[11])*(x[24]))
	f[2] = (x[46])-((x[17])*(data[t-0,70]))
	f[3] = (x[7])-((data[t-0,55])*(x[46]))
	f[4] = (x[18])-((x[17])*(((1)+(data[t-0,73]))))
	f[5] = (x[6])-(((x[18])*(((1)-(data[t-0,71]))))/(x[48]))
	f[6] = ((log(x[16])- (log(data[t-1,45]))))-(((((((((coeff['ar2p6d5'])*((log(data[t-2,45])- (log(data[t-3,45])))))+((coeff['petfx0p6d5'])*((log(data[t-0,67])- (log(data[t-1,67]))))))+((coeff['petfx1p6d5'])*((log(data[t-1,67])- (log(data[t-2,67]))))))+((coeff['ulc0p6d5'])*((log(x[6])- (log(data[t-1,14]))))))+((coeff['clt1p6d5'])*(((log((data[t-2,45])/(data[t-2,67])))-((0.3)*(log((data[t-2,14])/(data[t-2,67]))))))))+(coeff['c0p6d5']))+((coeff['dum1p6d5gd5'])*(data[t-0,61])))+(data[t-0,102]))
	f[7] = ((log(x[53])- (log(data[t-1,43]))))-(((((((((coeff['c1p6d1'])*((log(data[t-0,57])- (log(data[t-1,57])))))+((((1)-(coeff['c1p6d1'])))*((log(data[t-1,57])- (log(data[t-2,57]))))))+((coeff['c3p6d1'])*((((log((x[16])/(data[t-0,67]))- (log((data[t-1,45])/(data[t-1,67])))))+((log((data[t-1,45])/(data[t-1,67]))- (log((data[t-2,45])/(data[t-2,67])))))))))+((coeff['mup6d1'])*(log((data[t-1,43])/(data[t-1,57])))))-((((2)*(coeff['mup6d1']))*(coeff['c3p6d1']))*(log((data[t-1,45])/(data[t-1,67])))))+((coeff['clt2p6d1'])*(data[t-0,64])))+(coeff['clt0p6d1']))+(data[t-0,101]))
	f[8] = (x[25])-((x[53])*(x[16]))
	f[9] = ((log(x[0])- (log(data[t-1,37]))))-(((((((coeff['ulc0p51m5'])*((log(x[6])- (log(data[t-1,14])))))+((coeff['ulc1p51m5'])*((log(data[t-1,14])- (log(data[t-2,14]))))))+((coeff['cltp51md5'])*(log((data[t-1,37])/(data[t-1,14])))))+(coeff['c0p51md5']))+((coeff['dum1p51md5'])*(data[t-0,63])))+(data[t-0,96]))
	f[10] = ((log(x[44])- (log(data[t-1,26]))))-(((((((((coeff['ar1p3gd5'])*((log(data[t-1,26])- (log(data[t-2,26])))))+((coeff['ar2p3gd5'])*((log(data[t-2,26])- (log(data[t-3,26]))))))+((coeff['ulc0p3g5'])*((log(x[6])- (log(data[t-1,14]))))))+((coeff['ulc1p3g5'])*((log(data[t-1,14])- (log(data[t-2,14]))))))+((coeff['cltp3gd5'])*(log((data[t-2,26])/(data[t-2,14])))))+(coeff['c0p3gd5']))+((coeff['dum1p3gd5'])*(data[t-0,62])))+(data[t-0,91]))
	f[11] = (x[14])-((data[t-0,77])*(x[44]))
	f[12] = (x[30])-(((x[26])*(x[52]))+(((((1)-(x[26])))*(x[6]))/(0.47)))
	f[13] = (x[26])-((x[33])/(((((x[33])+(x[19]))-(x[14]))-(x[45]))))
	f[14] = (x[33])-((x[27])*(x[52]))
	f[15] = ((log(x[27])- (log(data[t-1,46]))))-(((((((((coeff['c1p7d1'])*((log((x[21])+(x[53]))- (log((data[t-1,20])+(data[t-1,43]))))))+((coeff['ulc0p7d1'])*((log(x[6])- (log(data[t-1,14]))))))+((coeff['ulc1p7d1'])*((log(data[t-1,14])- (log(data[t-2,14]))))))+((coeff['p7d50p7d1'])*((log(x[52])- (log(data[t-1,48]))))))+((coeff['mup7d1'])*(((log(((data[t-1,46])/(((data[t-1,20])+(data[t-1,43]))))))+((((coeff['ulc0p7d1'])+(coeff['ulc1p7d1'])))*(log(((data[t-2,48])/(data[t-2,14])))))))))+((coeff['clt2p7d1'])*(data[t-1,64])))+(coeff['clt0p7d1']))+(data[t-0,103]))
	f[16] = (x[21])-((x[37])+(x[15]))
	f[17] = (x[15])-((((((coeff['c0p523d1'])+((coeff['ar1p523d1'])*(data[t-1,41])))+((coeff['c1p523d1'])*((x[37]- (data[t-1,21])))))+((coeff['c2p523d1'])*((data[t-1,21]- (data[t-2,21])))))+(((coeff['c3p523d1'])*(data[t-1,21]))*(((data[t-1,69])-((100)*((((data[t-1,51])/(data[t-5,51]))-(1))))- ((data[t-2,69])-((100)*((((data[t-2,51])/(data[t-6,51]))-(1)))))))))+(data[t-0,99]))
	f[18] = ((log(x[34])- (log(data[t-1,38]))))-((((((coeff['c0p51td1'])+((coeff['ar2p51td1'])*((log(data[t-2,38])- (log(data[t-3,38]))))))+((coeff['pib0p51td1'])*((log(x[48])- (log(data[t-1,49]))))))+((coeff['mu0p51td1'])*(log(((data[t-1,38])/(data[t-1,49]))))))+((coeff['mu1p51td1'])*(((log(((data[t-1,40])/(data[t-1,51]))))+(log((((data[t-0,68])/(100))+(0.08))-(log((data[t-1,40])/(data[t-4,40])))))))))+(data[t-0,97]))
	f[19] = (x[31])-((x[34])*(x[38]))
	f[20] = (x[2])-(((x[45])+(x[31]))+(x[41]))
	f[21] = (x[5])-((((((((((data[t-1,28])+(data[t-1,31]))+(data[t-1,25]))+(data[t-1,23]))+(data[t-1,44])))/((((((data[t-1,27])+(data[t-1,30]))+(data[t-1,77]))+(data[t-1,22]))+(data[t-1,43])))))*(x[15]))+(data[t-0,100]))
	f[22] = (x[8])-((x[20])/(x[4]))
	f[23] = ((log(x[4])- (log(data[t-1,24]))))-(((((((((coeff['ar1p3ad5'])*((log(data[t-1,24])- (log(data[t-2,24])))))+((coeff['ar2p3ad5'])*((log(data[t-2,24])- (log(data[t-3,24]))))))+((coeff['p70p3ad5'])*((log(x[52])- (log(data[t-1,48]))))))+((coeff['p71p3ad5'])*((log(data[t-1,48])- (log(data[t-2,48]))))))+((coeff['ulc1p3a5'])*((log(data[t-1,14])- (log(data[t-2,14]))))))+((coeff['cltp3ad5'])*(log((data[t-2,24])/(data[t-2,13])))))+(coeff['c0p3ad5']))+(data[t-0,90]))
	f[24] = ((log(x[28])- (log(data[t-1,34]))))-((((((((coeff['ar1p51gd5'])*((log(data[t-1,34])- (log(data[t-2,34])))))+((coeff['p70p51gd5'])*((log(x[52])- (log(data[t-1,48]))))))+((coeff['ulc0p51gg5'])*((log(x[6])- (log(data[t-1,14]))))))+((coeff['cltp51gd5'])*(log((data[t-1,34])/(data[t-1,13])))))+(coeff['c0p51gd5']))+((coeff['dum1p51gd5'])*(data[t-0,58])))+(data[t-0,94]))
	f[25] = (x[41])-((data[t-0,78])*(x[28]))
	f[26] = ((log(x[38])- (log(data[t-1,40]))))-((((((((coeff['ar1p51td5'])*((log(data[t-1,40])- (log(data[t-2,40])))))+((coeff['p70p51td5'])*((log(x[52])- (log(data[t-1,48]))))))+((coeff['ulc0p51td5'])*((log(x[6])- (log(data[t-1,14]))))))+((coeff['ulc1p51td5'])*((log(data[t-1,14])- (log(data[t-2,14]))))))+((coeff['cltp51td5'])*(log(((data[t-1,37])/(data[t-1,13]))))))+(coeff['c0p51td5']))+(data[t-0,98]))
	f[27] = ((log(x[10])- (log(data[t-1,29]))))-((((((((((coeff['ar1p3md5'])*((log(data[t-1,29])- (log(data[t-2,29])))))+((coeff['ar2p3md5'])*((log(data[t-2,29])- (log(data[t-3,29]))))))+((coeff['p70p3md5'])*((log(x[52])- (log(data[t-1,48]))))))+((coeff['ulc0p3m5'])*((log(x[6])- (log(data[t-1,14]))))))+((coeff['ulc1p3m5'])*((log(data[t-1,14])- (log(data[t-2,14]))))))+((coeff['cltp3md5'])*(log((data[t-2,29])/(data[t-2,13])))))+(coeff['c0p3md5']))+((coeff['dum1p3dmd5'])*(data[t-0,59])))+(data[t-0,93]))
	f[28] = (x[51])-(((0.25)*(((((data[t-1,29])+(data[t-2,29]))+(data[t-3,29]))+(data[t-4,29]))))*(data[t-0,74]))
	f[29] = ((log(x[12])- (log(data[t-1,27]))))-((((((((((coeff['c1p3md1'])*((log((x[22])/(x[10]))- (log((data[t-1,17])/(data[t-1,29]))))))+((coeff['c2p3md1'])*((log((data[t-1,17])/(data[t-1,29]))- (log((data[t-2,17])/(data[t-2,29])))))))+((coeff['c3p3md1'])*((log((data[t-2,17])/(data[t-2,29]))- (log((data[t-3,17])/(data[t-3,29])))))))+((coeff['c4p3md1'])*((log((data[t-3,17])/(data[t-3,29]))- (log((data[t-4,17])/(data[t-4,29])))))))+((coeff['c5p3md1'])*(((data[t-2,69])-(((((data[t-2,29])/(data[t-6,29]))-(1)))*(100))- ((data[t-3,69])-(((((data[t-3,29])/(data[t-7,29]))-(1)))*(100)))))))+((coeff['c6p3md1'])*((x[3]- (data[t-1,15])))))+((coeff['mup3md1'])*(log(((data[t-1,27])/(x[22]))*(data[t-1,29])))))+(coeff['c0p3md1']))+(data[t-0,92]))
	f[30] = (x[3])-(((((data[t-0,76])-(x[49])))/(data[t-0,76]))*(100))
	f[31] = (x[49])-(((x[24])/(((1)-(data[t-0,72]))))+(data[t-0,75]))
	f[32] = ((log(x[11])- (log(data[t-1,2]))))-((((((coeff['c0d11d5'])+((coeff['ar1d11d5'])*((log(data[t-1,2])- (log(data[t-2,2]))))))+((coeff['pc0d11d5'])*((log(x[10])- (log(data[t-1,29]))))))+((coeff['dum1d11d5'])*(((data[t-0,59])-(data[t-0,60])))))+((coeff['c3d11dim5'])*(log(x[3]))))+(data[t-0,85]))
	f[33] = ((log(x[24])- (log(data[t-1,12]))))-(((((coeff['c0empsd7'])+((coeff['ar1empsd7'])*((log(data[t-1,12])- (log(data[t-2,12]))))))+((((1)-(coeff['ar1empsd7'])))*((log(x[48])- (log(data[t-1,49]))))))+((coeff['c1empsd7'])*((((log(((x[11])/(x[47]))*(100))- (log(((data[t-1,2])/(data[t-1,51]))*(100)))))+((log(((data[t-1,2])/(data[t-1,51]))*(100))- (log(((data[t-2,2])/(data[t-2,51]))*(100)))))))))+(data[t-0,89]))
	f[34] = (x[47])-((x[19])/(x[48]))
	f[35] = (x[42])-((data[t-0,65])*(x[19]))
	f[36] = ((x[50]- (data[t-1,6])))-((((coeff['ar1d4zs143'])*((data[t-1,6]- (data[t-2,6]))))+((coeff['ac1d4zs143'])*((data[t-1,50]- (data[t-2,50])))))+(data[t-0,87]))
	f[37] = (x[40])-((data[t-0,54])*(x[19]))
	f[38] = (x[39])-(((((((x[40])+(x[46]))+(x[32]))+(x[50]))-(x[7]))+(x[51]))+(x[42]))
	f[39] = ((log(x[35])- (log(data[t-1,7]))))-(((((coeff['p1d5s14'])*(1.9))*((log(x[1])- (log(data[t-1,18])))))+((((1)-(coeff['p1d5s14'])))*((log(x[39])- (log(data[t-1,19]))))))+(data[t-0,88]))
	f[40] = (x[1])-(((((data[t-0,80])*(((((data[t-1,17])+(data[t-2,17]))+(data[t-3,17]))+(data[t-4,17]))))+((data[t-0,81])*(((((data[t-2,17])+(data[t-3,17]))+(data[t-4,17]))+(data[t-4,17])))))+((data[t-0,82])*(((((data[t-3,17])+(data[t-4,17]))+(data[t-4,17]))+(data[t-5,17])))))+((data[t-0,83])*(((((data[t-4,17])+(data[t-4,17]))+(data[t-5,17]))+(data[t-6,17])))))
	f[41] = (x[22])-((x[39])-(x[35]))
	f[42] = ((x[32])/(data[t-1,17]))-(((((coeff['c0d14s14s3'])+(((coeff['ard41s14s3'])*(data[t-1,5]))/(data[t-2,17])))+((coeff['rl0d41s14s3'])*(data[t-0,68])))+((coeff['r3md41s14s3'])*(((data[t-0,69])-((coeff['ard41s14s3'])*(data[t-1,69]))))))+(data[t-0,86]))
	f[43] = ((log(x[29])- (log(data[t-1,35]))))-((((((coeff['c0p51md1'])+((coeff['ar1p51md1'])*((log(data[t-1,35])- (log(data[t-2,35]))))))+((coeff['c1p51md1'])*((log(data[t-1,37])- (log(data[t-2,37]))))))+((coeff['mup51md1'])*(((log(data[t-1,35]))-(log(((data[t-1,17])/(data[t-1,37]))*(100)))))))+((coeff['ctlp51md1'])*(((data[t-1,68])-(((((data[t-1,37])/(data[t-5,37]))-(1)))*(100))))))+(data[t-0,95]))
	f[44] = (x[36])-(((x[29])+(x[34]))+(data[t-0,78]))
	f[45] = (x[37])-(((((x[12])+(x[36]))+(data[t-0,77]))+(x[8]))+(x[53]))
	f[46] = (x[9])-((x[12])*(x[10]))
	f[47] = (x[45])-((x[29])*(x[0]))
	f[48] = (x[20])-((data[t-0,56])*(x[22]))
	f[49] = (x[19])-(((((((x[9])+(x[2]))+(x[14]))+(x[20]))+(x[25]))+(x[5]))-(x[33]))
	f[50] = (x[48])-(((((((x[12])+(x[36]))+(data[t-0,77]))+(x[8]))+(x[53]))+(x[15]))-(x[27]))
	f[51] = (x[23])-((x[2])/(x[36]))
	f[52] = (x[43])-((data[t-0,67])/(x[16]))
	f[53] = ((log(x[13])- (log(data[t-1,52]))))-(data[t-0,105])
	return f

def colibri_0_jac(x,t,data,coeff): 
	"""
	Fonction produite automatiquement pour la résolution du modèle 

	Jacobienne de la fonction associée au bloc 
	
	Arguments : 
		x : vecteur de variables endogènes contemporaines 
		t : date courante (dans le tableau de données) 
		data : tableau numpy contenant les données du modèle 
	
	""" 
	df = np.zeros((54,54),dtype=np.float64)
	df[0][52] = (1/(x[52]))
	df[1][11] = -(x[24])
	df[1][17] = (1)
	df[1][24] = -(x[11])
	df[2][17] = -(data[t-0,70])
	df[2][46] = (1)
	df[3][7] = (1)
	df[3][46] = -(data[t-0,55])
	df[4][17] = -(((1)+(data[t-0,73])))
	df[4][18] = (1)
	df[5][6] = (1)
	df[5][18] = -(((((1)-(data[t-0,71])))/(x[48])))
	df[5][48] = -(-((((x[18])*(((1)-(data[t-0,71]))))/(x[48]))*(1/(x[48]))))
	df[6][6] = -((coeff['ulc0p6d5'])*(1/(x[6])))
	df[6][16] = (1/(x[16]))
	df[7][16] = -(((coeff['c3p6d1'])*(((1/(data[t-0,67]))/((x[16])/(data[t-0,67]))))))
	df[7][53] = (1/(x[53]))
	df[8][16] = -(x[53])
	df[8][25] = (1)
	df[8][53] = -(x[16])
	df[9][0] = (1/(x[0]))
	df[9][6] = -((coeff['ulc0p51m5'])*(1/(x[6])))
	df[10][6] = -((coeff['ulc0p3g5'])*(1/(x[6])))
	df[10][44] = (1/(x[44]))
	df[11][14] = (1)
	df[11][44] = -(data[t-0,77])
	df[12][6] = -((((1)-(x[26])))/(0.47))
	df[12][26] = -((x[52])+((((-(1)))*(x[6]))/(0.47)))
	df[12][30] = (1)
	df[12][52] = -(x[26])
	df[13][14] = -(-(((x[33])/(((((x[33])+(x[19]))-(x[14]))-(x[45]))))*((((-(1))))/(((((x[33])+(x[19]))-(x[14]))-(x[45]))))))
	df[13][19] = -(-(((x[33])/(((((x[33])+(x[19]))-(x[14]))-(x[45]))))*(((((1))))/(((((x[33])+(x[19]))-(x[14]))-(x[45]))))))
	df[13][26] = (1)
	df[13][33] = -((1/(((((x[33])+(x[19]))-(x[14]))-(x[45]))))-(((x[33])/(((((x[33])+(x[19]))-(x[14]))-(x[45]))))*(((((1))))/(((((x[33])+(x[19]))-(x[14]))-(x[45]))))))
	df[13][45] = -(-(((x[33])/(((((x[33])+(x[19]))-(x[14]))-(x[45]))))*(((-(1)))/(((((x[33])+(x[19]))-(x[14]))-(x[45]))))))
	df[14][27] = -(x[52])
	df[14][33] = (1)
	df[14][52] = -(x[27])
	df[15][6] = -((coeff['ulc0p7d1'])*(1/(x[6])))
	df[15][21] = -((coeff['c1p7d1'])*(1/((x[21])+(x[53]))))
	df[15][27] = (1/(x[27]))
	df[15][52] = -((coeff['p7d50p7d1'])*(1/(x[52])))
	df[15][53] = -((coeff['c1p7d1'])*(1/((x[21])+(x[53]))))
	df[16][15] = -(1)
	df[16][21] = (1)
	df[16][37] = -(1)
	df[17][15] = (1)
	df[17][37] = -(coeff['c1p523d1'])
	df[18][34] = (1/(x[34]))
	df[18][48] = -((coeff['pib0p51td1'])*(1/(x[48])))
	df[19][31] = (1)
	df[19][34] = -(x[38])
	df[19][38] = -(x[34])
	df[20][2] = (1)
	df[20][31] = -(1)
	df[20][41] = -(1)
	df[20][45] = -(1)
	df[21][5] = (1)
	df[21][15] = -((((((((data[t-1,28])+(data[t-1,31]))+(data[t-1,25]))+(data[t-1,23]))+(data[t-1,44])))/((((((data[t-1,27])+(data[t-1,30]))+(data[t-1,77]))+(data[t-1,22]))+(data[t-1,43])))))
	df[22][4] = -(-(((x[20])/(x[4]))*(1/(x[4]))))
	df[22][8] = (1)
	df[22][20] = -((1/(x[4])))
	df[23][4] = (1/(x[4]))
	df[23][52] = -((coeff['p70p3ad5'])*(1/(x[52])))
	df[24][6] = -((coeff['ulc0p51gg5'])*(1/(x[6])))
	df[24][28] = (1/(x[28]))
	df[24][52] = -((coeff['p70p51gd5'])*(1/(x[52])))
	df[25][28] = -(data[t-0,78])
	df[25][41] = (1)
	df[26][6] = -((coeff['ulc0p51td5'])*(1/(x[6])))
	df[26][38] = (1/(x[38]))
	df[26][52] = -((coeff['p70p51td5'])*(1/(x[52])))
	df[27][6] = -((coeff['ulc0p3m5'])*(1/(x[6])))
	df[27][10] = (1/(x[10]))
	df[27][52] = -((coeff['p70p3md5'])*(1/(x[52])))
	df[28][51] = (1)
	df[29][3] = -(coeff['c6p3md1'])
	df[29][10] = -((coeff['c1p3md1'])*((-(((x[22])/(x[10]))*(1/(x[10]))))/((x[22])/(x[10]))))
	df[29][12] = (1/(x[12]))
	df[29][22] = -(((coeff['c1p3md1'])*(((1/(x[10])))/((x[22])/(x[10]))))+((coeff['mup3md1'])*(((-(((data[t-1,27])/(x[22]))*(1/(x[22]))))*(data[t-1,29]))/(((data[t-1,27])/(x[22]))*(data[t-1,29])))))
	df[30][3] = (1)
	df[30][49] = -((((-1))/(data[t-0,76]))*(100))
	df[31][24] = -(1/(((1)-(data[t-0,72]))))
	df[31][49] = (1)
	df[32][3] = -((coeff['c3d11dim5'])*(1/(x[3])))
	df[32][10] = -((coeff['pc0d11d5'])*(1/(x[10])))
	df[32][11] = (1/(x[11]))
	df[33][11] = -((coeff['c1empsd7'])*(((((1/(x[47])))*(100))/(((x[11])/(x[47]))*(100)))))
	df[33][24] = (1/(x[24]))
	df[33][47] = -((coeff['c1empsd7'])*((((-(((x[11])/(x[47]))*(1/(x[47]))))*(100))/(((x[11])/(x[47]))*(100)))))
	df[33][48] = -((((1)-(coeff['ar1empsd7'])))*(1/(x[48])))
	df[34][19] = -((1/(x[48])))
	df[34][47] = (1)
	df[34][48] = -(-(((x[19])/(x[48]))*(1/(x[48]))))
	df[35][19] = -(data[t-0,65])
	df[35][42] = (1)
	df[36][50] = (1)
	df[37][19] = -(data[t-0,54])
	df[37][40] = (1)
	df[38][7] = -(-(1))
	df[38][32] = -((1))
	df[38][39] = (1)
	df[38][40] = -((1))
	df[38][42] = -(1)
	df[38][46] = -((1))
	df[38][50] = -((1))
	df[38][51] = -(1)
	df[39][1] = -(((coeff['p1d5s14'])*(1.9))*(1/(x[1])))
	df[39][35] = (1/(x[35]))
	df[39][39] = -((((1)-(coeff['p1d5s14'])))*(1/(x[39])))
	df[40][1] = (1)
	df[41][22] = (1)
	df[41][35] = -(-(1))
	df[41][39] = -((1))
	df[42][32] = (1/(data[t-1,17]))
	df[43][29] = (1/(x[29]))
	df[44][29] = -(1)
	df[44][34] = -(1)
	df[44][36] = (1)
	df[45][8] = -(1)
	df[45][12] = -(1)
	df[45][36] = -(1)
	df[45][37] = (1)
	df[45][53] = -(1)
	df[46][9] = (1)
	df[46][10] = -(x[12])
	df[46][12] = -(x[10])
	df[47][0] = -(x[29])
	df[47][29] = -(x[0])
	df[47][45] = (1)
	df[48][20] = (1)
	df[48][22] = -(data[t-0,56])
	df[49][2] = -((1))
	df[49][5] = -((1))
	df[49][9] = -((1))
	df[49][14] = -((1))
	df[49][19] = (1)
	df[49][20] = -((1))
	df[49][25] = -((1))
	df[49][33] = -(-(1))
	df[50][8] = -((1))
	df[50][12] = -((1))
	df[50][15] = -((1))
	df[50][27] = -(-(1))
	df[50][36] = -((1))
	df[50][48] = (1)
	df[50][53] = -((1))
	df[51][2] = -((1/(x[36])))
	df[51][23] = (1)
	df[51][36] = -(-(((x[2])/(x[36]))*(1/(x[36]))))
	df[52][16] = -(-(((data[t-0,67])/(x[16]))*(1/(x[16]))))
	df[52][43] = (1)
	df[53][13] = (1/(x[13]))
	return df

