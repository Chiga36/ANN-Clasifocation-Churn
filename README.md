# ANN-Clasifocation-Churn
while deploying your streamlit app with an older version of python,tensorflow: follow this instructions:
1. in requirement.txt please mention streamlit : streamlit>=1.8.0, h5py==3.8.0
2. while deploying, it will show error, go to manage app at bottom left corner of the "oops message" and at the end there will be 3 dots click on that -> settings -> select python version 3.11
3. if still doesn't work add a runtime.txt in the root folder and add the python version (python-3.11.7)
4. Create a .streamlit/config.toml file:

[runner]
pythonVersion = "3.11"

Easy

pictoral representation
1. ![image](https://github.com/user-attachments/assets/628a5869-4e65-4b74-8da0-f384782be0f9)
2. ![image](https://github.com/user-attachments/assets/243b1592-95a4-4635-834c-b7e8f81998ce)
3. ![image](https://github.com/user-attachments/assets/c2c54839-827a-4bc5-83c9-4d928da08d09)
4. ![image](https://github.com/user-attachments/assets/de059e33-0fa6-4868-920a-a28d43505797)
