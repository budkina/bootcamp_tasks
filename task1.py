def suffix_array(s):
    return [rank for suffix, rank in sorted((s[i:], i) for i in range(len(s)))]

class FMIndex(object):
#F-first BWM column, L-last BWM column, tally - tally matrix, sa - offset of each suffix
    def __init__(self, s):
        s+='$'
        self.unique_chars=sorted(list(set(s)))
        self.char_count=dict.fromkeys(self.unique_chars, 0)
        self.tally=[]
        self.F=[]
        self.L=[]
        self.sa=suffix_array(s)
        for offset in self.sa:
            first=s[offset]
            last=s[offset-1]
            self.F.append(first)
            self.L.append(last)
            self.char_count[last]+=1
            self.tally.append(self.char_count.copy())
    
    #get first row index for char ch in F column of BW matrix
    def get_bwm_row_index(self,ch):
        n_row=0
        for unique_char in self.unique_chars:
            if unique_char==ch: break
            n_row+=self.char_count[unique_char]
        return n_row     
    
    #return list of offsets: [0..len s-1]
    def search(self,t):
        if not t: return []
        last_char=t[-1]
        if last_char not in self.char_count: return []
        last_char_count=self.char_count[last_char]    
        n_row=self.get_bwm_row_index(last_char)        
        next_char_ranks = [(last_char,i) for i in range(last_char_count)]
        
        for ch in reversed(t):
            current_char_ranks = [p for p in next_char_ranks if p[0]==ch] 
            next_char_ranks=[]
            
            for char,rank in current_char_ranks:       
                n_row=self.get_bwm_row_index(char)
                prev_char=self.L[n_row+rank]
                prev_rank= self.tally[n_row+rank][prev_char]-1                
                next_char_ranks.append((prev_char,prev_rank))
                
        offsets=[]     
        for char,rank in current_char_ranks:
            n_row=self.get_bwm_row_index(char)
            offsets.append(self.sa[n_row+rank])
        
        return sorted(offsets)

ex1_string='abcabcaaabbbaaaaaaaa'
ex1_substring='aa'
print("Search ",ex1_substring, " in ", ex1_string)
ex1 = FMIndex(ex1_string)
print(ex1.search(ex1_substring))

ex2_string='GATATATGCATATACTT'
ex2_substring='ATAT'
print("Search ",ex2_substring, " in ", ex2_string)
ex2 = FMIndex(ex2_string)
print(ex2.search(ex2_substring))