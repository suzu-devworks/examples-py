ARG VARIANT="1-3.12-bookworm"
FROM mcr.microsoft.com/devcontainers/python:${VARIANT} as dev-stage

## Configure apt and install packages
RUN set -x \
    && apt update \
    && apt install sqlite3 \
    ;

# Clean up
RUN set -x \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/* \
    ;
