from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        resdict = {}
        for path in paths:
            pathSplit = path.split(' ')
            pathRoot = pathSplit[0]
            for i in range(1, len(pathSplit)):
                pathNameContent = pathSplit[i].split('(')
                fileName = pathNameContent[0]
                fileContent = pathNameContent[1][:len(pathNameContent[1])-1]
                try:
                    resdict[fileContent] += [pathRoot + "/" + fileName]
                except:
                    resdict[fileContent] = [pathRoot+ "/" + fileName]
        
        res = []
        for key in resdict.keys():
            temp = []
            if len(resdict[key]) > 1:
                for val in resdict[key]:
                    temp.append(val)
            res.append(temp)

        return res
    
print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]))
