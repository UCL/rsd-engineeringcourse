### "imports"

from numpy import linspace,exp,log,sqrt, array
import math
from scipy.interpolate import UnivariateSpline
from scipy.signal import lombscargle
from scipy.integrate import cumtrapz
from numpy.fft import rfft,fft,fftfreq
import csv
from StringIO import StringIO
from datetime import datetime
import requests
import matplotlib.pyplot as plt

### "load_data"

def load_sunspots():
     url_base="http://www.quandl.com/api/v1/datasets/SIDC/SUNSPOTS_A.csv"
     x=requests.get(url_base,params={'trim_start':'1700-12-31',
                                        'trim_end':'2014-01-01',
                                        'sort_order':'asc'})
     data=csv.reader(StringIO(x.text)) #Convert requests result to look 
                                       #like a file buffer before 
                                       # reading with CSV
     data.next() # Skip header row
     return [float(row[1]) for row in data]

### "InitialFigure"
spots=load_sunspots()
plt.plot(spots)
plt.savefig('spots.png')

### "naive_fft"
spectrum=rfft(spots)

### "FFT figure"
plt.figure()
plt.plot(abs(spectrum))
plt.savefig('fixed.png')

### "Series"

class Series(object):
    """Enhance NumPy N-d array with some helper functions for clarity"""
    def __init__(self, data):
        self.data=array(data)
        self.count=self.data.shape[0]
        self.start=self.data[0,0]
        self.end=self.data[-1,0]
        self.range=self.end-self.start
        self.step=self.range/self.count
        self.times=self.data[:,0]
        self.values=self.data[:,1]
        self.plot_data=[self.times,self.values]
        self.inverse_plot_data=[1.0/self.times[20:], self.values[20:]]


### "Client"

class AnalyseSunspotData(object):
    def format_date(self, date):
        date_format="%Y-%m-%d"
        return datetime.strptime(date,date_format)
    def load_data(self):
        start_date_str='1700-12-31'
        end_date_str='2014-01-01'
        self.start_date=self.format_date(start_date_str)
        end_date=self.format_date(end_date_str)
        url_base=("http://www.quandl.com/api/v1/datasets/"+
                  "SIDC/SUNSPOTS_A.csv")
        x=requests.get(url_base,params={'trim_start':start_date_str,
                                        'trim_end':end_date_str,
                                        'sort_order':'asc'})
        secs_per_year=(datetime(2014,1,1)-datetime(2013,1,1)
                ).total_seconds()
        data=csv.reader(StringIO(x.text)) #Convert requests
                                          #result to look
                                          #like a file buffer before
                                          #reading with CSV
        data.next() # Skip header row
        self.series=Series([[
                (self.format_date(row[0])-self.start_date
                    ).total_seconds()/secs_per_year
                 ,float(row[1])] for row in data])
    def __init__(self, frequency_strategy):
        self.load_data()
        self.frequency_strategy=frequency_strategy
    def frequency_data(self):
        return self.frequency_strategy.transform(self.series)

### "Naive"

class FourierNearestFrequencyStrategy(object):
    def transform(self, series):
        transformed=fft(series.values)[0:series.count/2]
        frequencies=fftfreq(series.count, series.step)[0:series.count/2]
        return Series(zip(frequencies, abs(transformed)/series.count))


### "Spline"

class FourierSplineFrequencyStrategy(object):
    def next_power_of_two(self, value):
        "Return the next power of 2 above value"
        return 2**(1+int(log(value)/log(2)))
    def transform(self, series):
        spline=UnivariateSpline(series.times, series.values)
        # Linspace will give us *evenly* spaced points in the series
        fft_count= self.next_power_of_two(series.count)
        points=linspace(series.start,series.end,fft_count)
        regular_xs=[spline(point) for point in points]
        transformed=fft(regular_xs)[0:fft_count/2]
        frequencies=fftfreq(fft_count,
                series.range/fft_count)[0:fft_count/2]
        return Series(zip(frequencies, abs(transformed)/fft_count))


### "Lomb"

class LombFrequencyStrategy(object):
    def transform(self,series):
        frequencies=array(linspace(1.0/series.range,
            0.5/series.step,series.count))
        result= lombscargle(series.times,
                series.values,2.0*math.pi*frequencies)
        return Series(zip(frequencies, sqrt(result/series.count)))


### "Declare"

fourier_model=AnalyseSunspotData(FourierSplineFrequencyStrategy())
lomb_model=AnalyseSunspotData(LombFrequencyStrategy())
nearest_model=AnalyseSunspotData(FourierNearestFrequencyStrategy())


### "Analyze"

comparison=fourier_model.frequency_data().inverse_plot_data+['r']
comparison+=lomb_model.frequency_data().inverse_plot_data+['g']
comparison+=nearest_model.frequency_data().inverse_plot_data+['b']
deviation=365*(fourier_model.series.times-linspace(
    fourier_model.series.start,
    fourier_model.series.end,
    fourier_model.series.count))

### "FinalPlots"

plt.figure()
plt.plot(*comparison)
plt.xlim(0,16)
plt.savefig('comparison.png')

plt.figure()
plt.plot(deviation)
plt.savefig('deviation.png')



