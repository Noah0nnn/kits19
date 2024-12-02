import nibabel as nib
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

# 假設你有一個 cases 的路徑列表
tumor_volumes = []
data_path = "data/"
case_count = 210


for i in range(case_count):
    case_id = f"case_{i:05d}"
    case_path = os.path.join(data_path, case_id, "segmentation.nii.gz")  # 假設影像檔名為 imaging.nii.gz
    
    segmentation = nib.load(case_path)

    spacing = segmentation.header.get_zooms()  # 從metadata獲取voxel spacing

    if not os.path.exists(case_path):
        continue

    # 讀取影像和獲取資料
    seg_img = nib.load(case_path)
    seg_data = seg_img.get_fdata()

    # 計算腫瘤體素數量 (標籤2)
    tumor_voxels = np.sum(seg_data == 2)

    # 將體素數量轉換為實際體積
    tumor_volume = tumor_voxels * spacing[0] * spacing[1] * spacing[2]
    tumor_volumes.append(tumor_volume)


# 將腫瘤大小資料放入 DataFrame
tumor_df = pd.DataFrame(tumor_volumes, columns=['Tumor Volume (mm^3)'])

tumor_df['Tumor Volume (cm^3)'] = tumor_df['Tumor Volume (mm^3)'] / 1000

# 畫直方圖
plt.hist(tumor_df['Tumor Volume (cm^3)'], bins=20, edgecolor='black')
plt.title("Tumor Volume Distribution Across Cases")
plt.xlabel("Tumor Volume (cm³)")
plt.ylabel("Number of Cases")
plt.show()

# 基本統計資訊
print(tumor_df)

print(tumor_df.describe())