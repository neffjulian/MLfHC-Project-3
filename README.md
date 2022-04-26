
# ML4H course project

This is the course project for Machine Learning for Health Care

## Installation

Create the conda environment for the project. A version of conda must be installed on your system.

```bash
  conda env create -f environment.yml
  conda activate ml4h
```

## Dataset

Download the dataset from [Pubmed RCT](https://github.com/Franck-Dernoncourt/pubmed-rct) and extract it to the `data` folder. The folder should have the following structure:

    .
    ├── ...
    ├── data                    
    │   ├── PubMed_20k_RCT
            ├── dev.txt
            ├── test.txt
            ├── train.txt
    │   ├── PubMed_20k_RCT_numbers_replaced_with_at_sign
            ├── ...
    │   ├── PubMed_200k_RCT
            ├── dev.txt
            ├── test.txt
            ├── train.7z
    │   ├── PubMed_200k_RCT_numbers_replaced_with_at_sign
            ├── ...
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
