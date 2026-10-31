## Installation

The workshop runs in a single conda environment that holds every package both sessions use. Please build it before the workshop: it downloads a little under 3 GB, and building it takes 10 to 15 minutes on a good connection, longer on conference wifi.

### Which computers work

The environment builds on Windows (64-bit), on Linux, and on Macs with Apple silicon running macOS 15 or newer. On an Intel Mac, or a Mac running macOS 14 or older, two of the packages have no prebuilt version; use [Codespaces](#codespaces) instead.

The environment needs conda. A pip-only installation will not work, because one of the packages depends on a compiled library (SuiteSparse) that conda supplies.

### Building the environment

1. Install [Miniforge](https://conda-forge.org/download/), a small conda installer that uses the conda-forge channel. If you already have Anaconda or Miniconda, it will work too; the environment file does not use Anaconda's default channel.

2. Get the workshop materials, either with git,

   ```bash
   git clone https://github.com/knaaptime/workshop-pysal-narsc26.git
   ```

   or by downloading the zip file from the green Code button at <https://github.com/knaaptime/workshop-pysal-narsc26> and extracting it.

3. Open a terminal (on Windows, the Miniforge Prompt from the Start menu), move into the materials folder, and build the environment:

   ```bash
   cd workshop-pysal-narsc26
   conda env create -f environment.yml
   ```

4. Activate the environment and start JupyterLab:

   ```bash
   conda activate workshop-pysal-narsc26
   jupyter lab
   ```

5. In JupyterLab, open `content/check.ipynb` and run every cell. If the last cell prints a small table, the environment is ready.

If you built the environment some time ago, update it to the current version of the materials with

```bash
conda env update -f environment.yml --prune
```

### Codespaces

If your computer cannot build the environment, open the materials in a browser with the Open in GitHub Codespaces button in the [README](../README.md). Codespaces runs the same environment on a GitHub server and needs only a free GitHub account. The first launch builds the environment, which takes several minutes, so start it before the session begins.

### Troubleshooting

If JupyterLab fails to start on Windows with

```bash
FileNotFoundError: [WinError 2] The system cannot find the file specified
```

run the following in the Miniforge Prompt, with the environment active:

```bash
python -m ipykernel install --user
```
