import csv
import os

def remove():
	os.makedirs('./Headless Csv', exist_ok=True)
	for i in os.listdir('./Csv Files'):
		if i.endswith('.csv'):
			print('Removing Header from %s...' % i)
			csvFile = open(os.path.join('.', 'Csv Files', i), 'r')
			csvReader = csv.reader(csvFile)
			csvData = list(csvReader)
			csvFile.close()
			newCsvFile = open(os.path.join('.', 'Headless Csv', i), 'w', newline='')
			csvWriter = csv.writer(newCsvFile)
			for j in range(len(csvData)-1):
				csvWriter.writerow(csvData[j+1])
			newCsvFile.close()

remove()
