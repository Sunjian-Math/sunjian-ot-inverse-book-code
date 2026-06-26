# Chapter 7 — OT-CycleGAN and Synthetic CT Domains

## Overview

This directory corresponds to the Chapter 7 practice discussion of OT-CycleGAN for unpaired CT-domain translation.

## Contents

`simulation_data.py` is a self-written teaching script that generates synthetic LDCT/SDCT-domain samples from a Shepp--Logan phantom by applying Gaussian smoothing, Poisson noise, and Gaussian noise.

## Source note

External repository: `jryoungw/OT_CycleGAN`.

The synthetic LDCT/SDCT-domain data generated in this directory are self-written teaching examples. They are not real clinical CT data and are not intended for clinical validation. Real low-dose and standard-dose CT datasets may involve patient privacy, ethics approval, data-use agreements, and institutional restrictions. This directory does not redistribute the OT-CycleGAN source code, clinical datasets, pretrained models, or model weights.

For the practice-section source catalogue, see [`../../third_party/SOURCE.md`](../../third_party/SOURCE.md). Manuscript-synchronized BibTeX entries for practice-section references and external repository entries are available in [`../../third_party/references.bib`](../../third_party/references.bib).
