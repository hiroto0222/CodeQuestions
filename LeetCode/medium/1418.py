from collections import defaultdict

class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        # tableNumber: {foodItem: counts}
        dic = defaultdict(dict)
        table = [[]]

        for curr_order in orders:
            if int(curr_order[1]) not in dic:
                dic[int(curr_order[1])][curr_order[2]] = 1
            else:
                if curr_order[2] not in dic[int(curr_order[1])]:
                    dic[int(curr_order[1])][curr_order[2]] = 1
                else:
                    dic[int(curr_order[1])][curr_order[2]] += 1

            if curr_order[2] not in table[0]:
                table[0].append(curr_order[2])
        
        table[0].sort()
        table[0].insert(0, 'Table')

        for tableNumber in sorted(dic.keys()):
            row = [str(tableNumber)]
            for foodItem in table[0][1:]:
                if foodItem in dic[tableNumber]:
                    row.append(str(dic[tableNumber][foodItem]))
                else:
                    row.append(str(0))
            table.append(row)

        return table


print(Solution().displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
