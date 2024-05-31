# seed based community detection

## How to use

example code
```
python detection.py --network ./dataset/TC1-6 --mode normal
python detection.py --network ./dataset/real/dolphin --mode normal
python general_evaluation.py --measure nmi --ground ./data/ground_truth/1-6.cmty --detected ./data/louvain/1-6.cmty
python general_evaluation.py --measure f1 --ground ./groundtruth/dolphin/dolphin.cmty --detected ./output/dolphin/dolphin.cmty --algorithm ours&
```
dataset should be placed in ./dataset/{datasetname} and change network file name to network.txt.

groundtruth file should be placed in ./data/ground_truth/{datasetname}.cmty

output file will be saved in ./data/{datasetname}.cmty
