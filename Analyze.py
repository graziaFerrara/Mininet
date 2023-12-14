import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Analyzer:

    def __init__(self, filename, col_header_name):
        """
        filename: name of the file to be analyzed
        col_header_name: name of the column to be analyzed
        
        table: pandas dataframe of the file
        """
        self.__filename = filename
        self.__col_header_name = col_header_name
    
        self.table = pd.read_csv(self.__filename)

    def set_col_header_name(self, col_header_name):
        self.__col_header_name = col_header_name

    def get_col_header_name(self):
        return self.__col_header_name
    
    def set_filename(self, filename):
        self.__filename = filename

    def get_filename(self):
        return self.__filename
        
    def compute_mean(self):
        return self.table[self.__col_header_name].mean()

    def compute_variance(self):
        return self.table[self.__col_header_name].var()

    def compute_CDF(self):
        sorted_data = np.sort(self.table[self.__col_header_name])
        yvals = np.arange(1,len(sorted_data)+1)/len(sorted_data)
        return yvals
    
    def compute_plot_CDF(self, title, xlabel, ylabel):
        yvals = self.compute_CDF()
        plt.plot(np.sort(analyzer.table[self.__col_header_name]), yvals)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        return plt

    def compute_pmf(self):
        pmf, bins = np.histogram(self.table[self.__col_header_name], bins=10)
        bin_centers = 0.5*(bins[1:] + bins[:-1])
        return pmf, bin_centers
    
    def compute_plot_pmf(self, title, xlabel, ylabel):
        pmf, bin_centers = self.compute_pmf()
        plt.bar(bin_centers, pmf, width=0.05)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        return plt
    
    def compute_pdf(self):
        pdf, bins = np.histogram(self.table[self.__col_header_name], bins=10, density=True)
        bin_centers = 0.5*(bins[1:] + bins[:-1])
        return pdf, bin_centers
    
    def compute_plot_pdf(self, title, xlabel, ylabel):
        pdf, bin_centers = self.compute_pdf()
        plt.bar(bin_centers, pdf, width=0.05)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        return plt

if __name__ == '__main__':

    print('PING h1 - h2')
    analyzer = Analyzer('data/h1pingh2.csv', 'Filtered Packets')
    print('Mean: ' + str(analyzer.compute_mean()))
    print('Variance: ' + str(analyzer.compute_variance()))

    print('PING h1 - h6')
    analyzer = Analyzer('data/h1pingh6.csv', 'Filtered Packets')
    print('Mean: ' + str(analyzer.compute_mean()))
    print('Variance: ' + str(analyzer.compute_variance()))

    print("TCP")
    analyzer = Analyzer('data/h1serverh2clientTCP.csv', 'Filtered Packets')
    print('Mean: ' + str(analyzer.compute_mean()))
    print('Variance: ' + str(analyzer.compute_variance()))
    yvals = analyzer.compute_CDF()
    
    plt = analyzer.compute_plot_CDF('CDF of Filtered Packets', 'Filtered Packets', 'CDF')
    plt.show()

    plt = analyzer.compute_plot_pmf('PMF of Filtered Packets', 'Filtered Packets', 'PMF')
    plt.show()