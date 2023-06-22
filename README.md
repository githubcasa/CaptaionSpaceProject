# CaptaionSpaceProject
This program elaborate the images and define the basic data that we need to calculate the indices of the project.

Three conversion tables have been defined: 
-	fastiecm_IS.py
-	fastiecm _IFH.py
-	fastiecm _IF.py
we used these tables to colorize the images according to the NDVI ranges used in the indexes:
file name 	NDVI	IS_index	R	G	B
fastiecm_IS.py	<= 0,10	IS_Useless_surface	255	0	0
	> 0,10	IS_Usefull_surface	49	127	67
fastiecm_IF.py	<= 0,10	IF_No_value	0	0	0
	0,10 < ndvi <= 0,30	IF_No_forest	95	95	95
	> 0,30	IF_Ok_forest	49	127	67
fastiecm_IFH.py	<= 0,10	IFH_No_value	0	0	0
	0,10 < ndvi <= 0,30	IFH_No_forest	95	95	95
	0,30 < ndvi <= 0,59	IFH_Unhealthy_Plant	119	221	119
	> 0,59	IFH_Healthy_plant	0	66	37
 
