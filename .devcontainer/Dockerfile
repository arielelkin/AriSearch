FROM mcr.microsoft.com/devcontainers/miniconda:3

ARG CONDA_LOCK_VERSION=4.0.2

RUN python -m pip install --no-cache-dir "conda-lock==${CONDA_LOCK_VERSION}"

COPY .devcontainer/conda-lock.yml /tmp/arisearch-conda-lock.yml

RUN conda-lock install --no-mamba --name arisearch /tmp/arisearch-conda-lock.yml \
    && conda clean --all --force-pkgs-dirs --yes \
    && rm /tmp/arisearch-conda-lock.yml

ENV PATH="/opt/conda/envs/arisearch/bin:${PATH}"

RUN echo 'conda activate arisearch' >> /home/vscode/.bashrc \
    && echo 'conda activate arisearch' >> /home/vscode/.zshrc
