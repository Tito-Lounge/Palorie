import os
import openai
import pandas as pd
import datetime
import os

openai.api_key = os.environ['OPENAI_API_KEY']

# Input: User Input for Foods Eaten
foodString = input("List out the foods you ate: ")
instructions = 'Please create a table listing the nutritional information for the following foods: Food, Amount, Calories, Protein, Carbohydrates, Fat. Separate each column with commas. Create a new row, separated by a new line, for each food listed. Truncate the amount from the food column so that only the name of the food is written in that column. Do not include column names in the output. If a listed item is not food, do not include it in your output:'
prompt = instructions + foodString
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
generated_text = response.choices[0].text
# Output: String of generated food text formatted in CSV.

# Timestamp for the file.
timestamp = datetime.datetime.now(datetime.timezone.utc).astimezone()
timestampString = "{}-{}-{}-{}{}{}.csv".format(timestamp.year, timestamp.month, timestamp.day, timestamp.strftime("%I"), timestamp.strftime("%M"), timestamp.strftime("%S"))

rawText = open('rawtext.txt', 'w')
rawText.write(generated_text)
rawText.close()

dataframe = pd.read_csv('rawtext.txt', delimiter=',', header=None)
dataframe.columns = ['Food', 'Amount', 'Calories', 'Protein', 'Carbohydrates', 'Fat']
dataframe.to_csv("./output/" + timestampString, index=None)
print(dataframe)

os.remove('rawtext.txt')
