# numpy dtype for LGAL_GAL_STRUCT
import numpy as np
struct_dtype = np.dtype([
('Type',np.int32,1),								
('HaloIndex',np.int32,1),
('SnapNum',np.int32,1),
('LookBackTimeToSnap',np.float32,1),
('CentralMvir',np.float32,1),
('CentralRvir',np.float32,1),
('DistanceToCentralGal',np.float32,3),
('Pos',np.float32,3),
('Vel',np.float32,3),
('Len',np.int32,1),
('Mvir',np.float32,1),
('Rvir',np.float32,1),
('Vvir',np.float32,1),
('Vmax',np.float32,1),
('GasSpin',np.float32,3),
('StellarSpin',np.float32,3),
('InfallVmax',np.float32,1),
('InfallVmaxPeak',np.float32,1),
('InfallSnap',np.int32,1),
('InfallHotGas',np.float32,1),
('HotRadius',np.float32,1),
('OriMergTime',np.float32,1),
('MergTime',np.float32,1),
('ColdGas',np.float32,1),
('StellarMass',np.float32,1),
('BulgeMass',np.float32,1),
('DiskMass',np.float32,1),
('HotGas',np.float32,1),
('EjectedMass',np.float32,1),
('BlackHoleMass',np.float32,1),
('ICM',np.float32,1),
('MetalsColdGas',np.float32,3),
('MetalsBulgeMass',np.float32,3),
('MetalsDiskMass',np.float32,3),
('MetalsHotGas',np.float32,3),
('MetalsEjectedMass',np.float32,3),
('MetalsICM',np.float32,3),
('PrimordialAccretionRate',np.float32,1),
('CoolingRadius',np.float32,1),
('CoolingRate',np.float32,1),
('CoolingRate_beforeAGN',np.float32,1),
('QuasarAccretionRate',np.float32,1),
('RadioAccretionRate',np.float32,1),
('Sfr',np.float32,1),
('SfrBulge',np.float32,1),
('XrayLum',np.float32,1),
('BulgeSize',np.float32,1),
('StellarDiskRadius',np.float32,1),
('GasDiskRadius',np.float32,1),
('CosInclination',np.float32,1),
('DisruptOn',np.int32,1),
('MergeOn',np.int32,1),
('MagDust',np.float32,40),
('Mag',np.float32,40),
('MagBulge',np.float32,40),
('MassWeightAge',np.float32,1),
('rbandWeightAge',np.float32,1),
('sfh_ibin',np.int32,1),
('sfh_numbins',np.int32,1),
('sfh_DiskMass',np.float32,20),
('sfh_BulgeMass',np.float32,20),
('sfh_ICM',np.float32,20),
('sfh_metalsDiskMass',np.float32,[20,3]),
('sfh_metalsBulgeMass',np.float32,[20,3]),
('sfh_metalsICM',np.float32,[20,3]),
('sfh_elementsDiskMass',np.float32,[20,11]),
('sfh_elementsBulgeMass',np.float32,[20,11]),
('sfh_elementsICM',np.float32,[20,11]),
('DiskMass_elements',np.float32,11),
('BulgeMass_elements',np.float32,11),
('ColdGas_elements',np.float32,11),
('HotGas_elements',np.float32,11),
('ICM_elements',np.float32,11),
('EjectedMass_elements',np.float32,11)
])

properties_used = {}
for ii in struct_dtype.names:
	properties_used[ii] = False
