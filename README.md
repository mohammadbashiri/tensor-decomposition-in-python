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
	<img src="https://raw.githubusercontent.com/mohammadbashiri/tensor-decomposition-in-python/master/figures/tensor-decomposition.png" alt="Fig1" width="700">
</p>

### Example Scenario (with a neuroscientific theme)

An attempt to partially reproducing the result of [this paper](https://doi.org/10.1016/j.neuron.2018.05.015)'s figure 2.

<p align="center">
	<img src="https://raw.githubusercontent.com/mohammadbashiri/tensor-decomposition-in-python/master/figures/model.png" alt="Fig1" width="380">
    <img src="https://raw.githubusercontent.com/mohammadbashiri/tensor-decomposition-in-python/master/figures/neuron-time.png" alt="Fig1" width="500">
</p>

### Example Results and Comparison
<p align="center">
	<img src="https://raw.githubusercontent.com/mohammadbashiri/tensor-decomposition-in-python/master/figures/groundtruth-estimate.png" alt="Fig1" width="520">
    <img src="https://raw.githubusercontent.com/mohammadbashiri/tensor-decomposition-in-python/master/figures/metric-1.png" alt="Fig1" width="300">
</p>

For the complete tutorial click [here](https://medium.com/@mohammadbashiri93/tensor-decomposition-in-python-f1aa2f9adbf4), and for the extended version click [here](https://github.com/mohammadbashiri/tensor-decomposition-in-python/blob/master/TCA-extended.ipynb).


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
- Tuncer, Yalcin, Murat M. Tanik, and David B. Allison. "An overview of statistical decomposition techniques applied to complex systems." Computational statistics & data analysis 52.5 (2008): 2292–2310.
- Cichocki, Andrzej, et al. "Tensor decompositions for signal processing applications: From two-way to multiway component analysis." IEEE Signal Processing Magazine 32.2 (2015): 145–163.
- Williams, Alex H., et al. "Unsupervised Discovery of Demixed, Low-Dimensional Neural Dynamics across Multiple Timescales through Tensor Component Analysis." Neuron (2018).
- [Talk](https://www.youtube.com/watch?v=L8uT6hgMt00&t=1302s) by Tamara Kolda
- Tutorial by Alex Williams: [part 1](https://www.youtube.com/watch?v=hmmnRF66hOA), [part 2](https://www.youtube.com/watch?v=O-YTsSuEFiM&t=5s)
