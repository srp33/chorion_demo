#!/bin/bash

############################################
# This script has the logic for building a
# Docker image based on the Dockerfile.
############################################

set -o errexit

tmpDir=/tmp/build_chorion_data_layer_${USER}

rm -rf $tmpDir
mkdir -p $tmpDir

cp Dockerfile $tmpDir/
cp -r data.tsv $tmpDir/

cd $tmpDir
docker build -t srp33/chorion_data_layer .
cd -
