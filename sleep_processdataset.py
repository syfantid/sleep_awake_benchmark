"""
    File to pre-process the raw actigraphy data into format that can be used by machine learning and formula based methods for
    distinguishing sleep from awake
"""
import os.path
import sys
from sleep_misc import load_dataset

if len(sys.argv) <= 1:
    print("Usage: %s <TASK_ID>" % (sys.argv[0]))
    sys.exit(0)

TASK = int(sys.argv[1])

print("Generating dataset for Task %d" % (TASK))
OUTPUTFILE="hdf_task%d" % (TASK)

if TASK in [1, 2]:
    # PATH_TO_FILES = "datasets"
    PATH_TO_FILES = os.path.join("datasets", "task{}".format(TASK))
    # if not os.path.exists(PATH_TO_FILES):
    #     os.makedirs(PATH_TO_FILES)
else:
    PATH_TO_FILES = "./data/mesa/actigraphy_test/"

method = "stage" if TASK != 3 else "interval"

print("...Loading dataset into memory...")
dftrain, dftest, featnames = load_dataset(PATH_TO_FILES, useCache=False, saveCache=True, cacheName=OUTPUTFILE, ground_truth=method)
print("...Done...")


dfoutname = "dftrain_task%d.csv" % (TASK)
print("...Saving Task %d dataset to disk. Filename: %s ..." % (TASK, dfoutname))
dftrain[["mesaid", "linetime", "marker", "interval", "binterval", "activity", "gt", "gt_sleep_block", "wake"]].to_csv(dfoutname, index=False)

dfoutname = "dftest_task%d.csv" % (TASK)
print("...Saving Task %d dataset to disk. Filename: %s ..." % (TASK, dfoutname))
dftest[["mesaid", "linetime", "marker", "interval", "binterval", "activity", "gt", "gt_sleep_block", "wake"]].to_csv(dfoutname, index=False)
print("...Done...")

