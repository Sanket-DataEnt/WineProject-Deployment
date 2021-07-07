# 1. Created an environment

```bash
python3.7 -m venv myenv
```

# 2. Activating Environment

```bash
(source myenv/bin/activate)
```

# 3. Creating and installing requirements.txt

```bash
touch requirements.txt
pip install -r requirements.txt
```

# 4. Initialising the Git and DVC

```bash
init git
init dvc
```

# 5. Adding data to dvc

```bash
dvc add data_given/winequality.csv
```


