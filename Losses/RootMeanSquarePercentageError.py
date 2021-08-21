import numpy as np

from Losses import Loss

class RootMeanSquarePercentageError(Loss):
    def call(self, true_labels, predicted_labels):
        error = np.abs(predicted_labels - true_labels)
        result = 100 * np.mean(np.square(error / np.abs(true_labels)))

        return np.sqrt(result)

    def __call__(self, true_labels, predicted_labels):
        return self.call(true_labels, predicted_labels)