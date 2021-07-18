import numpy as np

from Losses import Loss

class MeanRelativeAbsoluteError(Loss):
    def call(self, true_labels, predicted_labels):
        return np.mean(np.abs(true_labels - predicted_labels) / np.abs(true_labels - np.mean(true_labels)))

    def __call__(self, true_labels, predicted_labels):
        return self.call(true_labels, predicted_labels)