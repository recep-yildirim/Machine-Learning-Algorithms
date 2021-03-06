import numpy as np

from Optimizers import Optimizer

class AdaGrad(Optimizer):
    def __init__(self, learning_rate=0.1, decrease_learning_rate=True, epsilon=1e-7):
        self.__learning_rate = learning_rate
        self.__decrease_learning_rate = decrease_learning_rate
        self.__epsilon = epsilon
        self.__cumulative_sum = 0

    @property
    def learning_rate(self):
        return self.__learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        self.__learning_rate = value

    @property
    def decrease_learning_rate(self):
        return self.__decrease_learning_rate

    @decrease_learning_rate.setter
    def decrease_learning_rate(self, value):
        self.__decrease_learning_rate = value

    @property
    def epsilon(self):
        return self.__epsilon

    @epsilon.setter
    def epsilon(self, value):
        self.__epsilon = value

    def __learning_schedule(self, t):
        return 1 / t

    def __update_cumulative_sum(self, gradients):
        self.__cumulative_sum += np.power(gradients, 2)

    def call(self, gradients, **kwargs):
        self.__update_cumulative_sum(gradients)

        new_parameters = (self.__learning_rate / np.sqrt(self.__cumulative_sum + self.__epsilon)) * gradients

        if self.__decrease_learning_rate:
            self.__learning_rate = self.__learning_schedule((1 / (self.__learning_rate + 1)) * gradients.shape[0])

        return new_parameters

    def __call__(self, gradients, **kwargs):
        return self.call(gradients, **kwargs)
