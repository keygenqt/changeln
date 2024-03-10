#!/bin/bash

#########################
## Build snap application
#########################

VERSION='2.0.0'

# Remove
sudo snap remove changeln

# Build clean
snapcraft clean

# Build snap
snapcraft -v

# Install
sudo snap install changeln_${VERSION}_amd64.snap --devmode --dangerous

# Upload
# snapcraft upload --release=candidate <snap>
# snapcraft upload --release=stable <snap>
