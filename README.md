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

# Training and testing the peg-in-shallow-hole task
~~~~bash
source activate.sh
python test/train_spinningup_torch.py
~~~~
After running the above code (or if it converges), run the following code
~~~~bash
source activate.sh
python test/test_spinningup_torch.py -l 100
~~~~



# FAQ
# Tips for submodules

Install(complie) submodule
~~~~bash
cd submodule
pip install --ignore-installed pip
~~~~

Fetch and update the submodule projects on submodule directories
~~~~bash
git submodule update --remote
~~~~

Push changes from the root directory
~~~~bash
git push --recurse-submodules=check
~~~~

# Matplot Error
Set tkagg as the backend
~~~~bash
emacs -nw ~/.config/matplotlib/matplotlibrc
~~~~
add "backend : tkagg"

It there is an error "no module named tkinter":
~~~~bash
sudo apt-get install python3.7-tk
~~~~