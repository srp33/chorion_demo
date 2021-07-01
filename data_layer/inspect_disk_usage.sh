#! /bin/bash

sudo du -s --block-size=1 /var/lib/docker/aufs

# Before building data layer:
# 111763021824	/var/lib/docker/aufs
# After building data layer:
# 111763038208	/var/lib/docker/aufs
# Difference = 16384 = 2^14 (must be storage unit on this file system)
