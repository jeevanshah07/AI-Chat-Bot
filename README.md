[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/AI-Chat-Bot)
# AI-Chat-Bot
A Chat Bot powered by a Neural Network helps it choose how to respond.

# If you are going to clone the bot make sure you do this:
1. Clone the repo `git clone https://github.com/marvelman3284/AI-Chat-Bot`
2. Once you clone the repo the first file you can run is `train.py`. The current training data is saved to data.pth so if you choose not to do this you will train with a loss of 0.0001. 
    2a. It is currently set to train for 1500 epochs, you can increase or decrease this number based on your computers specs.
        2b. I personally had issues training it on my gpu, so it is set to run on you cpu. You can change this by uncommenting out line 69 in `train.py` and line 7 in `chat.py`. Make sure to comment the other statemtent (Line 70 in `train.py` and line 9 in `chat.py`). Also make sure that both files are consistent. If one file is using gpu and the other is cpu then you will catch an error.
3. Run `chat.py` to interact with the bot!
