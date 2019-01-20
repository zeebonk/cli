#!/bin/bash

set -e
#set -x

pip=pip3.7
python=python3.7

tag=$1

if [ $tag == '' ]; then
	echo "Usage:"
	echo "bash update_snap.sh <tag>"
	exit 1
fi

BUILD_DIR=`mktemp -d`

echo "Building in $BUILD_DIR..."

cd $BUILD_DIR
echo "Creating a virtualenv..."
virtualenv --python=$python . &> /dev/null
source ./bin/activate
echo "Installing asyncy==$tag..."
$pip install asyncy==$tag &> /dev/null

echo "Cloning asyncy/snapcraft..."
git clone git@github.com:asyncy/snapcraft.git &> /dev/null
cd snapcraft

echo "Running pip freeze and building snapcraft.yaml..."
$pip freeze | grep -v asyncy== | $python scripts/build.py $tag > snapcraft.yaml
deactivate

git checkout -b release_$tag
git commit -a -m "Release $tag."
git push origin release_$tag
echo "Branch release_$tag created. Please open a PR and have it accepted."

cd ../..
echo "Cleaning $BUILD_DIR..."
rm -rf $BUILD_DIR
echo "Done!"
