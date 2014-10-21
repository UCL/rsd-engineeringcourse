### "paths"
from os.path import join, dirname, abspath
# Load the data file from session 1
datapath=join(dirname(dirname(dirname(abspath(__file__)))),
              'session01', 'data', 'inflammation-01.csv')
newpath=join(dirname(__file__), 'midvals.yaml')

### "files"
source = open(datapath)
import csv
reader = csv.reader(source)
midvals = [row[len(row)/2] for row in reader]
print midvals
source.close()

### "context"
import yaml
with open(newpath, 'w') as yamlfile:
    yaml.dump(midvals, yamlfile)

