import boto3
import glob
from players import *
from botocore.config import Config
import os


my_config = Config(
    region_name = 'us-east-2',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

# Document
def get_extract(file_name):
    # Read document content
    with open(file_name, 'rb') as document:
        imageBytes = bytearray(document.read())

    # Amazon Textract client
    textract = boto3.client('textract', config=my_config)

    # Call Amazon Textract
    response = textract.detect_document_text(Document={'Bytes': imageBytes})
    return convert_extract_to_array(response)

def convert_extract_to_array(extract):
    # Print detected text
    arr = []
    for item in extract["Blocks"]:
        if item["BlockType"] == "LINE":
            arr.append(item["Text"])
    return arr

def loop_it(player_scores, extract):
    idx = -1
    for line in extract:
        print(line)
        temp_idx = line_is_a_name(line, player_scores)
        if temp_idx != -1: # found a player
            idx = temp_idx
        else:
            temp_score = line_is_a_number(line)
            if(temp_score != -1 and idx != -1): # found a score AND found a player previous
                player_scores[idx].score = temp_score
                idx = -1 # reset now that we set that score

def line_is_a_number(line):
    line = line.replace(",", "")
    if line.isdigit():
        num = int(line)
        if(num == 0 or num > 100):
            return num
    return -1

def line_is_a_name(line, player_scores):
    idx = 0
    for player in player_scores:
        for n in player.names:
            if n.upper() == line.upper():
                return idx
        idx = idx + 1

    return -1


player_scores = get_players()

path = os.environ['PICTURE_PATH']

files = glob.glob(path)

for file in files:
    extract = get_extract(file)
    loop_it(player_scores, extract)

result_with_names = ""
just_results = ""
for ps in player_scores:
    result_with_names += ps.name + "," + str(ps.score) + "\n"
    just_results += str(ps.score) + "\n"

f = open("output-withnames.csv", "a")
f.write(result_with_names)
f.close()

f = open("output-justscore.csv", "a")
f.write(just_results)
f.close()

