import pandas as pd
import math

class KNN:
    def __init__(self, k):
        # Set number of nearest neighbors to weigh
        self.k = k

        # 11 labels and dictionary for colors matching label
        self.labels = ["brown", "pink", "red", "orange", "yellow", "green", "blue", "purple", "white", "gray", "black"]
        self.color_dict = {label: [] for label in self.labels}

        # Read training data
        df = pd.read_csv("colors.csv")
        list_of_rows = df.values.tolist()

        for row in list_of_rows:
            for label in self.labels:
                if label in row[0]:
                    self.color_dict[label].append((int(row[3]) / 255, int(row[4] / 255), int(row[5] / 255)))
                    break

        # Print number of colors per label in training data
        for label in self.color_dict:
            print(str(label) + ": " + str(len(self.color_dict[label])))

    # Predicts the label of a given color
    def prediction(self, r, g, b):
        # Normalize rgb value
        rgb = (r / 255, g / 255, b / 255)
        # Get the k nearest neighbors
        nearest_neighbors = self.nearest_k(rgb)

        # Stores the cumulative weight of each label across the nearest neighbors
        label_weights = {}

        # Sum up the weights for each label in nearest neighbors
        for n in nearest_neighbors:
            if n.label in label_weights:
                label_weights[n.label] += n.weight
            else:
                label_weights[n.label] = n.weight

        # Print the k nearest neighbors
        for n in nearest_neighbors:
            print(n)

        # Print the weights of each label
        print("Weights: " + str(label_weights))

        # Return the label with the greatest weight
        prediction = max(label_weights, key=label_weights.get)
        return prediction

    # Returns the nearest k neighboring colors to the given color
    def nearest_k(self, rgb):
        # Stores a list of all neighboring colors sorted by distance from given color
        sorted_n = []

        for key in self.color_dict:
            for color in self.color_dict[key]:
                # Calculate distance
                dist = math.dist(rgb, color)
                # Create neighbor to store in list
                n = Neighbor(key, color, dist)

                # Insert into list ordered by smallest distance
                if len(sorted_n) == 0:
                    sorted_n.append(n)
                else:
                    index = self.binary_insertion(sorted_n, dist)
                    sorted_n.insert(index, n)

        # Return the nearest k neighbors
        return sorted_n[:self.k]

    # Returns the index to insert into the neighbors list ordered by distance
    def binary_insertion(self, sorted_n, d):
        low = 0
        high = len(sorted_n) - 1

        while low <= high:
            mid = (low + high) // 2

            if d < sorted_n[mid].d:
                high = mid - 1
            elif d > sorted_n[mid].d:
                low = mid + 1
            else:
                return mid

        return low


# Stores information on each neighboring color in the training set
class Neighbor:
    def __init__(self, label, rgb, d):
        self.label = label
        self.rgb = rgb
        self.d = d

        if d == 0.0:
            self.weight = 1000
        else:
            self.weight = 1/d

    def __repr__(self):
        return f"{self.label}: {self.rgb_formatted()} d={round(self.d, 5)} w={round(self.weight, 5)}"

    def rgb_formatted(self):
        r = int(self.rgb[0] * 255)
        g = int(self.rgb[1] * 255)
        b = int(self.rgb[2] * 255)
        return r, g, b

# Test classifier using 5 nearest neighbors
knn = KNN(k=5)

print("Prediction: " + knn.prediction(245, 66, 179)) # Test on a rgb color (pink)
print("Prediction: " + knn.prediction(7, 137, 224)) # Test on a rgb color (blue)
print("Prediction: " + knn.prediction(176, 69, 88)) # Test on a rgb color (blue)