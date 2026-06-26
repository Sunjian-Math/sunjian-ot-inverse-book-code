import numpy as np
import torch
from scipy.ndimage import gaussian_filter
from skimage.data import shepp_logan_phantom
from skimage.util import random_noise

# =========================================================================
# Synthetic LDCT / SDCT-domain data generation for Chapter 7
# =========================================================================

def generate_ct_pair(seed: int = 42):
    """Generate one synthetic LDCT/SDCT-domain pair.

    The SDCT-domain image is a smoothed Shepp--Logan phantom.
    The LDCT-domain image is obtained by adding Poisson and Gaussian noise.

    Returns
    -------
    ldct_obs : np.ndarray
        Synthetic low-dose CT-domain image.
    sdct_prior : np.ndarray
        Synthetic standard-dose/high-quality CT-domain image.
    ldct_tensor : torch.Tensor
        Tensor version with shape [1, 1, H, W].
    sdct_tensor : torch.Tensor
        Tensor version with shape [1, 1, H, W].
    """
    np.random.seed(seed)

    base_phantom = shepp_logan_phantom().astype(np.float32)

    sdct_prior = gaussian_filter(base_phantom, sigma=0.8)
    sdct_prior = np.clip(sdct_prior, 0.0, 1.0)

    ldct_obs = random_noise(sdct_prior, mode="poisson")
    ldct_obs = random_noise(ldct_obs, mode="gaussian", var=0.025)
    ldct_obs = np.clip(ldct_obs, 0.0, 1.0).astype(np.float32)

    sdct_prior = sdct_prior.astype(np.float32)

    ldct_tensor = torch.from_numpy(ldct_obs).float().unsqueeze(0).unsqueeze(0)
    sdct_tensor = torch.from_numpy(sdct_prior).float().unsqueeze(0).unsqueeze(0)
    return ldct_obs, sdct_prior, ldct_tensor, sdct_tensor


def generate_unpaired_ct_domains(num_samples: int = 16, seed: int = 42):
    """Generate synthetic LDCT and SDCT-domain sample lists.

    Different random seeds are used to create multiple samples. The returned
    lists can be treated as two teaching-domain sample collections.
    """
    ldct_samples = []
    sdct_samples = []

    for idx in range(num_samples):
        ldct_obs, sdct_prior, _, _ = generate_ct_pair(seed=seed + idx)
        ldct_samples.append(ldct_obs)
        sdct_samples.append(sdct_prior)

    return ldct_samples, sdct_samples


if __name__ == "__main__":
    ldct_obs, sdct_prior, ldct_tensor, sdct_tensor = generate_ct_pair()

    print(f"LDCT tensor shape: {tuple(ldct_tensor.shape)}")
    print(f"SDCT tensor shape: {tuple(sdct_tensor.shape)}")
    print(f"LDCT intensity range: [{ldct_obs.min():.4f}, {ldct_obs.max():.4f}]")
    print(f"SDCT intensity range: [{sdct_prior.min():.4f}, {sdct_prior.max():.4f}]")
