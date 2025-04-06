#! /bin/bash

set -xe

BASERAWURL=https://raw.githubusercontent.com/L4Re/l4re.org/refs/heads/main/src/use-cases/net-swt-curl/

mkdir demo
cd demo

wget -q $BASERAWURL/manifest-l4re-net-curl.xml

# Get sources
git clone https://github.com/kernkonzept/ham.git
ham/ham init -f manifest-l4re-net-curl.xml
ham/ham sync

# Get individual files out of the page on l4re.org
wget -q $BASERAWURL/modules.list
wget -q $BASERAWURL/net-vswt-curl-example.cfg
wget -q $BASERAWURL/resolv.conf
wget -q $BASERAWURL/virtio-net-switch-drv-example.cfg

# Build the microkernel
make -C fiasco -j8

# Build the user-level
make -C l4 B=build
# Enable usage of ixl network drivers in virtual network switch
l4/tool/kconfig/scripts/config --file l4/build/.kconfig --enable CONFIG_VNS_IXL
make -C l4/build -j8 oldconfig
# Build
make -C l4/build -j8 

# Run QEMU
make -C l4/build qemu E=virtio-net-switch-drv-example \
     MODULES_LIST=$PWD/modules.list \
     MODULE_SEARCH_PATH=$PWD/fiasco/build:$PWD \
     QEMU_OPTIONS="-serial stdio -vnc none -m 1g -netdev user,id=net1 -device e1000,netdev=net1"
