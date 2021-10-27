import random 
class polinucleo_chain:
    def __str__(self):
        raise NotImplemented
    
    def __repr__(self):
        raise NotImplemented
    
    def return_index(self):
        raise NotImplemented
    
    def __add__(self, other):
        raise NotImplemented
    
    def __mul__(self, other):
        raise NotImplemented
    
    def __eq__(self, other):
        raise NotImplemented
class RNA(polinucleo_chain):
    def __init__(self, sequence):
        #check = lambda s: all(x in bases_of_RNA for x in s)
        control = lambda f: all(x in RNA_bases for x in f)    
        if  control(sequence):
            self.sequence = sequence
        else: 
            raise Exception
        self.compl_sequence1 = ''
        self.compl_sequence2 = ''
        self.mul_sequence = ''
    
    def return_index(self, index):
        return f'{self.sequence[index]}'
    
    def __add__(self, other):
        return RNA(self.sequence + other.sequence)
    
    def complimentary_sequences(self):
        for i in self.sequence:
            self.compl_sequence1 += dict_of_RNA_to_DNA[i]
            if i == 'U':
                self.compl_sequence2 += 'T'
            else:
                self.compl_sequence2 += i
        return [self.compl_sequence1, self.compl_sequence2]
    
    def __mul__(self, other):
        for i in range(min(len(self.sequence), len(other.sequence))):
            p = random.choice([True, False])
            if p:
                self.mul_sequence += self.sequence[i]
            else:
                self.mul_sequence += other.sequence[i]
        if len(self.sequence) >= len(other.sequence):
            return RNA(self.mul_sequence + self.sequence[len(other.sequence) : len(self.sequence)])
        else:
            return RNA(self.mul_sequence + other.sequence[len(self.sequence) : len(other.sequence)])
    
    def __eq__(self, other):
        return self.sequence == other.sequence
    
    def __str__(self):
        return f'{self.sequence}'
    
    def __repr__(self):
        return f'RNA({self.sequence})'

class DNA(polinucleo_chain):
    def __init__(self, sequence):  
        self.sequence = ['', '']
        control = lambda f: all(x in DNA_bases for x in f)      
        if  control(sequence):
            for j in sequence:
                self.sequence[0] += j
                self.sequence[1] += dict_of_DNA[j]
        else: 
            raise Exception
        self.mul_sequence = ''
        self.mul_compl_sequence = ''
    
    def return_index(self, index):
        return [self.sequence[0][index], self.sequence[1][index]]
    
    def __add__(self, other):
        return DNA(self.sequence[0] + other.sequence[0])
    
    def __mul__(self, other):
        for i in range(min(len(self.sequence[0]), len(other.sequence[0]))):
            p = random.choice([True, False])
            if p:
                self.mul_sequence += self.sequence[0][i]
                
            else:
                self.mul_sequence += other.sequence[0][i]
              
        if len(self.sequence[0]) >= len(other.sequence[0]):
            return DNA(self.mul_sequence + self.sequence[0][len(other.sequence[0]) : len(self.sequence[0])])
        else:
            return DNA(self.mul_sequence + other.sequence[0][len(self.sequence[0]) : len(other.sequence[0])])
    
    def __eq__(self, other):
        return self.sequence[0] == other.sequence[0] and self.sequence[1] == other.sequence[1] 
    
    def __str__(self):
        return f'{self.sequence}'
    
    def __repr__(self):
        return f'DNA({self.sequence})'
            
RNA_bases = ['A', 'U', 'G', 'C']
DNA_bases = ['T', 'A', 'C', 'G']
dict_of_RNA_to_DNA = {'A' : 'T', 'U' : 'A', 'G' : 'C', 'C' : 'G'}
dict_of_DNA = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
             
    


if __name__== '__main__':
    sequence1_RNA = RNA('GGG')
    sequence2_RNA = RNA('UGCAU')
    
    sequence_sum_RNA = sequence1_RNA + sequence2_RNA
    sequence_mul_RNA = sequence1_RNA * sequence2_RNA
    
    print(sequence1_RNA.return_index(2))
    
    print(sequence1_RNA)
    print(repr(sequence2_RNA))
    
    print(RNA.complimentary_sequences(sequence1_RNA))
    
    print(sequence_sum_RNA)
    print(sequence_mul_RNA)
    
    print(sequence1_RNA == sequence_mul_RNA) 
    
    print()
    
    sequence1_DNA = DNA('ATATA')
    sequence2_DNA = DNA('GACA')
    
    sequence_sum_DNA = sequence1_DNA + sequence2_DNA
    sequence_mul_DNA  = sequence2_DNA * sequence1_DNA
    
    print(sequence2_DNA.return_index(2))
    
    print(sequence2_DNA)
    print(repr(sequence1_DNA))
    
    print(sequence_sum_DNA)
    print(sequence_mul_DNA) 
    
    print(sequence_sum_DNA == sequence_mul_DNA + sequence2_DNA)