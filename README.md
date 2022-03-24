# Python Coding Playground

---

## Conda Environments

> __conda__: Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN, and more.

The easiest way to install conda on your machine is via the [Anaconda Distribution](https://www.anaconda.com/distribution/) of Python & R. Once you have conda installed, read [&#34;A Guide to Conda Environments&#34;](https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533). This article will provide an introduce into some of the conda basics. If you need some additional help getting started, the official [&#34;Setting started with conda&#34;](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) guide will point you in the right direction.

:snake :

To get the sprint environment setup:

1. Open your command line tool (Terminal for MacOS, Anaconda Prompt for Windows)
2. Navigate to the folder with this sprint's content. There should be a`requirements.txt`
3. Run`conda create -n U4-S1-NLP python==3.7` => You can also rename the environment if you would like. Once the command completes, your conda environment should be ready.
4. Now, we are going to add in the require python packages for this sprint. You will need to 'activate' the conda environment:`source activate U4-S1-NLP` on Terminal or`conda activate U4-S1-NLP` on Anaconda Prompt. Once your environment is activate, run`pip install -r requirements.txt` which will install the required packages into your environment.
5. We are going to also add an Ipython Kernel reference to your conda environment, so we can use it from JupyterLab.
6. Next run`python -m ipykernel install --user --name U4-S1-NLP --display-name "U4-S1-NLP (Python3)"` => This will add a json object to an ipython file, so JupterLab will know that it can use this isolated instance of Python. :)
7. Last step, we need to install the models for Spacy. Run these commands`python -m spacy download en_core_web_md` and`python -m spacy download en_core_web_lg`
8. Deactivate your conda environment and launch JupyterLab. You should know see "U4-S1-NLP (Python3)" in the list of available kernels on launch screen.


# General

Note that you can generally add `-y` to avoid prompts for confirmation if using these in shell scripts.

Full docs at: https://conda.io/docs/commands.html#conda-general-commands .

```bash
## list environments
conda info --envs         # list environments

## switch environments (without `source` if you use CMD or PowerShell)
source activate myenv1    # activate envronment
source deactivate myenv1  # deactivate environment
                          # (!on Windows & Git Bash this may require a Bash restart afterwards!)


## create environments
conda create -n myenv1 python      # create environment (empty, using default python version)
                                   # !! you DO need the `python` there if you want an *empty*
                                   #    environment, otherwise the system packages will be included
                                   #    (and yeah, this is NOWHERE in the official documentation)
  
conda create -n myenv1             # create env with default python and global packages included
                                   # (!probably NOT what you want!)

conda create -n myenv1 python=2.7  # create empty env using specific python version

conda create -n myenv python django otherpackage  # create empty env with default python version
                                                  # and install packages `django` and `otherpackage`


## remove environment
conda remove -n myenv1 --all
```

# Windows tips

**TL;DR (brute force solution to most problems):** Just use CMD (`cmd.exe`, the old DOS-era-style shell...) with its default Windows GUI instead of fancier and more modern alternatives, and instead of "proper" conda environment switching just close shell window and open a new one. This is annoying but will let you avoid many weird bugs if really in a hurry...

Generally after `source deactivate` on Bash on Windows, Bash is left in a messed up state, with `conda` not in the path. Simplest solution is to restart shell...

If you come across lots of funny issues with Conda + Python 2.x on Windows (encoding WTFs etc.), switch to using **CMD**, it works much better with this combo than PowerShell or Bash. Also, being stuck in CMD-land, it's useful to remember the `start mycommand ...` and `start /B mycommand ...` tricks for starting background jobs just like you do with `&` suffix in Bash (the `/B` version is if you don't want the extra console window for seeing output or stopping the task).
