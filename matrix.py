from __future__ import annotations


class Matrix:
    def __init__(self, default_rows=[]):
        self.rows = default_rows

    def print(self):
        for row in self.rows:
            print(' '.join(map(str, row)))

    def multiply_constant(self, constant):
        for i in range(len(self.rows)):
            self.rows[i] = list(map(lambda i: i * constant, self.rows[i]))

    @property
    def row(self):
        return len(self.rows)
    
    @property
    def col(self):
        return len(self.rows[0])
    
    def add(self, another: Matrix):
        for i in range(self.row):
            for j in range(self.col):
                self.rows[i][j] = self.rows[i][j] + another.rows[i][j]

    def minus(self, another: Matrix):
        for i in range(self.row):
            for j in range(self.col):
                self.rows[i][j] = self.rows[i][j] - another.rows[i][j]

    def multiply(self, another: Matrix):
        rows = []
        for i in range(self.row):
            row = []
            for j in range(another.col):
                val = 0
                for k in range(self.col):
                    val += (self.rows[i][k] * another.rows[k][j])
                row.append(val)
            rows.append(row)

        self.rows = rows

    def divide(self, another: Matrix):
        rows = []
        for i in range(self.row):
            row = []
            for j in range(another.col):
                val = 0
                for k in range(self.col):
                    val += (self.rows[i][k] // another.rows[k][j])
                row.append(val)
            rows.append(row)

        self.rows = rows

    def determinant(self):
        determinant = 0
        for i in range(self.col):
            val = 1
            for j in range(self.row):
                val *= self.rows[i][(i + j) % self.col]
            determinant += val

        for i in range(self.row-1, -1, -1):
            val = 1
            for j in range(self.row):
                val *= self.rows[i][(i - j) % self.col]
            determinant -= val
        
        return determinant
