class TrainingSet:
    def __init__(self, dataset, attributes_position_array, label_position):
        self.dataset = dataset
        self.attributes = list(dataset[:,attributes_position_array])
        self.labels = list(dataset[:,label_position])

