To turn into an executable, run the following commands:

```
pip install pyinstaller
pyinstaller --onefile ec2.py
sudo mv dist/ec2 /usr/local/bin/ec2
```

## Usage when executable is in PATH

```
ec2 us-west-2
```

# Usage when calling with python

```
python ec2.py us-west-2
```