import pandas as pandas

dataTrain = pandas.read_csv("TrainsetTugas1ML.csv")
dataTest = pandas.read_csv("TestsetTugas1ML.csv")
hasilAkhir = []
dataHasil = {}
data_income = []
dataRow = dataTest.iterrows()
dataTrainColumn = dataTrain.columns[1:-1]

def finalOutput(hasil, fileName):
	pandas.DataFrame(hasil).to_csv(fileName, index=False, header=False)    

def incomeLoop(paramData):
	return dataTrain.groupby(paramData)

def groupJenisData(jenisData):
	return kelasdata.groupby(jenisData)  

def probIncome(x):    
	for data in x:
		dataCount = dataTrain.count()[8]
		dataLoopIncome = data / dataCount
		data_income.append(dataLoopIncome)
	return data_income

objProbIncome = pandas.DataFrame({ 
		"incomeData": dataTrain['income'].value_counts().index, 
		"probData": probIncome(dataTrain['income'].value_counts())
	})

for key, nilai in dataRow:
	incomeData = []
	for jenis, kelasdata in incomeLoop("income"):
		objKelasDataEmpty = {jenis: {}}
		dataHasil.update(objKelasDataEmpty)
		for jenisData in dataTrainColumn:
			objJenisDataEmpty = {jenisData: {}}
			dataHasil[jenis].update(objJenisDataEmpty)
			for x, y in groupJenisData(jenisData):
				dataHasil[jenis][jenisData].update({ 
					x: len(y) / len(kelasdata) 
				})

	for jenisDataTrain, nilaiData in incomeLoop("income"):
		for dataKey in dataTrainColumn:
			dataJenisIndex = dataHasil[jenisDataTrain][dataKey][nilai[dataKey]]
			a = 1
			a = a * dataJenisIndex
		calcData = objProbIncome.loc[objProbIncome["incomeData"] == jenisDataTrain].probData.values
		hasilCalc = a * calcData
		incomeData.append([hasilCalc, jenisDataTrain])

	hasilAkhir.append(incomeData[0][1]) if incomeData[1][0] < incomeData[0][0] else hasilAkhir.append(incomeData[1][1])
	finalOutput(hasilAkhir, "TebakanTugas1ML.csv")