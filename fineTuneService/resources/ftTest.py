from fineTuneService.ftConfiguration.ftTrainConfig import train_filepath, train_filename

from pathlib import Path

data_folder = Path(train_filepath)
print(data_folder)

file_to_open = data_folder / train_filename
print(file_to_open)

f = open(file_to_open)

print(f.read())

