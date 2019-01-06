import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def rank_one_tensor(a, b, c):
    """Returns a rank 1 tensor, given three vectors  
    """
    a = a.reshape(-1, 1).astype(np.float32)
    b = b.reshape(-1, 1).astype(np.float32)
    c = c.reshape(-1, 1).astype(np.float32)
    return np.tensordot(a * b.T, c, axes=0)[:, :, :, 0]


def normalize(x, lower=0, upper=1, axis=0):
    return (x - x.min(axis=axis)) / (x.max(axis=axis) - x.min(axis=axis))


def reconstruct(factors, rank=None):
    a, b, c = factors
    rank = rank if rank else a.shape[1]
    R1s = np.zeros((a.shape[0], b.shape[0], c.shape[0], rank))
    for i in range(rank):
        R1s[:, :, :, i] = rank_one_tensor(a[:, i], b[:, i], c[:, i])
    return R1s.sum(axis=3)

def plot_factors(factors, d=3):
    a, b, c = factors
    rank = a.shape[1]
    fig, axes = plt.subplots(rank, d, figsize=(8, int(rank * 1.2 + 1)))
    factors_name = ["Time", "Features", "Time"] if d==3 else ["Time", "Features"]
    for ind, (factor, axs) in enumerate(zip(factors[:d], axes.T)):
        axs[-1].set_xlabel(factors_name[ind])
        for i, (f, ax) in enumerate(zip(factor.T, axs)):
            sns.despine(top=True, ax=ax)
            ax.plot(f)
            axes[i, 0].set_ylabel("Factor " + str(i+1))
    fig.tight_layout()
    
    
def compare_factors(factors, factors_actual, factors_ind=[0, 1, 2], fig=None):

    a_actual, b_actual, c_actual = factors_actual
    a, b, c = factors
    rank = a.shape[1]
    
    fig, axes = fig, np.array(fig.axes).reshape(rank, -1) if fig else plt.subplots(rank, 3, figsize=(8, int(rank * 1.2 + 1)))
    sns.despine(top=True)

    f_ind = factors_ind

    for ind, ax in enumerate(axes):
        ax1, ax2, ax3 = ax
        label, label_actual = ("Estimate", "Ground truth") if ind==0 else (None, None)
        ax1.plot(a_actual[:, ind], lw=5, c='b', alpha=.8, label=label_actual);  # a
        ax1.plot(a[:, f_ind[ind]], lw=2, c='red', label=label);  # a
        ax2.plot(b_actual[:, ind], lw=5, c='b', alpha=.8);  # b
        ax2.plot(b[:, f_ind[ind]], lw=2, c='red');  # a
        ax3.plot(c_actual[:, ind], lw=5, c='b', alpha=.8);  # c
        ax3.plot(c[:, f_ind[ind]], lw=2, c='red');  # a
        
        ax2.set_yticklabels([])
        ax2.set_yticks([])
        ax3.set_yticklabels([])
        ax3.set_yticks([])
        ax1.set_ylabel("Factor {}".format(ind+1), fontsize=15)
        
        if ind != 2:
            ax1.set_xticks([])
            ax1.set_xticklabels([])
            ax2.set_xticks([])
            ax2.set_xticklabels([])
            ax3.set_xticks([])
            ax3.set_xticklabels([])
        else:
            ax1.set_xlabel("Time", fontsize=15)
            ax2.set_xlabel("Neuron", fontsize=15)
            ax3.set_xlabel("Trial", fontsize=15)

    fig.tight_layout()
    fig.legend(loc='lower left', bbox_to_anchor= (0.08, -0.02), ncol=2, 
               borderaxespad=0, fontsize=15, frameon=False)
    
    return fig, axes