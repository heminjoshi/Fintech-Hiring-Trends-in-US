import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import luigi
import os
import time

domain_dict = {}

class ClusterAnalysis(luigi.Task):

    def requires(self):
        return []

    def run(self):
        try: 
            # Read the MS Excel file of top 100 keywords
            df = pd.read_excel('../deliverables/final_clusters.xlsx', sheet_name='Sheet1')
            
            # Forming Dictionary and dropping 'nan' strings
            for key in list(df):
                domain_dict[key] = [value for value in df[key] if str(value) != 'nan']
            
            with self.output().open('w') as f:
                f.write("{}\n".format('ClusterAnalysis done'))
        except Exception as e:
            with self.output().open('w') as f:
                f.write("{}\n".format(e))
    def output(self):
        return luigi.LocalTarget("../userlogs/logs_%s.txt" % time.strftime("%Y%m%d-%H%M%S"))
 
    
    
class Categorize(luigi.Task):
      def requires(self):
          return [
              ClusterAnalysis()
          ]
  
      def output(self):
        return luigi.LocalTarget("../userlogs/logs_%s.txt" % time.strftime("%Y%m%d-%H%M%S"))
  
      def run(self):
        try:
            for i in range(1,13):
                try:
                    newDF = pd.read_excel('../banks_data/Sheet%d.xlsx' % i, sheet_name='Sheet1')
                    for index, row in newDF.iterrows():
                        try:
                            count = dict.fromkeys(domain_dict.keys())
                            for key in domain_dict.keys():
                                count[key] = sum(row[2].count(x) for x in domain_dict[key])
                                newDF.loc[index,key] = count[key]
                            max_category = max(count, key=count.get)
                            newDF.loc[index, 'Domain'] = max_category
                            if(max_category in ['technology','analytics','data science','cyber security']):
                                newDF.loc[index, 'Fintech/Non-Fintech'] = 'Fintech'
                            else:
                                newDF.loc[index, 'Fintech/Non-Fintech'] = 'Non-Fintech' 
                        
                        except Exception as ex:
                            print(ex)
                    newDF.to_excel("../deliverables/analyzed/Sheet%d_analyzed.xlsx" % i, index = False)
                    print('done %d' % i)
                    with self.output().open('w') as f:
                        f.write("{}\n".format('done %d' % i))
                    
                except Exception as e:
                    print(e)
                    with self.output().open('w') as f:
                        f.write("{}\n".format(e))
        except Exception as exc:
                print(exc)
                with self.output().open('w') as f:
                    f.write("{}\n".format(exc))

                 
if __name__ == '__main__':
    luigi.run()