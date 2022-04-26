import torch
import numpy as np
import pandas as pd

from pytorch_lightning import LightningDataModule
from torch.utils.data import Dataset, DataLoader


class PubMedDataset(Dataset):
    """TODO implement dataset
    """
    def __init__(self):
        pass

    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass 


class PubMedDataModule(LightningDataModule):
    """TODO implement datamodule
    """
    def __init__(self, batch_size=32, train_split=0.8, num_workers=4):
        super().__init__()
        self.batch_size = batch_size
        self.train_split = train_split
        self.num_workers = num_workers
        self.train_set = None
        self.val_set = None
        self.test_set = None

    def setup(self, stage=None):
        pass

    def train_dataloader(self):
        return DataLoader(self.train_set, batch_size=self.batch_size, num_workers=self.num_workers)

    def val_dataloader(self):
        return DataLoader(self.val_set, batch_size=self.batch_size, num_workers=self.num_workers)

    def test_dataloader(self):
        return DataLoader(self.test_set, batch_size=self.batch_size, num_workers=self.num_workers)
