FROM mcr.microsoft.com/devcontainers/miniconda:latest

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Use conda-forge alone, as Miniforge does, rather than the image's defaults channel.
RUN /opt/conda/bin/conda config --system --add channels conda-forge \
    && (/opt/conda/bin/conda config --system --remove channels defaults || true)

# Build the workshop environment as its own named environment, leaving base alone:
# the workshop's Python is newer than the image's, and replacing base's Python breaks conda.
# Copy "noop.txt" too so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env create -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp \
    && echo ". /opt/conda/etc/profile.d/conda.sh && conda activate workshop-pysal-narsc26" >> /home/vscode/.bashrc

# [Optional] Uncomment to install a different version of Python than the default
# RUN conda install -y python=3.6 \
#     && pip install --no-cache-dir pipx \
#     && pipx reinstall-all

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
