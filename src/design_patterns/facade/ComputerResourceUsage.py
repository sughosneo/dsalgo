from CPUUsage import *
from DiskUsage import *
from MemoryUsage import *

class ComputerResourceUsage:

    def usage(self):

        DiskUsage().diskUsage()
        CPUUsage().cpuUsage()
        MemoryUsage().memoryUsage()
        


