class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        results = 0

        for i in range(len(seats)):
            if students[i] < seats[i]:
                results += seats[i] - students[i]
            elif students[i] > seats[i]:
                results += students[i] - seats[i]
        return results
                
        