import matplotlib.pyplot as plt


class Plot:

    def __init__(self,data,count):
        self.count=count
        self.l = data

    def histogram(self):
        self.dict = dict()
        for c in self.l:
            if c[0] not in self.dict:
                self.dict[c[0]] = 1
            else:
                self.dict[c[0]] += 1
        return self.dict

    def limit_count(self):
        d = self.dict
        self.result = {}
        for i in range(self.count):
            m = max(d, key=d.get)
            self.result[m] = d[m]
            d.pop(m)

    def barchart(self,period=""):
        plt.bar(list(self.result.keys()), self.result.values(), color=(0.2, 0.4, 0.6, 0.6), edgecolor='black')
        plt.title("Распределение " + str(self.count) + " самых популярных тегов статей с сайта Habr"+period, fontsize=16,
                  fontweight='bold')
        plt.xticks(list(self.result.keys()), self.result.keys(), color='blue', rotation=45, fontweight='bold', fontsize='15',
                   horizontalalignment='right')
        plt.subplots_adjust(bottom=0.50, top=0.95)
        plt.xlabel('Теги')
        plt.ylabel('Частоты')
        mng = plt.get_current_fig_manager()
        mng.window.state("zoomed")
        plt.show()



