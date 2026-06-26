# Optimal Transport for Inverse Problems — Companion Code

![Repository banner](docs/assets/banner.svg)

**Authors:** Jian Sun (孙建) and Wenshuai Wang (汪文帅)  
**Repository name:** `sunjian-ot-inverse-book-code`

This repository accompanies a book manuscript on optimal transport and inverse problems. It is organized by chapter and records the self-written teaching scripts, the Chapter 7 synthetic CT-domain data-generation script, and the practice-section source catalogue cited by the book.

![Workflow](docs/assets/workflow.svg)

## Repository contents

| Chapter | Directory | Content |
|---|---|---|
| Chapter 1 | `chapters/ch01_illposed_linear/` | Self-written teaching script for ill-posed linear inversion and Tikhonov regularization. |
| Chapter 2 | `chapters/ch02_euclidean_shift/` | Self-written teaching script for Euclidean misfit under spatial shift. |
| Chapter 3 | `chapters/ch03_discrete_ot/` | Self-written teaching script for a discrete optimal transport matrix example using POT. |
| Chapter 4 | `chapters/ch04_wasserstein_shift/` | Self-written teaching script comparing $L^2$, $W_1$, and $W_2$ shift landscapes. |
| Chapter 5 | `chapters/ch05_sinkhorn/` | Self-written PyTorch benchmark for Sinkhorn computation, epsilon scaling, and debiased Sinkhorn divergence. |
| Chapter 6 | `chapters/ch06_lpd_wasserstein/` | Chapter-level source note for Learned Primal-Dual Reconstruction and Wasserstein-loss inverse-problem references. |
| Chapter 7 | `chapters/ch07_ot_cyclegan/` | Chapter-level source note and synthetic LDCT/SDCT data-generation script. |
| Chapter 8 | `chapters/ch08_adfwi_sinkhorn_fwi/` | Chapter-level source note for ADFWI. |
| Chapter 9 | `chapters/ch09_ot_flow_swiss_roll/` | Chapter-level source note for OT-Flow. |
| Chapter 10 | `chapters/ch10_posterior_flow_abc/` | Chapter-level source note for Flower and pyABC. |

![Chapter overview](docs/assets/chapter_overview.svg)

## Self-written scripts

The self-written scripts included in this repository are:

```text
chapters/ch01_illposed_linear/main.py
chapters/ch02_euclidean_shift/main.py
chapters/ch03_discrete_ot/main.py
chapters/ch04_wasserstein_shift/main.py
chapters/ch05_sinkhorn/main.py
chapters/ch07_ot_cyclegan/simulation_data.py
```

## Practice-section source catalogue

External projects and bibliographic items cited in the book practice sections are recorded in [`third_party/SOURCE.md`](third_party/SOURCE.md). The file [`third_party/references.bib`](third_party/references.bib) provides BibTeX entries for the practice-section references only; it is not the full bibliography of the book manuscript.

| Chapter | Practice-section source items | Public repository or reference |
|---|---|---|
| Chapters 3--4 | POT: Python Optimal Transport | [`PythonOT/POT`](https://github.com/PythonOT/POT) |
| Chapter 5 | Sinkhorn and entropic optimal transport references | Cuturi (2013); Feydy et al. (2019); Peyré and Cuturi (2019) |
| Chapter 6 | Learned Primal-Dual Reconstruction; Wasserstein inverse problems | [`adler-j/learned_primal_dual`](https://github.com/adler-j/learned_primal_dual); [`adler-j/wasserstein_inverse_problems`](https://github.com/adler-j/wasserstein_inverse_problems) |
| Chapter 7 | OT-CycleGAN | [`jryoungw/OT_CycleGAN`](https://github.com/jryoungw/OT_CycleGAN) |
| Chapter 8 | ADFWI | [`liufeng2317/ADFWI`](https://github.com/liufeng2317/ADFWI) |
| Chapter 9 | OT-Flow | [`EmoryMLIP/OT-Flow`](https://github.com/EmoryMLIP/OT-Flow) |
| Chapter 10 | Flower; pyABC | [`mehrsapo/Flower`](https://github.com/mehrsapo/Flower); [`ICB-DCM/pyABC`](https://github.com/ICB-DCM/pyABC) |

## Repository structure

```text
sunjian-ot-inverse-book-code/
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── environment.yml
├── chapters/
├── docs/
├── third_party/
└── tools/
```

## Citation

Citation metadata for this companion repository are provided in [`CITATION.cff`](CITATION.cff).

## License and attribution

The self-written materials in this repository are released under the license in [`LICENSE`](LICENSE). External projects listed in [`third_party/SOURCE.md`](third_party/SOURCE.md) remain governed by their own licenses and citation requirements.
