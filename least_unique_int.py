class Solution:

    def __init__(self, arr, k):

         self.arr = arr
         self.k = k

    def findLeastNumOfUniqueInts(self):

        # Make a dictionary that tracks count of unique elements
        uniques = {}
        for i in self.arr:
            if uniques.get(i, 'Not Found') == 'Not Found':
                uniques[i]=0
            uniques[i]+=1

        # Sort dictionary as per values (smallest to largest)
        sorted_list = sorted(uniques.items(), key = lambda item: item[1])

        # Convert sorted_list which is a list of tuples to list of lists
        # Since tuple are immutable
        temp = []
        for i in sorted_list:
            temp.append(list(i))

        # Remove k elements
        for i in temp:
            if self.k > 0:
                self.k -= 1
                i[1] -= 1
                continue
            break

        # Count unique non-zero elements
        counter = 0
        for i in temp:
            if i[1] != 0:
                counter += 1

        return counter, temp

# Test Cases
arr = [4,3,1,1,3,3,2]
k = 3

arr_1 = [5, 5, 4]
k_1 = 1

ins_1 = Solution(arr, k)
ins_2 = Solution(arr_1, k_1)

print(ins_1.findLeastNumOfUniqueInts())
print(ins_2.findLeastNumOfUniqueInts())
