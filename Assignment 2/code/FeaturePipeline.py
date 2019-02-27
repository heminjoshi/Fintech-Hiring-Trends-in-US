import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import luigi
import os
import time

# Global dictionary to save top 100 words
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
            
            # Write success message to luigi output file to continue with execution of next task in the pipeline
            with self.output().open('w') as f:
                f.write("{}\n".format('ClusterAnalysis done'))

        except Exception as e:
            # Write error message to luigi output file to continue with execution of next task in the pipeline
            with self.output().open('w') as f:
                f.write("{}\n".format(e))

    def output(self):
        # Defining output target for the task
        return luigi.LocalTarget("../userlogs/logs_%s.txt" % time.strftime("%Y%m%d-%H%M%S"))
 
    
    
class Categorize(luigi.Task):
      def requires(self):
          # Execute cluster analysis before starting this task
          return [
              ClusterAnalysis()
          ]
  
      def output(self):
          # Defining output target for the task
        return luigi.LocalTarget("../userlogs/logs_%s.txt" % time.strftime("%Y%m%d-%H%M%S"))
  
      def run(self):
        try:
            # Loop through bank data dumps
            for i in range(1,13):
                try:
                    # Fetch data for current bank and store in a pandas dataframe
                    newDF = pd.read_excel('../banks_data/Sheet%d.xlsx' % i, sheet_name='Sheet1')
                    
                    # Loop through each job in the bank data dump
                    for index, row in newDF.iterrows():
                        try:

                            # Creating a dictionary to store count of words from category
                            count = dict.fromkeys(domain_dict.keys())

                            # Storing count of word occurences from each category in the current job description
                            for key in domain_dict.keys():
                                count[key] = sum(row[2].count(x) for x in domain_dict[key])
                                newDF.loc[index,key] = count[key]

                            # Compute the category which has most word occurences in the current job description 
                            max_category = max(count, key=count.get)
                            # Add the category which has most word occurences to the current job
                            newDF.loc[index, 'Domain'] = max_category

                            # Check whether the job is a fintech job and write it to the current job
                            if(max_category in ['technology','analytics','data science','cyber security']):
                                newDF.loc[index, 'Fintech/Non-Fintech'] = 'Fintech'
                            else:
                                newDF.loc[index, 'Fintech/Non-Fintech'] = 'Non-Fintech' 
                        
                        except Exception as ex:
                            print(ex)
                    
                    # Persist the job data with new columns to a new file for the current bank
                    newDF.to_excel("../deliverables/analyzed/Sheet%d_analyzed.xlsx" % i, index = False)

                    # Write success message to luigi output file to continue with execution of next task in the pipeline
                    print('done %d' % i)
                    with self.output().open('w') as f:
                        f.write("{}\n".format('done %d' % i))
                    
                except Exception as e:
                    # Write erro message to luigi output file 
                    print(e)
                    with self.output().open('w') as f:
                        f.write("{}\n".format(e))
        except Exception as exc:
                print(exc)
                # Write error message to luigi output file
                with self.output().open('w') as f:
                    f.write("{}\n".format(exc))

# Execute as a Luigi pipeline                 
if __name__ == '__main__':
    luigi.run()