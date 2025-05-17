# ANN-Clasifocation-Churn
while deploying your streamlit app with an older version of python,tensorflow: follow this instructions:
1. in requirement.txt please mention streamlit : streamlit>=1.8.0, h5py==3.8.0
2. while deploying, it will show error, go to manage app at bottom left corner of the "oops message" and at the end there will be 3 dots click on that -> settings -> select python version 3.11
3. if still doesn't work add a runtime.txt in the root folder and add the python version (python-3.11.7)
4. Create a .streamlit/config.toml file:

[runner]
pythonVersion = "3.11"

Easy
