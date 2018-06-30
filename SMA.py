# SMA formula
import pandas as pd
import numpy as np

sma=trades['price'].rolling(5).mean()
print(sma)
