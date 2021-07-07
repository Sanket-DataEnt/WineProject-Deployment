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
Download data from [here](https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing)
```

```bash
dvc add data_given/winequality.csv
```

# 6. Add and commit all the data to local

```bash
git add . && git commit -m "introductory commit"
```

# 6. Now create an empty repository on github and use the below command to push all the things in repo

```bash
git remote add origin https://github.com/XXXXX/XXX.git
git branch -M main
git push origin main
```

### tox command

```bash
tox
```

### for rebuilding after changes to requirememts.py file

```bash
tox -r
```

### pytest command

```bash
pytest -v
```

### setup commands -

```bash
pip install -e . 
```

### build your own package commands-

```bash
python setup.py sdist bdist_wheel
```

