# Transfer Learning Library for Fault Diagnosis

## Overview
Welcome to our repository dedicated to advancing cross-domain fault diagnosis through transfer learning. Our focus lies in **single-source unsupervised domain adaptation**, **multi-source unsupervised domain adaptation** and **domain gneralization**. Our library offers a rich suite of resources and methods, supporting **closed-set**, **open-set**, **partial**, and **universal** domain adaptation scenarios.

## Updates
### 2024.07.25
We are excited to release version 2.0.0 of the TL-Fault-Diagnosis-Library. Key updates include:
- The library now supports not only closed-set but also open-set, partial, and universal domain adaptation scenarios. All models are reorganized for training across these scenarios. When models originally designed for closed-set are used in open-set or universal scenarios, the Closed-set-acc (which excludes categories present in the target domain but absent in the source domain) will also be reported.
- [Selective Transfer](#selective-transfer) method is integrated to enable the selection of specific faults within a dataset for transfer.
- The library now includes popular methods such as IWAN and AFN for partial domain adaptation, and UDA for universal domain adaptation.
- ResNet is now available as a backbone architecture option, specifically a 1D ResNet adapted from [this repository](https://github.com/Xiaohan-Chen/transfer-learning-fault-diagnosis-pytorch).
- Releases have been created for this repository, with dataset examples integrated within the Releases section instead of the [Dataset-TL-BFD repo](https://github.com/Feaxure-fresh/Dataset-TL-BFD). The original version of our code (v1.0.0) remains accessible for reference.

Please note: Due to extensive updates in version 2.0.0, models from this version cannot be used to train in the original version of the code.

## Featured Models
### Domain Adaptation
- **ACDANN** - Integrating expert knowledge with domain adaptation for unsupervised fault diagnosis. [Published in TIM 2021](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9612159) | [View Code](/models/ACDANN.py)
- **ADACL** - Adversarial domain adaptation with classifier alignment for cross-domain intelligent fault diagnosis of multiple source domains. [Published in Measurement Science and Technology 2020](https://iopscience.iop.org/article/10.1088/1361-6501/abcad4/pdf) | [View Code](/models/ADACL.py)
- **BSP** - Transferability vs. discriminability: Batch spectral penalization for adversarial domain adaptation. [Published in ICML 2019](http://proceedings.mlr.press/v97/chen19i/chen19i.pdf) | [View Code](/models/BSP.py) 
- **CDAN** - Conditional adversarial domain adaptation. [Published in NIPS 2018](http://papers.nips.cc/paper/7436-conditional-adversarial-domain-adaptation) | [View Code](/models/CDAN.py) 
- **CORAL** - Deep coral: Correlation alignment for deep domain adaptation. [Published in ECCV 2016](https://arxiv.org/abs/1607.01719) | [View Code](/models/CORAL.py)
- **DAN** - Learning transferable features with deep adaptation networks. [Published in ICML 2015](http://ise.thss.tsinghua.edu.cn/~mlong/doc/deep-adaptation-networks-icml15.pdf) | [View Code](/models/DAN.py)
- **DANN** - Unsupervised domain adaptation by backpropagation. [Published in ICML 2015](http://proceedings.mlr.press/v37/ganin15.pdf) | [View Code](/models/DANN.py)
- **MCD** - Maximum classifier discrepancy for unsupervised domain adaptation. [Published in CVPR 2018](http://openaccess.thecvf.com/content_cvpr_2018/papers/Saito_Maximum_Classifier_Discrepancy_CVPR_2018_paper.pdf) | [View Code](/models/MCD.py)
- **MDD** - Bridging theory and algorithm for domain adaptation. [Published in ICML 2019](http://proceedings.mlr.press/v97/zhang19i/zhang19i.pdf) | [View Code](/models/MDD.py)
- **MFSAN** - Aligning domain-specific distribution and classifier for cross-domain classification from multiple sources. [Published in AAAI 2019](https://ojs.aaai.org/index.php/AAAI/article/view/4551) | [View Code](/models/MFSAN.py) 
- **MSSA** - A multi-source information transfer learning method with subdomain adaptation for cross-domain fault diagnosis. [Published in Knowledge-Based Systems 2022](https://reader.elsevier.com/reader/sd/pii/S0950705122001927?token=03BD384CA5D6E0E7E029B23C739C629913DE8F8BB37F6331F7D233FB6C57599BFFC86609EE63BE2F9FC43871D96A2F61&originRegion=us-east-1&originCreation=20230324021230) | [View Code](/models/MSSA.py)

### Domain Generalization
- **IRM** - Invariant risk minimization. [Published in ArXiv 2019](https://arxiv.org/abs/1907.02893) | [View Code](/models/IRM.py)
- **MixStyle** - Domain generalization with mixstyle. [Published in ICLR 2021](https://arxiv.org/abs/2104.02008) | [View Code](/models/MixStyle.py)
- **IBN** - Two at once: Enhancing learning and generalization capacities via IBN-Net. [Published in ECCV 2018](https://openaccess.thecvf.com/content_ECCV_2018/papers/Xingang_Pan_Two_at_Once_ECCV_2018_paper.pdf) | [View Code](/models/IBN.py)
- **MLDG** - Learning to generalize: Meta-learning for domain generalization. [Published in AAAI 2018](https://ojs.aaai.org/index.php/AAAI/article/view/11596) | [View Code](/models/MLDG.py)
- **GroupDRO** - Distributionally robust neural networks for group shifts: On the importance of regularization for worst-case generalization. [Published in ICLR 2020](https://arxiv.org/pdf/1911.08731.pdf) | [View Code](/models/DRO.py)
- **VREx** - Out-of-distribution generalization via risk extrapolation. [Published in ICML 2021](https://proceedings.mlr.press/v139/krueger21a/krueger21a.pdf) | [View Code](/models/VREx.py)

### Partial Domain Adaptation
- **IWAN** - Importance weighted adversarial nets for partial domain adaptation. [Published in CVPR 2018](https://openaccess.thecvf.com/content_cvpr_2018/papers/Zhang_Importance_Weighted_Adversarial_CVPR_2018_paper.pdf) | [View Code](/models/IWAN.py)
- **AFN** - Larger norm more transferable: An adaptive feature norm approach for unsupervised domain adaptation. [Published in ICCV 2019](https://openaccess.thecvf.com/content_ICCV_2019/papers/Xu_Larger_Norm_More_Transferable_An_Adaptive_Feature_Norm_Approach_for_ICCV_2019_paper.pdf) | [View Code](/models/AFN.py)

### Universal Domain Adaptation
- **UDA** - Universal domain adaptation. [Published in CVPR 2019](https://openaccess.thecvf.com/content_CVPR_2019/papers/You_Universal_Domain_Adaptation_CVPR_2019_paper.pdf) | [View Code](/models/UDA.py)

## Getting Started
### Requirements
Our code runs fine with the following prerequisites:
*  Python 3 (>=3.8)
*  Pytorch (>=1.10)
*  Numpy (>=1.21.2)
*  Pandas (>=1.5.3)
*  tqdm (>=4.46.1)
*  Scipy (>=1.10)

### Repository Access
#### Direct Download
1. Click on the 'Code' button and select 'Download ZIP'.
2. Extract the ZIP file to your desired location.
#### Download Latest Release
1. Navigate to the 'Releases' section of the GitHub repository.
2. Click on the latest release named `TL-Fault-Diagnosis-Library.v*.*.*.zip`.
3. Extract the ZIP file to your desired location.
#### Using Git Clone
1. Open your command line interface.
2. Navigate to the directory where you wish to clone the repository.
3. Run the command:
```shell
git clone https://github.com/Feaxure-fresh/TL-Bearing-Fault-Diagnosis.git
```

## Accessing Datasets
### Supported datasets
Our repository supports several public datasets for fault diagnosis, with accompanying loading code. These include:
- **[CWRU](https://engineering.case.edu/bearingdatacenter)** - Case Western Reserve University dataset.
- **[MFPT](https://www.mfpt.org/fault-data-sets)** - Machinery Failure Prevention Technology dataset.
- **[PU](https://groups.uni-paderborn.de/kat/BearingDataCenter/)** - Paderborn University dataset.
- **[XJTU](https://biaowang.tech/xjtu-sy-bearing-datasets)** - Xi’an Jiaotong University dataset.
- **[IMS](https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset?resource=download)** - Intelligent Maintenance Systems dataset.
- **[JNU](https://github.com/ClarkGableWang/JNU-Bearing-Dataset)** - Jiangnan University dataset.

### Setting Up Dataset Directory
- Create a folder named "datasets" in the root directory of the cloned repository.
- Download the desired datasets and place them into this "datasets" folder, follow the steps below:

#### Within-dataset Transfer
For analyzing a specific dataset under different working conditions:
1. Divide the dataset into separate folders named "condition_0", "condition_1", etc., each representing a unique operational condition.
2. Within each "condition_?" folder, create subfolders (with custom names) for different fault categories containing the respective fault data.
3. Ensure each 'condition_?' folder contains subfolders with identical names and numbers (indicating the same classes of faults).

For example, for the CWRU dataset:
   - Organize the dataset into folders based on motor speed (four speeds as four folders).
   - Within each condition folder, categorize data into 9 subfolders for 9 fault classes, such as '7 mil Inner Race fault', '14 mil Inner Race fault', '7 mil Outer Race fault', etc., as detailed in Table XII of [this IEEE article](https://ieeexplore.ieee.org/abstract/document/9399341).

Example folder structure for CWRU dataset:
```
.
└── datasets
    └── CWRU
        ├── condition_0
        │   ├── ball_07
        │   │   └── 122.mat
        │   ├── inner_07
        │   │   └── 109.mat
        │   ...
        ├── condition_1
        │   ├── ball_07
        │   │   └── 123.mat
        │   ...
        ├── condition_2
        ...
```

#### Cross-dataset Transfer
For implementing transfer between different datasets:
1. Organize the dataset into multiple folders according to fault categories across at least two datasets.
2. Maintain consistency in folder names and numbers across all datasets.

For instance, when organizing CWRU and MFPT datasets for one-to-one transfer:
```
.
└── datasets
    ├── CWRU
    │   ├── inner
    |   |    ├── ***.mat
    |   |    |   ***.mat
    |   |    ...
    │   ├── normal
    │   └── outer
    └── MFPT
        ├── inner
        ├── normal
        └── outer
```
🌟 Still confused about the dataset setup? Please refer to the sample datasets in the 'Releases' named `Dataset-TL-FD-Library.zip`.
### Custom Dataset Integration
For incorporating other public datasets or your custom datasets, navigate to `data_loader/load_methods.py` in the repository. Implement your data loading function following this template:
```python
def your_dataset_name(item_path):
    # Your code to extract the signal or data from the file
    signal = take_out_data_from_file(item_path)
    return signal
```
This process allows for the seamless integration within our framework.

## Training Procedures
### Within-dataset Transfer
Train models using data from the same dataset but different operational conditions.

##### One-to-One Transfer
Example: Transfer from CWRU operation condition 0 to condition 1.
```shell
python train.py --model_name DAN --source CWRU_0 --target CWRU_1 --train_mode single_source --cuda_device 0
```

##### Many-to-One Transfer
Example: Transfer from CWRU operation condition 0 and condition 1 to condition 2.
```shell
python train.py --model_name MFSAN --source CWRU_0,CWRU_1 --target CWRU_2 --train_mode multi_source --cuda_device 0 
```

### Cross-dataset Transfer
Train models using data from different datasets.

##### One-to-One Transfer
Example: Transfer from CWRU to MFPT dataset.
```shell
python train.py --model_name DAN --source CWRU --target MFPT --train_mode single_source --cuda_device 0
```

##### Many-to-One Transfer
Example: Transfer from CWRU and PU datasets to MFPT dataset.
```shell
python train.py --model_name MFSAN --source CWRU,PU --target MFPT --train_mode multi_source --cuda_device 0
```

### Selective Transfer
Select specific fault categories within the dataset to create a sub-dataset for transfer. Use the format "dataset-numbers" to select fault categories, where 'numbers' refers to specific faults.

For example, consider the sample datasets in the 'Releases' named `Dataset-TL-FD-Library`: Transfer from CWRU (inner, normal, and outer faults) to MFPT (inner and normal faults) dataset.
```shell
python train.py --model_name DAN --source CWRU --target MFPT-01 --train_mode single_source --cuda_device 0
```
In this partial domain adaptation scenario, only the fault types 'inner' and 'normal' are selected from the MFPT dataset for transfer. Thus, `--target` is set as `MFPT-01`, where '0' and '1' denote the first and second fault types (as sorted in filenames) in the MFPT dataset, respectively. This functionality is especially useful for creating category gaps in various transfer scenarios without the need to reorganize dataset files.

With the following command:
```shell
python train.py --model_name UDA --source CWRU_0-01,CWRU_1-01 --target CWRU_1-12 --train_mode source_combine --cuda_device 0
```
It creates a multi-source universal domain adaptation scenario, transferring 'ball_07' and 'ball_14' from conditions 0 and 1 to 'ball_14' and 'ball_21' in condition 1.

### Load trained weights
Load and utilize weights from previously trained models.

Example: Load weights and test on CWRU operation condition 3.
```shell
python train.py --model_name MFSAN --load_path ./ckpt/MFSAN/multi_source/**.pth --source CWRU_0,CWRU_1 --target CWRU_3 --cuda_device 0
```
NOTE: The `--source` flag is not necessary for some models when loading weights for testing. However, for certain models, the number of sources is required to define the model structure, and the specific sources used are not important in this context.

🛠️ For more experimental settings, please modify the arguments in `opt.py`.
## Contact
We welcome feedback, inquiries, and suggestions to improve our work. If you encounter any issues with our code or have recommendations, please don't hesitate to reach out. You can contact Jinyuan Zhang via email at feaxure@outlook.com, or alternatively, feel free to post your queries or suggestions in the [Issues](https://github.com/Feaxure-fresh/TL-Bearing-Fault-Diagnosis/issues) section of our GitHub repository.

## Citation
Your support in citing our project when used in your research is highly appreciated. It helps in the recognition and dissemination of our work. Please use the following citation format:
```latex
@misc{TL-Fault-Diagnosis-Library,
    author = {Jinyuan Zhang},
    title = {TL-Fault-Diagnosis-Library},
    year = {2022},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/Feaxure-fresh/TL-Fault-Diagnosis-Library}}
}
```

