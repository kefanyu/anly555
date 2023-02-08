#!/usr/bin/env python
# coding: utf-8

# In[75]:


class Matrix:
    def __init__(self, dimension):
        
        self.dimension = dimension  # define the dimension of matrix
        self.row = len(dimension)  # number of row
        self.column = len(dimension[0])  # number of column
                
                
    def __add__(self,other):
        """Return sum of two matrices."""
        if self.row != other.row and other.column != other.column:  # check for same length
            raise ValueError('dimensions must agree')
            
        result = [[0] * self.column for i in range(self.row)]  # initialize the target matrix
        for i in range(self.row):  
            for j in range(self.column):
                result[i][j] = self.dimension[i][j] + other.dimension[i][j]  # summation
        return result

    def __mul__(self,other):
        """Return product of two matrices."""
        
        if self.row != other.row and other.column != other.column:  
        # check if the length and classes are equal
            raise ValueError('dimensions must agree')
            
        result = [[0] * self.column for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.column):
                result[i][j] = self.dimension[i][j] * other.dimension[i][j]  # have the multiplication elementwisely
        
        for k in range(self.row):
            result[k] = sum(result[k])  # sum each row
            
        return sum(result)  # sum the whole matrix


# In[89]:


class Vector(Matrix):
    def outer(self,other):  # outer product
        """return outer product of matrices."""
        result = [[0] * other.column for i in range(self.row)]
        for i in range(self.row):
            for j in range(other.column):
                for k in range(other.row):
                    result[i][j] = self.dimension[i][k] * other.dimension[k][j]  # matrix multiplication with row multipliy with column
        return result


# In[90]:


if __name__ == '__main__':
  
    A = Matrix([[1,2,3], [1,1,1], [2,3,4]])
    
    print(A+A)
    print(A*A)
    
    #B = Vector([3,2,1],[6,6,6],[1,1,1])
    B = Vector([[2,3,1],[1,1,1]])
    C = Vector([[1,1],[4,2],[3,6]])
    print(Vector.outer(B,C))
    
    
    


# In[ ]:




