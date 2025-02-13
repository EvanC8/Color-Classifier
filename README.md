# Color Classifier
This color classifier labels RGB color values by making use of the [K-Nearest Neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) supervised machine learning algorithm.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#how-it-works">How it works</a>
      <ul>
        <li><a href="#training">Training</a></li>
        <li><a href="#predictions">Predictions</a></li>
      </ul>
    </li>
    <li><a href="#next-steps">Next Steps</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

# Installation
* Clone the repo
   ```sh
   git clone https://github.com/EvanC8/Color-Classifier.git
   ```
# Usage
1. Download project
2. Create a KNN(k) object, where k represents the number of neighbors for the prediction algorithm to use.
3. Run the class's prediction(red, green, blue) method. RGB values range from 0-255

# How it works

### Training
`K-Nearest Neighbors` is a supervised machine learning algorithm. Thus, the model is trained by passing in a large dataset of RGB color values, each labeled with a corresponding color. The red, green, and blue values are the <i>features</i> for the model. The <i>targets</i> for the model are the possible labels for each color which include brown, pink, red, orange, yellow, green, blue, purple, white, gray, and black. Each training example's RGB values represent a point in 3D color space, which is utilized for making predictions.

### Preditions
When a RGB color is passed into the model for a prediction, the model locates the RGB value in 3D color space. Then, it calculates the k (specified at model instantiation) RGB values from the database that are closest to this point using Euclidean distance. Each of these k colors are given a weight based on their proximity to the unseen data point. Using a weighted voting system across all k colors, the most voted for label is assigned as the prediction for the unseen data point.


# Next Steps
* Train the model on a large and more comprehensive dataset to increase accuracy.
* Allow for a wider range of color labels to support more detailed and precise classifications. 
* Explore other models including neural networks and decision trees.

# License
Destributed under the MIT License. See `LICENSE.txt` for more information.
