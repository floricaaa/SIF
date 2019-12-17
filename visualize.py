import torch
import numpy as np
from models import Network_MLP, Network_MLP_Single_Triple


dataset = 'ml-100k'
if dataset == 'ml-100k':
	num_users = 9433
	num_items = 1682
elif dataset == 'ml-1m':
	num_users = 6040
	num_items = 3952
elif dataset == 'ml-10m':
	num_users = 71567
	num_items = 65133
elif dataset == 'ml-20m':
	num_users = 138493
	num_items = 131262
elif dataset == 'youtube_small':
	num_ps = 600
	num_qs = 14340
	num_rs = 5
elif dataset == 'youtube':
	num_ps = 15088
	num_qs = 15088
	num_rs = 5

embedding_dim, reg = 8, 1e-5
path = '/data3/chenxiangning/models/binarydarts_mlp_ml-100k_8_Adagrad0.05_5e-05_3'
gpu = 6
torch.cuda.set_device(gpu)

network_mlp = Network_MLP(num_users, num_items, embedding_dim, reg)
network_mlp.load_state_dict(torch.load(path))

mlp_p = network_mlp.mlp_p
mlp_q = network_mlp.mlp_q

inputs = torch.tensor(np.linspace(-3,3,500).tolist()).cuda().view(-1,1)
outputs_p = mlp_p(inputs).view(-1)
outputs_q = mlp_q(inputs).view(-1)

print(outputs_p)
print(outputs_q)


p_2 = [ 0.4697,  0.4683,  0.4669,  0.4654,  0.4640,  0.4625,  0.4611, ...
         0.4596,  0.4581,  0.4566,  0.4552,  0.4537,  0.4522,  0.4507, ...
         0.4491,  0.4476,  0.4461,  0.4446,  0.4430,  0.4415,  0.4399, ...
         0.4384,  0.4368,  0.4352,  0.4337,  0.4321,  0.4305,  0.4289, ...
         0.4273,  0.4257,  0.4240,  0.4224,  0.4208,  0.4191,  0.4175, ...
         0.4159,  0.4142,  0.4125,  0.4109,  0.4092,  0.4075,  0.4058, ...
         0.4041,  0.4024,  0.4007,  0.3990,  0.3972,  0.3955,  0.3938, ...
         0.3920,  0.3903,  0.3885,  0.3867,  0.3850,  0.3832,  0.3814, ...
         0.3796,  0.3778,  0.3760,  0.3742,  0.3724,  0.3706,  0.3687, ...
         0.3669,  0.3650,  0.3632,  0.3613,  0.3595,  0.3576,  0.3557, ...
         0.3538,  0.3520,  0.3501,  0.3482,  0.3463,  0.3443,  0.3424, ...
         0.3405,  0.3386,  0.3366,  0.3347,  0.3327,  0.3308,  0.3288, ...
         0.3269,  0.3249,  0.3229,  0.3209,  0.3189,  0.3170,  0.3150, ...
         0.3130,  0.3110,  0.3089,  0.3069,  0.3049,  0.3029,  0.3008, ...
         0.2988,  0.2968,  0.2947,  0.2927,  0.2906,  0.2886,  0.2865, ...
         0.2844,  0.2824,  0.2803,  0.2782,  0.2762,  0.2741,  0.2720, ...
         0.2699,  0.2678,  0.2657,  0.2636,  0.2615,  0.2594,  0.2573, ...
         0.2552,  0.2531,  0.2510,  0.2489,  0.2468,  0.2447,  0.2426, ...
         0.2405,  0.2384,  0.2362,  0.2341,  0.2320,  0.2299,  0.2278, ...
         0.2257,  0.2236,  0.2215,  0.2194,  0.2172,  0.2151,  0.2130, ...
         0.2109,  0.2088,  0.2067,  0.2046,  0.2025,  0.2004,  0.1984, ...
         0.1963,  0.1942,  0.1921,  0.1900,  0.1880,  0.1859,  0.1839, ...
         0.1818,  0.1798,  0.1777,  0.1757,  0.1736,  0.1716,  0.1696, ...
         0.1676,  0.1656,  0.1636,  0.1616,  0.1596,  0.1576,  0.1557, ...
         0.1537,  0.1517,  0.1498,  0.1479,  0.1459,  0.1440,  0.1421, ...
         0.1402,  0.1383,  0.1365,  0.1346,  0.1327,  0.1309,  0.1291, ...
         0.1272,  0.1254,  0.1236,  0.1218,  0.1201,  0.1183,  0.1165, ...
         0.1148,  0.1131,  0.1114,  0.1097,  0.1080,  0.1063,  0.1046, ...
         0.1030,  0.1014,  0.0997,  0.0981,  0.0965,  0.0949,  0.0934, ...
         0.0918,  0.0903,  0.0888,  0.0872,  0.0857,  0.0843,  0.0828, ...
         0.0813,  0.0799,  0.0785,  0.0770,  0.0756,  0.0742,  0.0729, ...
         0.0715,  0.0702,  0.0688,  0.0675,  0.0662,  0.0649,  0.0636, ...
         0.0623,  0.0610,  0.0598,  0.0586,  0.0573,  0.0561,  0.0549, ...
         0.0537,  0.0525,  0.0513,  0.0502,  0.0490,  0.0479,  0.0467, ...
         0.0456,  0.0445,  0.0434,  0.0423,  0.0412,  0.0401,  0.0390, ...
         0.0379,  0.0368,  0.0358,  0.0347,  0.0336,  0.0326,  0.0315, ...
         0.0305,  0.0294,  0.0284,  0.0274,  0.0263,  0.0253,  0.0243, ...
         0.0232,  0.0222,  0.0212,  0.0202,  0.0191,  0.0181,  0.0171, ...
         0.0161,  0.0150,  0.0140,  0.0130,  0.0119,  0.0109,  0.0099, ...
         0.0088,  0.0078,  0.0067,  0.0057,  0.0046,  0.0035,  0.0025, ...
         0.0014,  0.0003, -0.0008, -0.0019, -0.0030, -0.0041, -0.0052, ...
        -0.0063, -0.0074, -0.0085, -0.0097, -0.0108, -0.0120, -0.0131, ...
        -0.0143, -0.0154, -0.0166, -0.0178, -0.0190, -0.0202, -0.0214, ...
        -0.0226, -0.0239, -0.0251, -0.0264, -0.0276, -0.0289, -0.0301, ...
        -0.0314, -0.0327, -0.0340, -0.0353, -0.0366, -0.0379, -0.0393, ...
        -0.0406, -0.0420, -0.0433, -0.0447, -0.0461, -0.0474, -0.0488, ...
        -0.0502, -0.0516, -0.0531, -0.0545, -0.0559, -0.0573, -0.0588, ...
        -0.0602, -0.0617, -0.0632, -0.0647, -0.0661, -0.0676, -0.0691, ...
        -0.0706, -0.0722, -0.0737, -0.0752, -0.0767, -0.0783, -0.0798, ...
        -0.0814, -0.0829, -0.0845, -0.0861, -0.0876, -0.0892, -0.0908, ...
        -0.0924, -0.0940, -0.0956, -0.0972, -0.0988, -0.1004, -0.1021, ...
        -0.1037, -0.1053, -0.1069, -0.1086, -0.1102, -0.1119, -0.1135, ...
        -0.1152, -0.1168, -0.1185, -0.1201, -0.1218, -0.1235, -0.1251, ...
        -0.1268, -0.1285, -0.1301, -0.1318, -0.1335, -0.1351, -0.1368, ...
        -0.1385, -0.1402, -0.1419, -0.1435, -0.1452, -0.1469, -0.1486, ...
        -0.1503, -0.1519, -0.1536, -0.1553, -0.1570, -0.1587, -0.1603, ...
        -0.1620, -0.1637, -0.1654, -0.1670, -0.1687, -0.1704, -0.1720, ...
        -0.1737, -0.1754, -0.1770, -0.1787, -0.1803, -0.1820, -0.1837, ...
        -0.1853, -0.1869, -0.1886, -0.1902, -0.1919, -0.1935, -0.1951, ...
        -0.1968, -0.1984, -0.2000, -0.2016, -0.2032, -0.2049, -0.2065, ...
        -0.2081, -0.2097, -0.2113, -0.2128, -0.2144, -0.2160, -0.2176, ...
        -0.2192, -0.2207, -0.2223, -0.2239, -0.2254, -0.2270, -0.2285, ...
        -0.2300, -0.2316, -0.2331, -0.2346, -0.2362, -0.2377, -0.2392, ...
        -0.2407, -0.2422, -0.2437, -0.2452, -0.2466, -0.2481, -0.2496, ...
        -0.2511, -0.2525, -0.2540, -0.2554, -0.2569, -0.2583, -0.2597, ...
        -0.2612, -0.2626, -0.2640, -0.2654, -0.2668, -0.2682, -0.2696, ...
        -0.2710, -0.2723, -0.2737, -0.2751, -0.2764, -0.2778, -0.2791, ...
        -0.2805, -0.2818, -0.2831, -0.2845, -0.2858, -0.2871, -0.2884, ...
        -0.2897, -0.2910, -0.2923, -0.2935, -0.2948, -0.2961, -0.2973, ...
        -0.2986, -0.2998, -0.3011, -0.3023, -0.3035, -0.3048, -0.3060, ...
        -0.3072, -0.3084, -0.3096, -0.3108, -0.3120, -0.3132, -0.3143, ...
        -0.3155, -0.3167, -0.3178]


q_2 = [ 0.2233,  0.2234,  0.2235,  0.2235,  0.2236,  0.2237,  0.2238, ...
         0.2239,  0.2240,  0.2242,  0.2243,  0.2244,  0.2245,  0.2246, ...
         0.2247,  0.2248,  0.2249,  0.2250,  0.2251,  0.2253,  0.2254, ...
         0.2255,  0.2256,  0.2257,  0.2258,  0.2260,  0.2261,  0.2262, ...
         0.2263,  0.2265,  0.2266,  0.2267,  0.2268,  0.2270,  0.2271, ...
         0.2272,  0.2274,  0.2275,  0.2276,  0.2277,  0.2279,  0.2280, ...
         0.2281,  0.2283,  0.2284,  0.2285,  0.2287,  0.2288,  0.2289, ...
         0.2291,  0.2292,  0.2293,  0.2295,  0.2296,  0.2297,  0.2299, ...
         0.2300,  0.2301,  0.2303,  0.2304,  0.2305,  0.2306,  0.2308, ...
         0.2309,  0.2310,  0.2311,  0.2313,  0.2314,  0.2315,  0.2316, ...
         0.2317,  0.2318,  0.2319,  0.2320,  0.2321,  0.2322,  0.2323, ...
         0.2324,  0.2325,  0.2326,  0.2327,  0.2328,  0.2329,  0.2329, ...
         0.2330,  0.2331,  0.2331,  0.2332,  0.2332,  0.2333,  0.2333, ...
         0.2333,  0.2334,  0.2334,  0.2334,  0.2334,  0.2334,  0.2334, ...
         0.2334,  0.2334,  0.2333,  0.2333,  0.2332,  0.2332,  0.2331, ...
         0.2330,  0.2330,  0.2329,  0.2327,  0.2326,  0.2325,  0.2324, ...
         0.2322,  0.2320,  0.2319,  0.2317,  0.2315,  0.2313,  0.2310, ...
         0.2308,  0.2305,  0.2302,  0.2300,  0.2296,  0.2293,  0.2290, ...
         0.2286,  0.2282,  0.2278,  0.2274,  0.2270,  0.2265,  0.2260, ...
         0.2256,  0.2250,  0.2245,  0.2239,  0.2233,  0.2227,  0.2221, ...
         0.2214,  0.2207,  0.2200,  0.2193,  0.2185,  0.2177,  0.2169, ...
         0.2160,  0.2152,  0.2143,  0.2133,  0.2123,  0.2113,  0.2103, ...
         0.2092,  0.2081,  0.2070,  0.2058,  0.2046,  0.2034,  0.2021, ...
         0.2008,  0.1994,  0.1980,  0.1966,  0.1951,  0.1936,  0.1920, ...
         0.1904,  0.1888,  0.1871,  0.1854,  0.1836,  0.1818,  0.1799, ...
         0.1780,  0.1761,  0.1741,  0.1721,  0.1700,  0.1679,  0.1657, ...
         0.1635,  0.1612,  0.1589,  0.1565,  0.1541,  0.1516,  0.1491, ...
         0.1465,  0.1439,  0.1413,  0.1386,  0.1358,  0.1330,  0.1301, ...
         0.1272,  0.1243,  0.1212,  0.1182,  0.1151,  0.1119,  0.1087, ...
         0.1055,  0.1022,  0.0989,  0.0955,  0.0920,  0.0886,  0.0851, ...
         0.0815,  0.0779,  0.0742,  0.0706,  0.0668,  0.0631,  0.0593, ...
         0.0554,  0.0516,  0.0477,  0.0437,  0.0398,  0.0358,  0.0317, ...
         0.0277,  0.0236,  0.0195,  0.0154,  0.0112,  0.0071,  0.0029, ...
        -0.0013, -0.0055, -0.0097, -0.0140, -0.0182, -0.0224, -0.0267, ...
        -0.0309, -0.0352, -0.0394, -0.0436, -0.0479, -0.0521, -0.0563, ...
        -0.0605, -0.0646, -0.0688, -0.0729, -0.0770, -0.0811, -0.0852, ...
        -0.0892, -0.0932, -0.0971, -0.1010, -0.1049, -0.1087, -0.1125, ...
        -0.1163, -0.1200, -0.1236, -0.1272, -0.1307, -0.1342, -0.1376, ...
        -0.1410, -0.1443, -0.1475, -0.1506, -0.1537, -0.1567, -0.1597, ...
        -0.1625, -0.1653, -0.1680, -0.1707, -0.1732, -0.1757, -0.1781, ...
        -0.1804, -0.1826, -0.1847, -0.1868, -0.1887, -0.1906, -0.1924, ...
        -0.1940, -0.1956, -0.1971, -0.1985, -0.1998, -0.2010, -0.2021, ...
        -0.2031, -0.2041, -0.2049, -0.2056, -0.2063, -0.2068, -0.2072, ...
        -0.2076, -0.2078, -0.2080, -0.2080, -0.2080, -0.2079, -0.2076, ...
        -0.2073, -0.2069, -0.2064, -0.2058, -0.2052, -0.2044, -0.2035, ...
        -0.2026, -0.2016, -0.2004, -0.1992, -0.1980, -0.1966, -0.1952, ...
        -0.1936, -0.1920, -0.1904, -0.1886, -0.1868, -0.1849, -0.1830, ...
        -0.1809, -0.1788, -0.1767, -0.1744, -0.1721, -0.1698, -0.1674, ...
        -0.1649, -0.1624, -0.1598, -0.1572, -0.1545, -0.1518, -0.1490, ...
        -0.1462, -0.1434, -0.1405, -0.1375, -0.1346, -0.1315, -0.1285, ...
        -0.1254, -0.1223, -0.1192, -0.1160, -0.1128, -0.1096, -0.1064, ...
        -0.1031, -0.0998, -0.0965, -0.0932, -0.0899, -0.0866, -0.0832, ...
        -0.0798, -0.0765, -0.0731, -0.0697, -0.0663, -0.0629, -0.0596, ...
        -0.0562, -0.0528, -0.0494, -0.0460, -0.0426, -0.0393, -0.0359, ...
        -0.0326, -0.0292, -0.0259, -0.0226, -0.0192, -0.0160, -0.0127, ...
        -0.0094, -0.0062, -0.0029,  0.0003,  0.0035,  0.0067,  0.0098, ...
         0.0130,  0.0161,  0.0192,  0.0223,  0.0253,  0.0283,  0.0313, ...
         0.0343,  0.0373,  0.0402,  0.0431,  0.0460,  0.0488,  0.0516, ...
         0.0544,  0.0572,  0.0599,  0.0627,  0.0653,  0.0680,  0.0706, ...
         0.0732,  0.0758,  0.0783,  0.0808,  0.0833,  0.0858,  0.0882, ...
         0.0906,  0.0930,  0.0953,  0.0976,  0.0999,  0.1022,  0.1044, ...
         0.1066,  0.1087,  0.1109,  0.1130,  0.1151,  0.1171,  0.1191, ...
         0.1211,  0.1231,  0.1250,  0.1269,  0.1288,  0.1307,  0.1325, ...
         0.1343,  0.1361,  0.1378,  0.1396,  0.1413,  0.1429,  0.1446, ...
         0.1462,  0.1478,  0.1494,  0.1509,  0.1524,  0.1539,  0.1554, ...
         0.1568,  0.1583,  0.1597,  0.1611,  0.1624,  0.1637,  0.1650, ...
         0.1663,  0.1676,  0.1688,  0.1701,  0.1713,  0.1724,  0.1736, ...
         0.1747,  0.1759,  0.1770,  0.1780,  0.1791,  0.1801,  0.1812, ...
         0.1822,  0.1831,  0.1841,  0.1851,  0.1860,  0.1869,  0.1878, ...
         0.1887,  0.1895,  0.1904,  0.1912,  0.1920,  0.1928,  0.1936, ...
         0.1943,  0.1951,  0.1958,  0.1965,  0.1972,  0.1979,  0.1986, ...
         0.1993,  0.1999,  0.2005]
























# p = [0.2517,  0.2505,  0.2493,  0.2481,  0.2469,  0.2457,  0.2445, ...
#          0.2433,  0.2421,  0.2409,  0.2397,  0.2385,  0.2373,  0.2360, ...
#          0.2348,  0.2336,  0.2324,  0.2312,  0.2299,  0.2287,  0.2275, ...
#          0.2263,  0.2250,  0.2238,  0.2226,  0.2213,  0.2201,  0.2189, ...
#          0.2176,  0.2164,  0.2151,  0.2139,  0.2127,  0.2114,  0.2102, ...
#          0.2089,  0.2077,  0.2064,  0.2052,  0.2039,  0.2027,  0.2014, ...
#          0.2002,  0.1989,  0.1977,  0.1964,  0.1952,  0.1939,  0.1927, ...
#          0.1914,  0.1902,  0.1889,  0.1877,  0.1864,  0.1852,  0.1839, ...
#          0.1827,  0.1814,  0.1802,  0.1789,  0.1777,  0.1764,  0.1752, ...
#          0.1739,  0.1727,  0.1715,  0.1702,  0.1690,  0.1677,  0.1665, ...
#          0.1652,  0.1640,  0.1628,  0.1615,  0.1603,  0.1591,  0.1578, ...
#          0.1566,  0.1554,  0.1542,  0.1529,  0.1517,  0.1505,  0.1493, ...
#          0.1481,  0.1469,  0.1457,  0.1445,  0.1433,  0.1421,  0.1409, ...
#          0.1397,  0.1385,  0.1373,  0.1361,  0.1349,  0.1337,  0.1326, ...
#          0.1314,  0.1302,  0.1291,  0.1279,  0.1268,  0.1256,  0.1245, ...
#          0.1233,  0.1222,  0.1211,  0.1199,  0.1188,  0.1177,  0.1166, ...
#          0.1155,  0.1144,  0.1133,  0.1122,  0.1111,  0.1100,  0.1090, ...
#          0.1079,  0.1068,  0.1058,  0.1047,  0.1037,  0.1027,  0.1016, ...
#          0.1006,  0.0996,  0.0986,  0.0976,  0.0966,  0.0956,  0.0946, ...
#          0.0936,  0.0927,  0.0917,  0.0908,  0.0898,  0.0889,  0.0879, ...
#          0.0870,  0.0861,  0.0852,  0.0843,  0.0834,  0.0825,  0.0817, ...
#          0.0808,  0.0799,  0.0791,  0.0782,  0.0774,  0.0766,  0.0758, ...
#          0.0750,  0.0742,  0.0734,  0.0726,  0.0718,  0.0711,  0.0703, ...
#          0.0696,  0.0688,  0.0681,  0.0674,  0.0667,  0.0660,  0.0653, ...
#          0.0646,  0.0640,  0.0633,  0.0626,  0.0620,  0.0613,  0.0607, ...
#          0.0601,  0.0595,  0.0589,  0.0583,  0.0577,  0.0571,  0.0566, ...
#          0.0560,  0.0555,  0.0549,  0.0544,  0.0538,  0.0533,  0.0528, ...
#          0.0523,  0.0518,  0.0513,  0.0508,  0.0504,  0.0499,  0.0494, ...
#          0.0490,  0.0485,  0.0481,  0.0477,  0.0472,  0.0468,  0.0464, ...
#          0.0460,  0.0456,  0.0452,  0.0448,  0.0444,  0.0440,  0.0436, ...
#          0.0433,  0.0429,  0.0425,  0.0422,  0.0418,  0.0415,  0.0411, ...
#          0.0408,  0.0404,  0.0401,  0.0397,  0.0394,  0.0391,  0.0387, ...
#          0.0384,  0.0381,  0.0377,  0.0374,  0.0371,  0.0368,  0.0364, ...
#          0.0361,  0.0358,  0.0355,  0.0351,  0.0348,  0.0345,  0.0342, ...
#          0.0338,  0.0335,  0.0332,  0.0328,  0.0325,  0.0322,  0.0318, ...
#          0.0315,  0.0311,  0.0308,  0.0304,  0.0301,  0.0297,  0.0294, ...
#          0.0290,  0.0286,  0.0283,  0.0279,  0.0275,  0.0271,  0.0268, ...
#          0.0264,  0.0260,  0.0256,  0.0252,  0.0247,  0.0243,  0.0239, ...
#          0.0235,  0.0231,  0.0226,  0.0222,  0.0217,  0.0213,  0.0208, ...
#          0.0203,  0.0199,  0.0194,  0.0189,  0.0184,  0.0179,  0.0174, ...
#          0.0169,  0.0164,  0.0159,  0.0153,  0.0148,  0.0143,  0.0137, ...
#          0.0132,  0.0126,  0.0120,  0.0115,  0.0109,  0.0103,  0.0097, ...
#          0.0091,  0.0085,  0.0079,  0.0073,  0.0067,  0.0060,  0.0054, ...
#          0.0048,  0.0041,  0.0035,  0.0028,  0.0021,  0.0015,  0.0008, ...
#          0.0001, -0.0006, -0.0013, -0.0020, -0.0027, -0.0034, -0.0041, ...
#         -0.0048, -0.0055, -0.0062, -0.0070, -0.0077, -0.0085, -0.0092, ...
#         -0.0100, -0.0107, -0.0115, -0.0122, -0.0130, -0.0138, -0.0146, ...
#         -0.0153, -0.0161, -0.0169, -0.0177, -0.0185, -0.0193, -0.0201, ...
#         -0.0209, -0.0217, -0.0226, -0.0234, -0.0242, -0.0250, -0.0258, ...
#         -0.0267, -0.0275, -0.0283, -0.0292, -0.0300, -0.0309, -0.0317, ...
#         -0.0326, -0.0334, -0.0343, -0.0351, -0.0360, -0.0368, -0.0377, ...
#         -0.0385, -0.0394, -0.0403, -0.0411, -0.0420, -0.0429, -0.0437, ...
#         -0.0446, -0.0455, -0.0463, -0.0472, -0.0481, -0.0490, -0.0498, ...
#         -0.0507, -0.0516, -0.0525, -0.0533, -0.0542, -0.0551, -0.0560, ...
#         -0.0569, -0.0577, -0.0586, -0.0595, -0.0604, -0.0612, -0.0621, ...
#         -0.0630, -0.0639, -0.0647, -0.0656, -0.0665, -0.0674, -0.0682, ...
#         -0.0691, -0.0700, -0.0709, -0.0717, -0.0726, -0.0735, -0.0743, ...
#         -0.0752, -0.0761, -0.0769, -0.0778, -0.0787, -0.0795, -0.0804, ...
#         -0.0812, -0.0821, -0.0829, -0.0838, -0.0847, -0.0855, -0.0864, ...
#         -0.0872, -0.0880, -0.0889, -0.0897, -0.0906, -0.0914, -0.0923, ...
#         -0.0931, -0.0939, -0.0948, -0.0956, -0.0964, -0.0972, -0.0981, ...
#         -0.0989, -0.0997, -0.1005, -0.1013, -0.1022, -0.1030, -0.1038, ...
#         -0.1046, -0.1054, -0.1062, -0.1070, -0.1078, -0.1086, -0.1094, ...
#         -0.1102, -0.1110, -0.1117, -0.1125, -0.1133, -0.1141, -0.1149, ...
#         -0.1156, -0.1164, -0.1172, -0.1180, -0.1187, -0.1195, -0.1202, ...
#         -0.1210, -0.1218, -0.1225, -0.1233, -0.1240, -0.1248, -0.1255, ...
#         -0.1262, -0.1270, -0.1277, -0.1284, -0.1292, -0.1299, -0.1306, ...
#         -0.1314, -0.1321, -0.1328, -0.1335, -0.1342, -0.1349, -0.1356, ...
#         -0.1363, -0.1370, -0.1377, -0.1384, -0.1391, -0.1398, -0.1405, ...
#         -0.1412, -0.1419, -0.1426, -0.1432, -0.1439, -0.1446, -0.1452, ...
#         -0.1459, -0.1466, -0.1472, -0.1479, -0.1486, -0.1492, -0.1499, ...
#         -0.1505, -0.1512, -0.1518]


# q = [-0.1777, -0.1765, -0.1753, -0.1740, -0.1728, -0.1715, -0.1702, ...
#         -0.1689, -0.1677, -0.1664, -0.1651, -0.1637, -0.1624, -0.1611, ...
#         -0.1598, -0.1584, -0.1571, -0.1557, -0.1543, -0.1530, -0.1516, ...
#         -0.1502, -0.1488, -0.1474, -0.1459, -0.1445, -0.1431, -0.1416, ...
#         -0.1402, -0.1387, -0.1372, -0.1358, -0.1343, -0.1328, -0.1313, ...
#         -0.1298, -0.1282, -0.1267, -0.1252, -0.1236, -0.1221, -0.1205, ...
#         -0.1190, -0.1174, -0.1158, -0.1142, -0.1126, -0.1110, -0.1094, ...
#         -0.1078, -0.1061, -0.1045, -0.1028, -0.1012, -0.0995, -0.0979, ...
#         -0.0962, -0.0945, -0.0928, -0.0911, -0.0894, -0.0877, -0.0860, ...
#         -0.0842, -0.0825, -0.0808, -0.0790, -0.0773, -0.0755, -0.0738, ...
#         -0.0720, -0.0702, -0.0684, -0.0666, -0.0648, -0.0630, -0.0612, ...
#         -0.0594, -0.0576, -0.0558, -0.0540, -0.0522, -0.0503, -0.0485, ...
#         -0.0466, -0.0448, -0.0430, -0.0411, -0.0392, -0.0374, -0.0355, ...
#         -0.0337, -0.0318, -0.0299, -0.0281, -0.0262, -0.0243, -0.0224, ...
#         -0.0206, -0.0187, -0.0168, -0.0149, -0.0131, -0.0112, -0.0093, ...
#         -0.0074, -0.0056, -0.0037, -0.0018,  0.0000,  0.0019,  0.0038, ...
#          0.0056,  0.0075,  0.0093,  0.0112,  0.0130,  0.0149,  0.0167, ...
#          0.0185,  0.0204,  0.0222,  0.0240,  0.0258,  0.0276,  0.0294, ...
#          0.0312,  0.0329,  0.0347,  0.0365,  0.0382,  0.0399,  0.0416, ...
#          0.0434,  0.0451,  0.0467,  0.0484,  0.0501,  0.0517,  0.0533, ...
#          0.0549,  0.0565,  0.0581,  0.0597,  0.0612,  0.0628,  0.0643, ...
#          0.0658,  0.0672,  0.0687,  0.0701,  0.0715,  0.0729,  0.0743, ...
#          0.0756,  0.0769,  0.0782,  0.0795,  0.0807,  0.0820,  0.0831, ...
#          0.0843,  0.0854,  0.0865,  0.0876,  0.0887,  0.0897,  0.0906, ...
#          0.0916,  0.0925,  0.0934,  0.0942,  0.0950,  0.0958,  0.0965, ...
#          0.0972,  0.0979,  0.0985,  0.0991,  0.0996,  0.1001,  0.1006, ...
#          0.1010,  0.1014,  0.1017,  0.1020,  0.1022,  0.1024,  0.1026, ...
#          0.1027,  0.1027,  0.1027,  0.1027,  0.1026,  0.1024,  0.1022, ...
#          0.1020,  0.1017,  0.1013,  0.1009,  0.1005,  0.1000,  0.0994, ...
#          0.0988,  0.0981,  0.0973,  0.0966,  0.0957,  0.0948,  0.0938, ...
#          0.0928,  0.0917,  0.0906,  0.0894,  0.0881,  0.0868,  0.0854, ...
#          0.0840,  0.0825,  0.0809,  0.0793,  0.0776,  0.0759,  0.0741, ...
#          0.0722,  0.0703,  0.0683,  0.0663,  0.0642,  0.0620,  0.0598, ...
#          0.0576,  0.0552,  0.0528,  0.0504,  0.0479,  0.0453,  0.0427, ...
#          0.0400,  0.0373,  0.0345,  0.0317,  0.0288,  0.0258,  0.0229, ...
#          0.0198,  0.0167,  0.0136,  0.0104,  0.0072,  0.0039,  0.0006, ...
#         -0.0027, -0.0061, -0.0096, -0.0130, -0.0165, -0.0201, -0.0236, ...
#         -0.0272, -0.0309, -0.0345, -0.0382, -0.0419, -0.0456, -0.0494, ...
#         -0.0531, -0.0569, -0.0607, -0.0645, -0.0684, -0.0722, -0.0760, ...
#         -0.0798, -0.0837, -0.0875, -0.0914, -0.0952, -0.0990, -0.1028, ...
#         -0.1066, -0.1104, -0.1142, -0.1179, -0.1216, -0.1254, -0.1290, ...
#         -0.1327, -0.1363, -0.1399, -0.1434, -0.1469, -0.1504, -0.1538, ...
#         -0.1572, -0.1605, -0.1638, -0.1670, -0.1702, -0.1733, -0.1764, ...
#         -0.1794, -0.1823, -0.1852, -0.1880, -0.1907, -0.1933, -0.1959, ...
#         -0.1984, -0.2009, -0.2032, -0.2055, -0.2076, -0.2097, -0.2117, ...
#         -0.2137, -0.2155, -0.2172, -0.2189, -0.2204, -0.2219, -0.2233, ...
#         -0.2245, -0.2257, -0.2268, -0.2277, -0.2286, -0.2293, -0.2300, ...
#         -0.2306, -0.2310, -0.2314, -0.2316, -0.2318, -0.2318, -0.2317, ...
#         -0.2316, -0.2313, -0.2309, -0.2304, -0.2298, -0.2291, -0.2284, ...
#         -0.2275, -0.2265, -0.2254, -0.2242, -0.2229, -0.2215, -0.2200, ...
#         -0.2184, -0.2167, -0.2149, -0.2131, -0.2111, -0.2091, -0.2069, ...
#         -0.2047, -0.2024, -0.2000, -0.1975, -0.1950, -0.1924, -0.1896, ...
#         -0.1869, -0.1840, -0.1811, -0.1781, -0.1750, -0.1719, -0.1687, ...
#         -0.1655, -0.1622, -0.1588, -0.1554, -0.1520, -0.1485, -0.1449, ...
#         -0.1413, -0.1377, -0.1340, -0.1302, -0.1265, -0.1227, -0.1189, ...
#         -0.1150, -0.1111, -0.1072, -0.1033, -0.0993, -0.0953, -0.0914, ...
#         -0.0873, -0.0833, -0.0793, -0.0752, -0.0712, -0.0671, -0.0631, ...
#         -0.0590, -0.0549, -0.0509, -0.0468, -0.0428, -0.0387, -0.0347, ...
#         -0.0306, -0.0266, -0.0226, -0.0186, -0.0146, -0.0106, -0.0067, ...
#         -0.0027,  0.0012,  0.0051,  0.0090,  0.0129,  0.0167,  0.0205, ...
#          0.0243,  0.0281,  0.0318,  0.0355,  0.0392,  0.0428,  0.0465, ...
#          0.0501,  0.0536,  0.0572,  0.0607,  0.0642,  0.0676,  0.0710, ...
#          0.0744,  0.0777,  0.0810,  0.0843,  0.0876,  0.0908,  0.0940, ...
#          0.0971,  0.1002,  0.1033,  0.1063,  0.1094,  0.1123,  0.1153, ...
#          0.1182,  0.1210,  0.1239,  0.1267,  0.1294,  0.1322,  0.1349, ...
#          0.1376,  0.1402,  0.1428,  0.1454,  0.1479,  0.1504,  0.1529, ...
#          0.1553,  0.1577,  0.1601,  0.1624,  0.1647,  0.1670,  0.1692, ...
#          0.1715,  0.1736,  0.1758,  0.1779,  0.1800,  0.1821,  0.1841, ...
#          0.1862,  0.1881,  0.1901,  0.1920,  0.1939,  0.1958,  0.1976, ...
#          0.1995,  0.2013,  0.2030,  0.2048,  0.2065,  0.2082,  0.2099, ...
#          0.2115,  0.2131,  0.2147,  0.2163,  0.2179,  0.2194,  0.2209, ...
#          0.2224,  0.2239,  0.2253]


 