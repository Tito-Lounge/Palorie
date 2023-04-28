# PalorieApp
An application by Eric Santos, Jared Ho and Ritesh Kothari designed to take a user's description of what they've eaten and utilize GPT-3 to calculate and tabulate the nutritional information.

### Test it Yourself!
If you have an OpenAI API key and want to test functionality, follow these instructions.
1. Navigate to the [OpenAI Developer Portal](https://platform.openai.com/).
2. Click on your profile icon on the top right.
3. Click 'View API keys'
4. Create a file called config.py
5. Type "api_key = '[your key here]'"

To set up a virtual environment for testing:
1. Install Python and pip on your machine.
2. Use pip to install the venv/virtualenv package using `pip install venv` or `pip install virtualenv` (whichever works).
3. Create a virtual environment folder using `python3 -m venv .[folder]` (omit the dot if you dont want the directory to be hidden).
5. Enter the virtual environment using `source [folder]/bin/activate`.
4. Install the following packages using `pip install`:
    a. openai
    b. pandas
    c. pytest
    d. django

To run the virtual server:
1. Have django installed in your virutal environment
2. Use `python(3) manage.py runserver`
