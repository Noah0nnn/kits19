from starter_code.utils import load_case
from starter_code.visualize import visualize


case_id = "case_00001"

volume, segmentation = load_case(case_id)
visualize(case_id, f"../output/{case_id}")









