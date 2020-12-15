class Solution(object):
    def findDuplicate(self, paths):
        ht = collections.defaultdict(list)
        for path in paths:
            data = path.split()
            root = data[0]
            for file in data[1:]:
                name, _, content = file.partition('(')
                ht[content[:-1]].append(root + '/' + name)
                    
        return [duplicates for duplicates in ht.values() if len(duplicates) > 1]

"""
Followups: 
* In a real file system I would either do BFS or DFS, I would use DFS if the depth is not too deep, else BFS
* We can make use of metadata such as inode or file size before we read large content, instead we can store the 
  hashcode of the file in the map
* If we do this hashing part would be most time and memory assuming
* if we want to assure there are no false positives, we can compare duplicate content chunk by chunk using check sum

"""
