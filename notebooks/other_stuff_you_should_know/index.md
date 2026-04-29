# Other Stuff You Should Know

This mini-sequence collects practical machine learning workflow topics that do not fit neatly into a single model family. The emphasis is on **how to run experiments well**, not on introducing another architecture.

## Notebook Sequence

1. `0_ml_systems_overview.ipynb` — why training pipelines and workflow choices matter
2. `1_dataloading_in_practice.ipynb` — workers, pinning memory, prefetching, and sharding
3. `2_device_management_and_gpu_usage.ipynb` — choosing devices, moving tensors carefully, and measuring throughput
4. `3_clean_training_loops_with_callbacks.ipynb` — structuring PyTorch training code without hiding the mechanics
5. `4_tracking_runs_with_tensorboard.ipynb` — logging and comparing experiments with one lightweight workflow tool

The notebooks are designed to work on CPU-only machines, but several cells expose extra information when CUDA is available.
