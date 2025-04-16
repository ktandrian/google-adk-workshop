## Material

[ADK Workshop slide](https://docs.google.com/presentation/d/1NgXccjzHEti5-Psc4-WPiDFo8zV_0LtUTBRqhFKDs9k/edit?usp=sharing)


## Setup
- Minimum is python 3.11
- Checkout code
```bash
git clone https://github.com/yapweiyih/google-adk-workshop.git
cd google-adk-workshop
```

## Setup virtual env with UV

```bash
# Install python
uv python install 3.11

# Pin a specific python version for current project
uv python pin 3.11

# Create venv
uv venv
source .venv/bin/activate

# install packages
uv pip install -r requirements
```


# Setup virtual env with Conda

```bash
conda create -n adk_release python=3.11 ipykernel -y
conda activate adk_release
pip install -r requirements.txt

```