class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        res = []
        
        n = len(series1)
        m = len(series2)
        i = 0
        j = 0

        while (i < n or j < m):

            current_time = -1

            if(j == m or (i < n and series1[i][0] < series2[j][0])):
                current_time = series1[i][0]
            elif(i == n or (j < m and series2[j][0] < series1[i][0])):
                current_time = series2[j][0]
            else:
                current_time = series1[i][0]

            val1 = -1
            val2 = -1

            if(i<n):
                val1 = series1[i][1]
                if(current_time == series1[i][0]):
                    i += 1
            else:
                val1 = 0

            if(j<m):
                val2 = series2[j][1]
                if(current_time == series2[j][0]):
                    j += 1
            else:
                val2 = 0

            res.append([current_time,val1+val2])
        return res