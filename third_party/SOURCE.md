# Practice-Section Source Catalogue

This file records public repositories and bibliographic items cited in the practice sections of the associated book. It is a practice-section source catalogue, not the full bibliography of the book manuscript.

The repositories listed here are external projects used as reference implementations, reproducibility entry points, or software sources for the corresponding practice sections. This companion repository does not redistribute third-party source code, datasets, model weights, trained models, or documentation.

## Chapters 3--4: POT — Python Optimal Transport

- Public repository: [PythonOT/POT](https://github.com/PythonOT/POT)
- Paper: Flamary et al. (2021), [*POT: Python Optimal Transport*](https://jmlr.org/papers/v22/20-451.html), *Journal of Machine Learning Research*.
- BibTeX keys: `FlamaryEtAl2021POT`, `POTRepo`
- Role in this book: external Python optimal-transport toolbox used by self-written teaching scripts for discrete OT and Wasserstein shift examples.
- Attribution note: POT remains governed by its own license and citation requirements.

## Chapter 5: Sinkhorn and entropic optimal transport

- Paper: Cuturi (2013), [*Sinkhorn Distances: Lightspeed Computation of Optimal Transport*](https://papers.nips.cc/paper/4927-sinkhorn-distances-lightspeed-computation-of-optimal-transport), *Advances in Neural Information Processing Systems*.
- Paper: Feydy et al. (2019), [*Interpolating between Optimal Transport and MMD using Sinkhorn Divergences*](https://proceedings.mlr.press/v89/feydy19a.html), *Proceedings of Machine Learning Research*.
- Paper: Peyré and Cuturi (2019), [*Computational Optimal Transport with Applications to Data Science*](https://doi.org/10.1561/2200000073), *Foundations and Trends in Machine Learning*.
- BibTeX keys: `Cuturi2013`, `Feydy2019`, `PeyreCuturi2019`
- Role in this book: theoretical and computational references for entropic regularization, Sinkhorn iterations, and Sinkhorn divergence.

## Chapter 6: Learned Primal-Dual and Wasserstein-loss inverse problems

- Public repository: [adler-j/learned_primal_dual](https://github.com/adler-j/learned_primal_dual)
- Paper: Adler and Öktem (2018), [*Learned Primal-Dual Reconstruction*](https://doi.org/10.1109/TMI.2018.2799231), *IEEE Transactions on Medical Imaging*.
- Public repository: [adler-j/wasserstein_inverse_problems](https://github.com/adler-j/wasserstein_inverse_problems)
- Paper: Adler, Ringh, Öktem, and Karlsson (2017), [*Learning to Solve Inverse Problems Using Wasserstein Loss*](https://arxiv.org/abs/1710.10898), arXiv.
- BibTeX keys: `AdlerOktem2018LPD`, `AdlerLPDRepo`, `AdlerEtAl2017Wasserstein`, `AdlerWassersteinInverseRepo`
- Role in this book: public sources for learned inverse reconstruction and Wasserstein-loss training examples.
- Attribution note: these projects are cited as external sources; their code is not redistributed in this companion repository.

## Chapter 7: OT-CycleGAN

- Public repository: [jryoungw/OT_CycleGAN](https://github.com/jryoungw/OT_CycleGAN)
- Paper: Sim, Oh, Kim, Jung, and Ye (2020), [*Optimal Transport Driven CycleGAN for Unsupervised Learning in Inverse Problems*](https://doi.org/10.1137/20M1317992), *SIAM Journal on Imaging Sciences*.
- BibTeX keys: `Sim2020OTCycleGAN`, `OTCycleGANRepo`
- Role in this book: public source for OT-CycleGAN and unpaired inverse-problem translation; this repository also includes a self-written synthetic LDCT/SDCT-domain data-generation script for teaching use.
- Attribution note: the OT-CycleGAN implementation remains governed by its original repository. The synthetic LDCT/SDCT-domain data in this companion repository are not real clinical CT data and are not intended for clinical validation.

## Chapter 8: ADFWI

- Public repository: [liufeng2317/ADFWI](https://github.com/liufeng2317/ADFWI)
- Paper: Liu, Li, Zou, and Li (2025), [*Automatic Differentiation-Based Full Waveform Inversion With Flexible Workflows*](https://doi.org/10.1029/2024JH000542), *Journal of Geophysical Research: Machine Learning and Computation*.
- BibTeX keys: `Liu2025JGR`, `ADFWIRepo`
- Role in this book: public source for automatic-differentiation-based full-waveform inversion and flexible waveform-inversion workflows.
- Attribution note: ADFWI remains governed by its own license, software archive, and citation requirements.

## Chapter 9: OT-Flow

- Public repository: [EmoryMLIP/OT-Flow](https://github.com/EmoryMLIP/OT-Flow)
- Paper: Onken, Wu Fung, Li, and Ruthotto (2021), [*OT-Flow: Fast and Accurate Continuous Normalizing Flows via Optimal Transport*](https://doi.org/10.1609/aaai.v35i10.17113), *Proceedings of the AAAI Conference on Artificial Intelligence*.
- BibTeX keys: `Onken2021OTFlow`, `OTFlowRepo`
- Role in this book: public source for optimal-transport-regularized continuous normalizing flows and continuous distribution paths.
- Attribution note: OT-Flow remains governed by its original repository and citation requirements.

## Chapter 10: Flower and pyABC

- Public repository: [mehrsapo/Flower](https://github.com/mehrsapo/Flower)
- Paper: Pourya, El Rawas, and Unser (2026), [*Flower: A Flow-Matching Solver for Inverse Problems*](https://openreview.net/forum?id=QGd34p02mI), ICLR.
- Public repository: [ICB-DCM/pyABC](https://github.com/ICB-DCM/pyABC)
- Paper: Schälte, Klinger, Alamoudi, and Hasenauer (2022), [*pyABC: Efficient and robust easy-to-use approximate Bayesian computation*](https://doi.org/10.21105/joss.04304), *Journal of Open Source Software*.
- BibTeX keys: `Pourya2025Flower`, `FlowerRepo`, `Schalte2022pyABC`, `pyABCRepo`
- Role in this book: public sources for flow-matching inverse solvers and approximate Bayesian computation / ABC-SMC inference.
- Attribution note: Flower and pyABC remain governed by their own licenses and citation requirements.
