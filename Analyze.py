import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Analyzer:

    def __init__(self, filename):
        self.filename = filename
        self.table = pd.read_csv(filename)
        
    def compute_mean(self):
        return self.table['Filtered Packets'].mean()

    def compute_variance(self):
        return self.table['Filtered Packets'].var()

    def compute_CDF(self):
        sorted_data = np.sort(self.table['Filtered Packets'])
        yvals = np.arange(1,len(sorted_data)+1)/len(sorted_data)
        return yvals

    def compute_pmf(self):
        pmf, bins = np.histogram(self.table['Filtered Packets'], bins=10)
        bin_centers = 0.5*(bins[1:] + bins[:-1])
        return pmf, bin_centers
    
if __name__ == '__main__':
    print('PING h1 - h2')
    analyzer = Analyzer('data/h1pingh2.csv')
    print('Mean: ' + str(analyzer.compute_mean()))
    print('Variance: ' + str(analyzer.compute_variance()))

    print('PING h1 - h6')
    analyzer = Analyzer('data/h1pingh6.csv')
    print('Mean: ' + str(analyzer.compute_mean()))
    print('Variance: ' + str(analyzer.compute_variance()))

    print("TCP")
    analyzer = Analyzer('data/h1serverh2clientTCP.csv')
    print('Mean: ' + str(analyzer.compute_mean()))
    print('Variance: ' + str(analyzer.compute_variance()))
    yvals = analyzer.compute_CDF()
    
    plt.plot(np.sort(analyzer.table['Filtered Packets']), yvals)
    plt.title('CDF of Filtered Packets')
    plt.xlabel('Filtered Packets')
    plt.ylabel('CDF')
    plt.show()

    pmf, bin_centers = analyzer.compute_pmf()
    plt.bar(bin_centers, pmf, width=0.05)
    plt.title('PMF of Filtered Packets')
    plt.xlabel('Filtered Packets')
    plt.ylabel('PMF')
    plt.show()