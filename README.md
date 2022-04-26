
# ML4H course project

This is the course project for Machine Learning for Health Care

## Setup

Create the conda environment for the project. A version of conda must be installed on your system.

```bash
  conda env create -f environment.yml
  conda activate ml4h
```

## Dataset

This dataset contains a mix of samples from the Kaggle datasets Brain MRI Images for Brain Tumor Detection and Brain Tumor Classification (MRI) datasets. The folder should have the following structure:

    .
    ├── ...
    ├── data                    
    │   ├── images
            ├── no
            ├── yes
    │   ├── radiomics
            ├── test_data.csv
            ├── test_labels.npy
            ├── train_data.csv
            ├── train_labels.npy
            ├── validation_data.csv
            ├── validation_labels.npy
    └── ...

## Experiments

Each experiment has its own config file in the configs folder. An experiment can be run through

```bash
  python main.py --config configs/base/mitbih_baseline_cnn.yaml
```

## Authors

- [@Julian Neff](https://github.com/neffjulian)
- [@Michael Mazourik](https://github.com/MikeDoes)
- [@Remo Kellenberger](https://github.com/remo48)

## Appendix

Overleaf: https://www.overleaf.com/project/62553c11e7264873d4f2dd60
