# constraint_learning
PyBullet + Spinningup + CBN-IRL


# Installation
~~~~bash
git clone --recurse-submodules https://github.com/pidipidi/constraint_learning.git
cd constraint_learning
./install.sh
~~~~
This package also requires tensorflow, tensorforce, pytorch...


# Test
~~~~bash
source activate.sh
python test/test_pybullet_gym.py
~~~~



# Tip for submodules

Fetch and update the submodule projects on submodule directories
~~~~bash
git submodule update --remote
~~~~

Push changes from the root directory
~~~~bash
git push --recurse-submodules=check
~~~~