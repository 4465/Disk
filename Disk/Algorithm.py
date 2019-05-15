import random
import copy

class Algorithm:

    def __init__(self):
        self.TRACK_MAX_COUNT = 100  # 磁道的总数
        self.TRACK_REQUEST_COUNT = 10  # 请求访问的磁道数量
        self.TRACK_START = 50
        self.SCAN_DIRECTION = 1  # 1表示向磁道号增加的方向扫描，0表示向磁道号减小的方向
        self.N_STEPSCAN = 4  # 表示请求队列被划分为长度为 N 的子队列

        self.track_request = [None] *self. TRACK_REQUEST_COUNT
        for i in range(self.TRACK_REQUEST_COUNT):
            self.track_request[i] = random.randint(0, self.TRACK_MAX_COUNT)
    # *********************先来先服务调度算法**************************/
    def FCFS(self):
        queue_FCFS = self.track_request.copy()
        queue_FCFS.insert(0, self.TRACK_START)
        return queue_FCFS


    # **********************最短寻道时间优先调度算法********************
    def findNearest(self,current, visited):
        minDis = self.TRACK_MAX_COUNT
        minIndex = -1
        for i in range(len(self.track_request)):
            if visited[i] == False:
                dis = abs(current - self.track_request[i])
                if dis < minDis:
                    minDis = dis
                    minIndex = i
        visited[minIndex] = True
        return minIndex, minDis


    def SSTF(self):
        visited = [False] * self.TRACK_REQUEST_COUNT
        queue_FCFS = []
        current = self.TRACK_START  # 起始的磁道
        for i in range(len(self.track_request) + 1):
            index, dis = self.findNearest(current,  visited)
            queue_FCFS.append(current)
            current = self.track_request[index]
        return queue_FCFS

        queue_SCAN.append(TRACK_START)
        current = TRACK_START  # **********************扫描调度算法********************


    def SCAN(self):
        queue_SCAN = []
        track_request_copy = copy.deepcopy(self.track_request)
        track_request_copy.sort()
        while track_request_copy.__len__() != 0:
            if self.SCAN_DIRECTION == 1:
                for track in track_request_copy.copy():
                    if self.TRACK_START <= track:
                        queue_SCAN.append(track)
                        track_request_copy.remove(track)
                self.SCAN_DIRECTION = 0

            if self.SCAN_DIRECTION == 0:
                track_request_copy.reverse()
                for track in track_request_copy.copy():
                    if self.TRACK_START >= track:
                        queue_SCAN.append(track)
                        current = track
                        track_request_copy.remove(track)
                self.SCAN_DIRECTION = 1
        return queue_SCAN


    # **********************循环扫描调度算法********************
    def CSCAN(self):

        queue_CSCAN = []
        queue_CSCAN.append(self.TRACK_START)
        track_request_copy = copy.deepcopy(self.track_request)
        track_request_copy.sort()
        i = 0
        is_find = False

        if self.SCAN_DIRECTION == 1:
            while i < track_request_copy.__len__():
                if (self.TRACK_START <= track_request_copy[i]) & (is_find == False):
                    index = i
                    i = 0
                    is_find = True
                if is_find == True:
                    queue_CSCAN.append(track_request_copy[index % self.TRACK_REQUEST_COUNT])
                    index += 1
                i += 1

        if self.SCAN_DIRECTION == 0:
            track_request_copy.reverse()
            while i < track_request_copy.__len__():
                if (self.TRACK_START >= track_request_copy[i]) & (is_find == False):
                    index = i
                    i = 0
                    is_find = True
                if is_find == True:
                    queue_CSCAN.append(track_request_copy[index % self.TRACK_REQUEST_COUNT])
                    index += 1
                    current = track_request_copy[index % self.TRACK_REQUEST_COUNT]
                i += 1

        return queue_CSCAN


    # ****************** NStepSCAN算法 ************************
    def NStepSCAN(self):
        queue_NStepSCAN = []
        queue_NStepSCAN.append(self.TRACK_START)
        swap_track_request = []
        Count = 0
        for i in range(self.TRACK_REQUEST_COUNT):  # 将队列进行划分成长度为N_STEPSCAN的队列
            # print(track_request[i])
            if i == self.TRACK_REQUEST_COUNT - 1:
                swap_track_request.append(self.track_request[i])
                sub_queue_NstepQueue = self.SCAN(swap_track_request)
                sub_queue_NstepQueue.remove(self.TRACK_START)
                print('子序列为')
                print(sub_queue_NstepQueue)
                queue_NStepSCAN += sub_queue_NstepQueue
                break
            if Count < self.N_STEPSCAN:
                # print(track_request)
                swap_track_request.append(self.track_request[i])
                # print(swap_track_request)
            else:
                sub_queue_NstepQueue = self.SCAN(swap_track_request)
                sub_queue_NstepQueue.remove(self.TRACK_START)
                print('子序列为')
                print(sub_queue_NstepQueue)
                queue_NStepSCAN += sub_queue_NstepQueue
                swap_track_request.clear()
                swap_track_request.append(self.track_request[i])
                Count = 0
            Count += 1
        return queue_NStepSCAN


    # def caculate(self,queue):
    #     print('访问的磁道序列为: ', end='')
    #     print(queue)
    #     sum_gap = sum([(abs(queue[i] - queue[i - 1])) for i in range(1, len(queue))])
    #     print('移动的磁道数为：%d' % sum_gap)
    #     print('平均移动的磁道数为：%.2f' % (sum_gap / TRACK_REQUEST_COUNT))
    #     print("")




    # if __name__ == '__main__':
    #
    #
    #     print('每次生成的磁道序列是随机的，对于不同的序列算法的算法的性能是不一样的，'
    #           '通过多次比较观察结果，SSTF是算法中移动的磁道数最少的')
    #
    #     print("TRACK SEQUECE:    ")
    #     print(track_request)
    #     print('')
    #
    #     print("FCFS:    ")
    #     caculate(FCFS(track_request))
    #
    #     print("SSTF:    ")
    #     caculate(SSTF(track_request))
    #
    #     print("SCAN:    ")
    #     caculate(SCAN(track_request))
    #
    #     print("CSCAN:   ")
    #     caculate(CSCAN(track_request))
    #
    #     print("NStepSCAN:   ")
    #     caculate(NStepSCAN(track_request))
    #
    #
