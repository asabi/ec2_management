To turn into an executable, run the following commands:

```
pip install pyinstaller
pyinstaller --onefile ec2.py
sudo mv dist/ec2 /usr/local/bin/ec2
```

## Usage

```
ec2 us-west-2
```