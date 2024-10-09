curl -sSf https://rye.astral.sh/get | RYE_TOOLCHAIN=`which python` RYE_INSTALL_OPTION="--yes" bash

mkdir -p ~/.local/bin
ln -s $HOME/.rye/shims/rye $HOME/.local/bin/rye

rye config --set-bool behavior.global-python=true
rye config --set-bool behavior.use-uv=true

mkdir -p ~/.local/share/bash-completion/completions
rye self completion > ~/.local/share/bash-completion/completions/rye.bash

rye self update
