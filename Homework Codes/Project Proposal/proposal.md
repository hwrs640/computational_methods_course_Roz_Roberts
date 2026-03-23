# Project Proposal (Draft — Version 1)
## Motivation and scientific question

Understanding precipitation variability during the North American Monsoon (NAM) is critical for improving short-term forecasting in southeastern Arizona during the summer months.
Previous work has identified distinct precipitation regimes using clustering approaches such as Self-Organizing Maps (SOM) and agglomerative hierarchical clustering. 
However, these methods primarily describe the average spatial structure of precipitation, and not the within regime modes of variability.

This project will ask: What are the dominant spatial modes of precipitation variability within each identified monsoon regime, and how do these modes relate to large-scale atmospheric structure?

## Dataset

This project will combine high-resolution precipitation data with large-scale (corse-resolution) reanalysis fields. Specifically I will be using the following:
- Precipitation: Daily PRISM 24-hour precipitation fields over a 1° × 1° domain centered on Tucson, Arizona.
- Atmospheric fields (ERA5):
- Geopotential height at 250, 500, and 850 hPa
- Eastward and northward water vapor flux
- Precipitable water

The analysis will focus on the core NAM season of July and August over the period of 1981–2024, providing a multi-decadal dataset of daily fields.

Previously identified precipitation regimes (via SOM + agglomerative clustering) will be used to subset the dataset. Each day is assigned to only one regime, allowing regime-specific analysis to take place.

Challenges include the following:
- Large data volume from ERA5 requiring efficient preprocessing
- Spatial mismatch between PRISM (high-resolution) and ERA5 (relativly low-resolution) grids
- Potential imbalance in the number of samples across regimes

## Proposed method

The primary method will be Singular Value Decomposition (SVD) / Principal Component Analysis (PCA) applied to the precipitation fields within each regime.

Workflow of the approach:
1) Regime separation
    - Use existing SOM + clustering labels to group daily precipitation fields
3) PCA within each regime
   - Input: Flattened precipitation fields for all days in a given regime
3) Output:
   - Principal spatial modes (EOF-like patterns)
   - Corresponding time coefficients (PCs)
   - Physical interpretation
   - Composite ERA5 fields (e.g., IVT, geopotential height) conditioned on high/low values of leading PCs

This workflow hopes to link precipitation variability modes to large-scale atmospheric drivers rather than just considering the average of a regime.
This method is appropriate because PCA provides a compact representation of dominant variability patterns, allowing identification of coherent spatial structures beyond mean composites.

## Expected outcomes and evaluation
This project is expected reveal the following:
- Identify dominant spatial modes of precipitation variability within each regime
- Reveal whether regimes are internally homogeneous or contain multiple sub-patterns
- Establish links between precipitation variability modes and large-scale atmospheric circulation
- Evaluation metrics and diagnostics will include:
    - Explained variance of leading principal components (to assess dimensionality reduction effectiveness)
    - Spatial pattern analysis of EOFs (interpretability and physical realism)
    - Composite analysis of ERA5 fields conditioned on PC extremes
    - Regime-mean precipitation patterns vs. leading EOFs

A successful outcome will demonstrate that PCA captures meaningful, physically interpretable variability that is not evident in regime averages alone.
