from importlib import import_module
import os

def get_parent_dir(n=0):
    current_path = os.path.dirname(os.path.abspath(__file__))

    for _ in range(n):
        current_path = os.path.dirname(current_path)

    return current_path

def get_loss(name):
    module = import_module(name)
    loss = getattr(module, name)

    return loss()   # creates an instances of the class

os.sys.path.append(get_parent_dir())

from Loss import Loss
from MeanSquaredError import MeanSquaredError as MSE
from MeanAbsoluteError import MeanAbsoluteError as MAE
from MeanAbsolutePercentageError import MeanAbsolutePercentageError as MAPE
from CosineSimilarity import CosineSimilarity
from HuberLoss import HuberLoss
from LogCosh import LogCosh
from RootMeanSquaredError import RootMeanSquaredError as RMSE
from Quantile import Quantile
from MeanError import MeanError
from MeanPercentageError import MeanPercentageError as MPE
from SymmetricMeanAbsolutePercentageError import SymmetricMeanAbsolutePercentageError as SMAPE
from MeanNormalizedBias import MeanNormalizedBias as MNB
from MedianAbsoluteError import MedianAbsoluteError as MdAE
from MaximumAbsoluteError import MaximumAbsoluteError as MaxAE
from MeanAbsoluteRelativeError import MeanAbsoluteRelativeError as MARE
from MedianAbsolutePercentageError import MedianAbsolutePercentageError as MdAPE
from RelativeAbsoluteError import RelativeAbsoluteError as RAE
from MeanRelativeAbsoluteError import MeanRelativeAbsoluteError as MRAE
from GeometricMeanAbsoluteError import GeometricMeanAbsoluteError as GMAE
from SumOfAbsoluteDifference import SumOfAbsoluteDifference as SAD
from GeometricMeanRelativeAbsoluteError import GeometricMeanRelativeAbsoluteError as GMRAE
from MedianRelativeAbsoluteError import MedianRelativeAbsoluteError as MdRAE
from SymmetricMedianAbsolutePercentageError import SymmetricMedianAbsolutePercentageError as sMdAPE
from SumOfSquaredError import SumOfSquaredError as SSE
from RelativeSquaredError import RelativeSquaredError as RSE
from RootRelativeSquaredError import RootRelativeSquaredError as RRSE
from GeometricRootMeanSquaredError import GeometricRootMeanSquaredError as GRMSE
from MeanSquarePercentageError import MeanSquarePercentageError as MSPE
from MedianSquarePercentageError import MedianSquarePercentageError as MdSPE
from RootMeanSquarePercentageError import RootMeanSquarePercentageError as RMSPE
from RootMedianSquarePercentageError import RootMedianSquarePercentageError as RMdSPE