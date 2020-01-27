from Day import *

class CSV:
    def __init__(self,data):
        self.tags=list(set(map(lambda x:x[0], data)))
        self.head=[]

    def group_by_month(self, data):
        self.head = [["Тег"] + month1]
        self.W=[]
        for tag in self.tags:
            w = [tag]
            for m in month:
                w.append(count(data, tag, m_number(m)))
            self.W.append(w)
        return self.W

    def histogr(self,dictdata):
        self.head = [["Тег","Частота"]]
        li = sorted(dictdata, key=dictdata.get, reverse=True)
        l = []
        for key in li:
            l.append([key, dictdata[key]])
        return l

    def write(self, W,file):
        W=self.head+W
        for w in W:
            for i in range(0, len(w)):
                w[i] = str(w[i])
            w.append("\n")

        with open(file, 'w') as output_file:
            for w in W:
                string_w = ';'.join(w)
                output_file.write(string_w)


