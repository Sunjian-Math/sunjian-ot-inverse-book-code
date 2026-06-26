# Inverse Problems and Optimal Transport: Companion Code Repository

![Repository banner](docs/assets/banner.svg)

This repository accompanies the Chinese academic monograph **《反问题与最优传输》** by **孙建** and **汪文帅**.

**Repository name:** `sunjian-ot-inverse-book-code`  
**Repository URL:** <https://github.com/Sunjian-Math/sunjian-ot-inverse-book-code>

This repository is organized by chapter and records self-written teaching scripts, synthetic data-generation scripts, practice-section source notes, selected BibTeX entries, QR-code materials, and repository-level documentation for readers who want to reproduce or extend the book's computational examples.

This repository does **not** replace the book manuscript and does **not** redistribute third-party source code, datasets, trained models, or documentation. External repositories are cited as public source projects, reference implementations, or reproducibility entry points only.

![Workflow](docs/assets/workflow.svg)

## Repository contents

| Chapter | Directory | Content |
|---|---|---|
| Chapter 1 | `chapters/ch01_illposed_linear/` | Self-written teaching script for ill-posed linear inversion and Tikhonov regularization. |
| Chapter 2 | `chapters/ch02_euclidean_shift/` | Self-written teaching script for Euclidean misfit under spatial shift. |
| Chapter 3 | `chapters/ch03_discrete_ot/` | Self-written teaching script for a discrete optimal-transport matrix example using POT. |
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
tools/make_qr.py
```

## Practice-section source catalogue

External projects and bibliographic items cited in the book practice sections are recorded in [`third_party/SOURCE.md`](third_party/SOURCE.md). The file [`third_party/references.bib`](third_party/references.bib) provides BibTeX entries for the practice-section references only; it is not the full bibliography of the book manuscript.

The table below gives direct links to the referenced public repositories and the corresponding papers. These links are provided for attribution, traceability, and reader convenience. This companion repository does not redistribute third-party source code.

| Chapter | Practice-section source items | Public repository links | Corresponding paper links |
|---|---|---|---|
| Chapters 3--4 | POT: Python Optimal Transport | [`PythonOT/POT`](https://github.com/PythonOT/POT) | [Flamary et al. (2021)](https://jmlr.org/papers/v22/20-451.html) |
| Chapter 5 | Sinkhorn and entropic optimal transport references | — | [Cuturi (2013)](https://papers.neurips.cc/paper_files/paper/2013/hash/af21d0c97db2e27e13572cbf59eb343d-Abstract.html); [Feydy et al. (2019)](https://proceedings.mlr.press/v89/feydy19a.html); [Peyré and Cuturi (2019)](https://doi.org/10.1561/2200000073) |
| Chapter 6 | Learned Primal-Dual Reconstruction; Wasserstein-loss inverse problems | [`adler-j/learned_primal_dual`](https://github.com/adler-j/learned_primal_dual); [`adler-j/wasserstein_inverse_problems`](https://github.com/adler-j/wasserstein_inverse_problems) | [Adler and Öktem (2018)](https://doi.org/10.1109/TMI.2018.2799231); [Adler et al. (2017)](https://arxiv.org/abs/1710.10898) |
| Chapter 7 | OT-CycleGAN | [`jryoungw/OT_CycleGAN`](https://github.com/jryoungw/OT_CycleGAN) | [Sim et al. (2020)](https://doi.org/10.1137/20M1317992) |
| Chapter 8 | ADFWI | [`liufeng2317/ADFWI`](https://github.com/liufeng2317/ADFWI) | [Liu et al. (2025)](https://doi.org/10.1029/2024JH000542) |
| Chapter 9 | OT-Flow | [`EmoryMLIP/OT-Flow`](https://github.com/EmoryMLIP/OT-Flow) | [Onken et al. (2021)](https://doi.org/10.1609/aaai.v35i10.17113) |
| Chapter 10 | Flower; pyABC | [`mehrsapo/Flower`](https://github.com/mehrsapo/Flower); [`ICB-DCM/pyABC`](https://github.com/ICB-DCM/pyABC) | [Pourya et al. (2026)](https://openreview.net/forum?id=QGd34p02mI); [Schälte et al. (2022)](https://doi.org/10.21105/joss.04304); [Klinger et al. (2018)](https://doi.org/10.1093/bioinformatics/bty361) |

## QR code for the book

The repository QR code can be generated with:

```bash
python tools/make_qr.py
```

The script writes a PNG preview to `docs/assets/book_companion_code_qr.png` and a print-oriented PDF to `figures/qrcode/book_companion_code_qr.pdf`.

## Repository structure

```text
sunjian-ot-inverse-book-code/
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── environment.yml
├── check_report.txt
├── chapters/
├── docs/
├── figures/
├── third_party/
└── tools/
```

## Citation

Citation metadata for this companion repository are provided in [`CITATION.cff`](CITATION.cff). Practice-section references and external source entries are listed in [`third_party/references.bib`](third_party/references.bib).

## License and attribution

The self-written materials in this repository are released under the license in [`LICENSE`](LICENSE). External projects listed in [`third_party/SOURCE.md`](third_party/SOURCE.md) remain governed by their own licenses, citation requirements, and usage terms.
