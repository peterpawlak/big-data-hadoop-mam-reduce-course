from mrjob.job import MRJob

class MRWorldCount(MRJob):


    def mapper(self, _, line):
        yield 'chars', len(line)