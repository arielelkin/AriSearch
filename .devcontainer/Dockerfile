FROM mcr.microsoft.com/devcontainers/miniconda:3

ARG CONDA_LOCK_VERSION=4.0.2

RUN python -m pip install --no-cache-dir "conda-lock==${CONDA_LOCK_VERSION}"

COPY .devcontainer/conda-lock.yml /tmp/arisearch-conda-lock.yml

# Conda uses raw URL basenames for cache and extraction names without decoding
# escaped version epochs. Normalize %21 to the equivalent, valid literal "!" so
# .conda archive members (for example cddlib 1!0.94n) match the cache filename.
RUN sed -i '/^[[:space:]]*url:/ s/%21/!/g' /tmp/arisearch-conda-lock.yml \
    && conda-lock install --no-mamba --name arisearch /tmp/arisearch-conda-lock.yml \
    && conda clean --all --force-pkgs-dirs --yes \
    && rm /tmp/arisearch-conda-lock.yml

ENV PATH="/opt/conda/envs/arisearch/bin:${PATH}"
