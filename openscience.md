---
layout: default
title: Open Science at the TELOS Collaboration
image: tsukuba
---

The TELOS Collaboration has a strong commitment to open science.
We aim to make all products of and processes used in our research openly available.
The overall process that we aim to follow is documented in
[arXiv:2504.01876][strategy]
(also [on Zenodo][strategy-zenodo];
working draft [on GitHub][strategy-github]).

## Data

For all new peer-reviewed articles released,
we aim to provide underpinning data.
This includes the raw data,
as transferred from high-performance computing systems,
and processed output data,
as shown in publications.

For conference proceedings,
we may refer to a previous or forthcoming peer-reviewed article
for the associated data.

To find our releases,
look for links marked "Data" in our [publications](/publications).

## Workflows

For all new peer-reviewed articles released,
we aim to provide a fully reproducible analysis workflow.
This takes raw data,
as transferred from high-performance computing systems,
and outputs the processed data, plots, and tables,
as included in publications.

For conference proceedings,
we may refer to a previous or forthcoming peer-reviewed article
for the associated workflow.

To find our releases,
look for links marked "Workflow" in our [publications](/publications).

## Field configurations

We aim to share our gauge ensembles openly in the near future,
via the [UKLFT][uklft] Regional Grid of [the International Lattice Data Grid][ildg].

If in the mean time you would like access to
the gauge ensembles supporting our published work,
please get in touch.

## Software

We make use of the following community software in our work:

- [Grid][grid],
  developed by Peter Boyle and collaborators,
  for generating field configurations and computing observables on them.
- [HiRep][hirep],
  developed by Claudio Pica and collaborators,
  for generating field configurations and computing observables on them.
  We specifically use [a fork][hirep-spn] adapted to work with symplectic groups,
  developed in house
  and optimised by Research Software Engineers
  at the Swansea Academy of Advanced Computing.
- [Hadrons][hadrons],
  developed by Antonin Portelli and collaborators,
  for computing observables on field configurations.
- [Snakemake][snakemake],
  for constructing data analysis workflows.
- [Python][python] and the scientific Python ecosystem
  ([numpy][numpy], [Scipy][scipy], [Pandas][pandas], [Matplotlib][matplotlib]),
  for performing data analysis.
- [gvar][gvar], [lsqfit][lsqfit], and [corrfitter][corrfitter],
  for performing fits of correlation functions.

We are grateful to the contributions of the development communities of these codebases,
without which our research would not be possible.

## Literature

We make preprints of our work available via [arXiv][arxiv].
We aim to publish all our work as open access in open access or hybrid journals;
additionally,
postprints of our work are available via
Swansea University's [Cronfa][cronfa] institutional repository.

[arxiv]: <https://arxiv.org>
[cronfa]: <https://cronfa.swan.ac.uk>
[ildg]: <https://hpc.desy.de/ildg/>
[strategy]: <https://arxiv.org/abs/2504.01876>
[strategy-github]: <https://github.com/telos-collaboration/strategy>
[strategy-zenodo]: <https://doi.org/10.5281/zenodo.15113709>
[uklft]: <https://generic.wordpress.soton.ac.uk/uklft/>

[grid]: <https://github.com/paboyle/Grid>
[hadrons]: <https://github.com/aportelli/Hadrons>
[hirep]: <https://github.com/claudiopica/HiRep>
[hirep-spn]: <https://github.com/sa2c/HiRep>

[python]: <https://python.org>
[numpy]: <https://numpy.org>
[scipy]: <https://scipy.org>
[pandas]: <https://pandas.pydata.org>
[matplotlib]: <https://matplotlib.org>
[gvar]: <https://github.com/gplepage/gvar>
[lsqfit]: <https://github.com/gplepage/lsqfit>
[corrfitter]: <https://github.com/gplepage/corrfitter>
[snakemake]: <https://snakemake.github.io>
