import numpy as np

from Losses import Loss

class MeanAbsoluteRelativeError(Loss):
    def call(self, true_labels, predicted_labels):
        return np.mean(np.abs(true_labels - predicted_labels) / np.abs(true_labels))

    def __call__(self, true_labels, predicted_labels):
        return self.call(true_labels, predicted_labels)