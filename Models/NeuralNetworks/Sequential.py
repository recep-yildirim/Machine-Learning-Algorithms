from Models.NeuralNetworks.Layers import Layer

class Sequential(Layer):
    def __init__(self):
        self.layers = list()

        self.__loss = None
        self.__optimizer = None


    def add(self, layer):
        self.layers.append(layer)

    def build(self, loss, optimizer):
        self.__loss = loss
        self.__optimizer = optimizer

    def call(self, data, labels):
        self.initialize_layers(data.shape[1])
        self.inputs = data

        self.forward()
        loss = self.__loss(labels, self.outputs)


    def initialize_layers(self, shape):
        for layer in self.layers:
            layer.initialize_weights(shape)
            shape = layer.n_neurons

    def forward(self):
        data = self.inputs
        for layer in self.layers:
            layer.inputs = data
            layer.forward()
            data = layer.outputs

        self.outputs = data

    def backward(self, optimizer, delta):
        pass