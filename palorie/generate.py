import os
import openai
import pandas as pd
import datetime
import config

def generateCSV(foodString):

  # Put API key in a config.py file.
  openai.api_key = config.api_key
  if openai.api_key is None:
    return 'ERR No API key found'
  else:
    categoryInstruction = 'Please create a table listing the nutritional information for the following foods: Food, Amount, Calories, Protein, Carbohydrates, Saturated Fat, Trans Fat, Polyunsaturated Fat, Monounsaturated Fat.'
    formatInstruction = ' Separate each column with commas. Create a new row, separated by a new line, for each food listed. Truncate the amount from the food column so that only the name of the food is written in that column. Do not include column names in the output.'
    exceptionInstruction = ' If a listed item is not food, output nothing at all: '
    prompt = categoryInstruction + formatInstruction + exceptionInstruction + foodString
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.3,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    generated_text = response.choices[0].text

    # Timestamp for the file.
    timestamp = datetime.datetime.now(datetime.timezone.utc).astimezone()
    timestampString = "{}-{}-{}-{}{}{}.csv".format(timestamp.year, timestamp.month, timestamp.day, timestamp.strftime("%I"), timestamp.strftime("%M"), timestamp.strftime("%S"))

    # Create a raw text file for the output
    rawText = open('rawtext.txt', 'w')
    rawText.write(generated_text)
    rawText.close()

    # Convert text file to CSV using pandas and create it.
    dataframe = pd.read_csv('rawtext.txt', delimiter=',', header=None)
    dataframe.columns = ['Food', 'Amount', 'Calories', 'Protein', 'Carbohydrates', 'Saturated Fat', 'Trans Fat', 'Polyunsaturated Fat', 'Monounsaturated Fat']
    dataframe.to_csv("./output/" + timestampString, index=None)
    print(dataframe)

    # Clean up and delete the raw text file. 
    os.remove('rawtext.txt')
    return 'Successfully generated!'
