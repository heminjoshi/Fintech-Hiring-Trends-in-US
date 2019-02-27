import luigi
import csv
import operator
import xlrd

#class readingJobs(luigi.Task):

#   def output(self):
#        return luigi.LocalTarget("analytics1.csv")

#    def run(self):
#        with open('final_clusters.csv') as csv_file:
#        	csv_reader = csv.reader(csv_file, delimiter=',')
#        	for row in csv_reader:
#        		self.output().write("%s\n"%(row[0]))

class Job():
	def __init__(self, title, bankName, description):
		self.title=title
		self.bankName=bankName
		self.description=description

class Cluster():
	def __init__(self, clusterName, listOfWords):
		self.clusterName=clusterName
		self.listOfWords=listOfWords

class AggData():
	def __init__(self, title, bankName, clusterDict, assignedCluster, assignedCategory):
		self.title=title
		self.bankName=bankName
		self.clusterDict=clusterDict
		self.assignedCluster=assignedCluster
		self.assignedCategory=assignedCategory



jobTitlesWithDescription = []
clusters = []
aggregatedData=[]

#for x in range(1,2):
#with open('excel2.csv') as jobs_file:
#    jobs_reader = csv.reader(jobs_file, delimiter=',')
#    for row in jobs_reader:
#    	jobTitlesWithDescription.append(Job(row[1],row[3],row[2]))

for x in range(1,13):
	loc = ("excel"+str(x)+".xlsx") 
	wb = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(0) 
	print(str(x)+" --------> "+str(sheet.nrows))
	for i in range(sheet.nrows): 
	    jobTitlesWithDescription.append(Job(sheet.cell_value(i, 1),sheet.cell_value(i, 3),sheet.cell_value(i, 2)))


#for job in jobTitlesWithDescription:
#	print(job.title)
    	
print(len(jobTitlesWithDescription))

#print("--------------------------------------------------")

#for value in jobTitlesWithDescription:
#	print(value)

for x in range(8):
	with open('cluster1.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		list_topWords=[]
		first=True
		second=True
		keyword=""
		for row in csv_reader:
			if first:
				first=False
			elif second:
				second=False
				keyword=row[x]
				print(keyword+"*****")
			else:
				list_topWords.append(row[x])
	list_topWords = list(filter(None, list_topWords))
	clusters.append(Cluster(keyword,list_topWords))

#for c in clusters:
#	print(c.clusterName)
#	print(c.listOfWords)
#	print("******************")

for job in jobTitlesWithDescription:
	listOfDesc = job.description.split(" ")
	clusterDict = {}
	for c in clusters:
		clusterDict[c.clusterName]=0
	for cluster in clusters:
		for word in cluster.listOfWords:
			for descWord in listOfDesc:
				if word in descWord:
					clusterDict[cluster.clusterName]+=1
	assignedCluster = max(clusterDict, key=clusterDict.get)
	if assignedCluster=='banking' or assignedCluster=='finance' or assignedCluster=='marketing' or assignedCluster=='management':
		assignedCategory='Finance'
	else:
		assignedCategory='FinTech'
	aggregatedData.append(AggData(job.title, job.bankName, clusterDict, assignedCluster, assignedCategory))

#for data in aggregatedData:
#	print(data.title)
#	print(data.bankName)
#	print(data.clusterDict)
#	print(data.assignedCluster)
#	print("")



with open('AggAnalysis1.csv', 'w') as f :
	spamwriter = csv.writer(f, delimiter='|')
	f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%("Title","Bank Name","Banking","Technology","Finance", "Marketing", "Analytics", "Management", "Cyber Security", "Data Science","Assigned Cluster","Assigned Category"))
	for data in aggregatedData:
		if isinstance(data.title, str):
			data.title=data.title.replace(",","|")
		f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(data.title,data.bankName,data.clusterDict["banking"],data.clusterDict["technology"],data.clusterDict["finance"],data.clusterDict["marketing"],data.clusterDict["analytics"],data.clusterDict["management"],data.clusterDict["cyber security"], data.clusterDict["data science"], data.assignedCluster, data.assignedCategory))

bankDict = {"JP Morgan":0, "Bank Of America":1, "WellsFargo":2, "CitiGroup":3, "Morgan Stanley":4, "Goldman Sachs":5,
			"US Bank":6, "American Express":7, "Charles Schwab":8, "PNC Bank":9, "BNY Mellon":10, "Capital One":11,
			"BB&T Corp":12,"State Street":13,"Suntrust Bank":14, "Discover Financials":15,"M&T Bank":16, "northern trust":17,
			"Fifth Third Bank":18, "Key Corp Bank":19, "Citizen":20, "Regions":21, "Huntington Bancshares":22, "Comerica Inc":23}

areaDict = {"technology":0,"analytics":1,"data science":2,"cyber security":3}

jobCount = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

print("*****11111*****")

for data in aggregatedData:
	if(data.assignedCategory=="FinTech"):
		jobCount[areaDict.get(data.assignedCluster)][bankDict.get(data.bankName)]+=1

print("*****22222*****")

with open('FintechTrendsAnalysis.csv', 'w') as f :
	spamwriter = csv.writer(f, delimiter='|')
	f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(" ","JP Morgan","Bank Of America", "WellsFargo","CitiGroup", "Morgan Stanley", "Goldman Sachs","US Bank", "American Express", "Charles Schwab", "PNC Bank", "BNY Mellon", "Capital One","BB&T Corp","State Street","Suntrust Bank", "Discover Financials","M&T Bank", "northern trust","Fifth Third Bank", "Key Corp Bank", "Citizen", "Regions", "Huntington Bancshares", "Comerica Inc"))
	for key,value in areaDict.items():
		f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(key,jobCount[value][0],jobCount[value][1],jobCount[value][2],jobCount[value][3],jobCount[value][4],jobCount[value][5],jobCount[value][6],jobCount[value][7],jobCount[value][8],jobCount[value][9],jobCount[value][10],jobCount[value][11],jobCount[value][12],jobCount[value][13],jobCount[value][14],jobCount[value][15],jobCount[value][16],jobCount[value][17],jobCount[value][18],jobCount[value][19],jobCount[value][20],jobCount[value][21],jobCount[value][22],jobCount[value][23])) 
	