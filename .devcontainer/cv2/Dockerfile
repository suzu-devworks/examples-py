FROM mcr.microsoft.com/devcontainers/base:ubuntu AS develop-stage

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

## Configure apt and install packages
RUN set -x \
    && apt update \
    && apt install --no-install-recommends -y \
        libgl1-mesa-dev libglib2.0-0 \
    ;

# Clean up
RUN set -x \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/* \
    ;

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog
