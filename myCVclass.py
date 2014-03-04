# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import math
import numpy

class CustomCV(object):
    def __init__(self, ids, n_folds=3):
        """Pass an array of phenomenon ids"""
        self.ids = ids
        self.n_folds = n_folds
        self.distinct_ids=list(set(ids))
    
        self.index1 = math.ceil(len(A)/self.n_folds)
        self.indexes1=range(n_folds+1)
        
        for a in range(self.n_folds+1):
            if a != (self.n_folds-2):
                ind1=(a+1)*self.index1
                while (self.ids[ind1+1]==self.ids[ind1]):
                    ind1 += 1
                self.indexes1[a] = ind1
            elif a==(self.n_folds-2):
                self.indexes1[a]=len(self.ids)-1
                
    def __iter__(self):
        for i in range(self.n_folds):
            i1=self.indexes1[(n_folds)-i-1]
            i2=self.indexes1[(n_folds)-i]
            train = np.ones(len(self.ids)).astype(int)
            train[i1:i2]=0
            test = np.logical_not(train)
            yield np.where(train)[0], np.where(test)[0]

# <codecell>

A=['a', 'a' ,'a' ,'a' ,'b' ,'b' ,'b' ,'c' ,'c' ,'c' ,'c' ,'c' ,'d' ,'d' ,'d' ,'d' ,'d' ,'d', 'e', 'e', 'e', 'e', 'e', 'e', 'e']

# <codecell>

B=customCV()

