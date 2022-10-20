import random
from abc import abstractmethod

class Acid:
    @abstractmethod
    def __init__(self, string):
        self.coding_seq = string
    
    @abstractmethod
    def __getitem__(self, item):
        if 0 <= item < len(self.coding_seq):
            return self.coding_seq[item]
        else:
            raise IndexError("Неверный индекс")
    
    @abstractmethod
    def complementarity_chain(self):
        pass
    
    @abstractmethod
    def __add__(self, other):
        if not isinstance(other, Acid):
            raise Exception('Second sequence must be from type Acid')
        
        return self.coding_seq + other.coding_seq
    
    @abstractmethod
    def __mul__(self, other):
        if not isinstance(other, Acid):
            raise Exception('Second sequence must be from type Acid')
        
        new_seq = ''
        for i in range(min(len(self.coding_seq), len(other.coding_seq))):
            new_seq += random.choice([self.coding_seq[i], other.coding_seq[i]])
        if len(self.coding_seq) > len(other.coding_seq):
            new_seq += self.coding_seq[len(other.coding_seq):]
        else:
            new_seq += other.coding_seq[len(self.coding_seq):]
        
        return new_seq
    
    @abstractmethod
    def __eq__(self, other):
        if not isinstance(other, Acid):
            raise Exception('Second sequence must be from type Acid')
        
        if self.coding_seq == other.coding_seq:
            return 'последовательности совпадают'
        return 'последовательности не совпадают'
    
    @abstractmethod
    def __repr__(self):
        pass

    

class DNA(Acid):
    
    def __init__(self, string):
        nitr_bases = set(['A', 'T', 'G', 'C'])
        complementarity_rule = {
                                'A': 'T',
                                'T' : 'A',
                                'G' : 'C',
                                'C' : 'G'
                                }
        super().__init__(string)
        if not(set(self.coding_seq) <= nitr_bases):
            raise Exception('Mistake(s) in input data')
    
    def __getitem__(self, item):
        base = super().__getitem__(item)
        self.complementarity_chain()
        return base, self.matrix_seq[item]
    
    def complementarity_chain(self):
        complementarity_rule = {
                                'A': 'T',
                                'T' : 'A',
                                'G' : 'C',
                                'C' : 'G'
                                }
        matrix_seq = ''
        for base in self.coding_seq:
            matrix_seq += complementarity_rule[base]
        self.matrix_seq = matrix_seq[::-1]

    def __repr__(self):
        if len(self.coding_seq) > 40:
            return f'Coding sequence: {self.coding_seq[:20]} ... {self.coding_seq[-20:]}\nMatrix sequence: {self.matrix_seq[:20]} ... {self.matrix_seq[-20:]}'
        
        return f'Coding sequence: {self.coding_seq}\nMatrix sequence: {self.matrix_seq}'



class RNA(Acid):

    def __init__(self, string):
        nitr_bases = set(['A', 'U', 'G', 'C'])
        complementarity_rule = {
                                'A': 'U',
                                'U' : 'A',
                                'G' : 'C',
                                'C' : 'G'
                                }
        super().__init__(string)
        if not(set(self.coding_seq) <= nitr_bases):
            raise Exception('Mistake(s) in input data')
    
    def complementarity_chain(self):
        complementarity_dna_rule = {
                                    'A': 'T',
                                    'U' : 'A',
                                    'G' : 'C',
                                    'C' : 'G'
                                    }
        dna_seq = ''
        for base in self.coding_seq:
            dna_seq += complementarity_dna_rule[base]
        return dna_seq[::-1]
    
    def __repr__(self):
        if len(self.coding_seq) > 40:
            return f'Coding sequence: {self.coding_seq[:20]} ... {self.coding_seq[-20:]}'
        
        return f'Coding sequence: {self.coding_seq}'