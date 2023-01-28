#!/bin/bash
echo "-------------------------"
echo "setup default gateway for ipv4"
sudo ip -4 route add default via (cat /etc/ilab_control_ipv4)

echo "-------------------------"
echo "performing apt-get update"
echo "-------------------------"
sudo apt-get update;

echo "-------------------------"
echo "Installing python and pip"
echo "-------------------------"
sudo apt-get install python3;
sudo apt-get install pip;


echo "-------------------------"
echo "installing flask"
echo "-------------------------"
pip install -q flask;

echo "installing grpcio and grpcio-tools"
echo "-------------------------"
pip install -q grpcio;
pip install -q grpcio-tools;


echo "installing strawberry-graphql"
echo "-------------------------"
pip install -q "strawberry-graphql[debug-server]";

echo "adding installed python libraries to path";
echo "-------------------------"
sudo export PATH="$HOME/.local/bin:$PATH";

echo ""
echo ""
echo "done."
