myDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
sudo -H python3 -m pip install --upgrade $myDIR/dist/*
