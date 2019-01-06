# Tensor Decomposition in Python

This repository gives a quick tutorial on implementing Canonical Polyadic tensor decomposition in Python, including a brief introduction to Tensor decomposition. However, the main purpose of this notebook is to focus on the implementation of tensor decomposition in Python. In line with these objectives, we will implement tensor decomposition using two libraries available in Python ([TensorLy](http://tensorly.org/stable/index.html) and [tensortools](https://tensortools-docs.readthedocs.io/en/latest/)) and a simple implementation of Tensor Decomposition with Numpy (via alternating optimization). Furthermore, the result of these three approaches are compared in terms of reconstruction error and execution time.

## Content
1. **Tensor Decomposition**
2. **Implementation**
    - TensorLy
    - tensortools
    - Numpy
3. **Results and Comparison**

---

### Tensor Decomposition
<p align="center">
	<img src="https://raw.githubusercontent.com/mbashiri/tensor-decomposition-with-python/master/figures/tensor-decomposition.png?token=AjfLQ2lPERLx7C6yn-IrWgBbVDCIMkNrks5cO1QEwA%3D%3D" alt="Fig1" width="700">
</p>

### Example Scenario (with a neuroscientific theme)

<p align="center">
	<img src="https://raw.githubusercontent.com/mbashiri/tensor-decomposition-with-python/master/figures/model.png?token=AjfLQx_zjcxGUTBEKsPdRnBva2PN87f9ks5cO1QVwA%3D%3D" alt="Fig1" width="380">
    <img src="https://raw.githubusercontent.com/mbashiri/tensor-decomposition-with-python/master/figures/neuron-time.png?token=AjfLQ4sdjOLJBGsAn8LOWNyvBZCp4MUMks5cO1QiwA%3D%3D" alt="Fig1" width="500">
</p>

### Example Results and Comparison
<p align="center">
	<img src="https://raw.githubusercontent.com/mbashiri/tensor-decomposition-with-python/master/figures/groundtruth-estimate.png?token=AjfLQ1gNQenFYExiYZoHUCXXhregCj1Kks5cO1RxwA%3D%3D" alt="Fig1" width="520">
    <img src="https://raw.githubusercontent.com/mbashiri/tensor-decomposition-with-python/master/figures/metric-1.png?token=AjfLQx3EfwRyn6MqYe1_bLLJC_dZ9xjUks5cO1SBwA%3D%3D" alt="Fig1" width="300">
</p>

For the complete tutorial click [here](), and for the Jupyter notebook click [here]().


---
## Dependencies
- Numpy
- Matplotlib
- Seaborn
- TensorLy
- tensortools

---
## Acknowledgement
I would like to thank Annika Thierfelder for her constructive feedback on the content.

---
## References

