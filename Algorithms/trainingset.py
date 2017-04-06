class TrainingSet:
    def __init__(self, dataset, attributes_position_array, label_position):
        self.dataset = dataset
        self.attribute_list = list(dataset[:,attributes_position_array])
        self.label_list = list(dataset[:,label_position])