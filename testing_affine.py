import nibabel as nib
import numpy as np

# 載入影像
image_path = 'data/case_00050/imaging.nii.gz'  # 替換成影像的實際路徑
image = nib.load(image_path)

# 取得 affine 矩陣
affine_matrix = image.affine
print("Affine Matrix:\n", affine_matrix)

header = image.header
print(header)

# 查看資料型別
print("Data type:", header.get_data_dtype())

# 查看體素間距
print("Voxel Spacing (zooms):", header.get_zooms())

# 查看影像維度信息
print("Dimensions:", header['dim'])

seg_data = image.get_fdata()
# print("fdata:", image.get_fdata())
tumor_voxels = np.where(seg_data == 2)
print("t:", tumor_voxels)