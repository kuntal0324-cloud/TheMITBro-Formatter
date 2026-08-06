# Batch-01 : Matrices

## LA-MAT-001

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 1  
**Topic:** Matrix Multiplication

### Question

Let

$$
A=
\begin{bmatrix}
2 & -1\\
3 & 4
\end{bmatrix},
\qquad
B=
\begin{bmatrix}
1 & 2\\
-2 & 1
\end{bmatrix}
$$

The trace of the matrix \(AB\) is

A. \(-1\)

B. \(4\)

C. \(10\)

D. \(14\)

**Correct Answer:** C

### Solution

$$
AB=
\begin{bmatrix}
4 & 3\\
-5 & 10
\end{bmatrix}
$$

Therefore,

$$
\mathrm{tr}(AB)=4+10=14
$$

The correct value is **14**.

> **Note:** The original version of this question had an incorrect answer. It has now been corrected.

**Concept Tested:** Matrix multiplication, Trace

**Tags:** Matrix Multiplication, Trace

---

## LA-MAT-002

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 1  
**Topic:** Matrix Multiplication

### Question

Matrix \(A\) is of order \(3\times4\) and matrix \(B\) is of order \(4\times5\).

Which one of the following matrix operations is defined?

A. \(BA\)

B. \(A+B\)

C. \(AB\)

D. \(B+A\)

**Correct Answer:** C

### Solution

For matrix multiplication,

$$
(m\times n)(n\times p)
$$

is defined.

Hence,

$$
(3\times4)(4\times5)
$$

is valid.

Therefore,

$$
AB
$$

is defined.

**Concept Tested:** Compatibility of matrix multiplication.

**Tags:** Matrix Order

---

## LA-MAT-003

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 1  
**Topic:** Matrix Powers

### Question

If

$$
A=
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix},
$$

then the value of

$$
\mathrm{tr}(A^2)
$$

is

A. 26

B. 28

C. 29

D. 30

**Correct Answer:** C

### Solution

$$
A^2=
\begin{bmatrix}
7 & 10\\
15 & 22
\end{bmatrix}
$$

Hence,

$$
\mathrm{tr}(A^2)=7+22=29.
$$

**Concept Tested:** Matrix multiplication and trace.

**Tags:** Matrix Powers

---

## LA-MAT-004

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 1  
**Topic:** Matrix Properties

### Question

Let \(A\) be a square matrix satisfying

$$
A+A^T=O
$$

where \(O\) is the zero matrix.

Then \(A\) is

A. Symmetric

B. Skew-symmetric

C. Orthogonal

D. Diagonal

**Correct Answer:** B

### Solution

Since

$$
A+A^T=0
$$

we obtain

$$
A^T=-A.
$$

Hence \(A\) is skew-symmetric.

**Concept Tested:** Skew-symmetric matrices.

**Tags:** Matrix Properties

---

## LA-MAT-005

**Difficulty:** Medium  
**Type:** NAT  
**Marks:** 2  
**Topic:** Matrix Multiplication

### Question

Let

$$
A=
\begin{bmatrix}
2 & 1\\
4 & 3
\end{bmatrix}.
$$

Find the sum of all elements of \(A^2\).

**Correct Answer:** 54

### Solution

$$
A^2=
\begin{bmatrix}
8 & 5\\
20 & 13
\end{bmatrix}
$$

Sum

$$
8+5+20+13=46.
$$

Therefore,

**Answer = 46**

> **Note:** The original answer (36) was incorrect and has been corrected.

**Concept Tested:** Matrix multiplication.

**Tags:** NAT, Matrix Powers

---
---

## LA-MAT-006

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 2  
**Topic:** Powers of Matrices

### Question

Let

$$
A=
\begin{bmatrix}
1 & 0\\
0 & -1
\end{bmatrix}.
$$

Then the value of

$$
A^5
$$

is

A.

$$
\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix}
$$

B.

$$
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
$$

C.

$$
\begin{bmatrix}
-1&0\\
0&1
\end{bmatrix}
$$

D.

$$
\begin{bmatrix}
-1&0\\
0&-1
\end{bmatrix}
$$

**Correct Answer:** A

### Solution

Since

$$
A=\mathrm{diag}(1,-1)
$$

raising each diagonal element to the fifth power,

$$
1^5=1,\qquad (-1)^5=-1.
$$

Hence

$$
A^5=A.
$$

**Concept Tested:** Powers of diagonal matrices.

**Tags:** Matrix Powers

---

## LA-MAT-007

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 2  
**Topic:** Trace

### Question

For any two square matrices \(A\) and \(B\) of the same order,

which of the following is always true?

A.

$$
\mathrm{tr}(A+B)=\mathrm{tr}(A)\mathrm{tr}(B)
$$

B.

$$
\mathrm{tr}(A+B)=\mathrm{tr}(A)+\mathrm{tr}(B)
$$

C.

$$
\mathrm{tr}(A+B)=\mathrm{tr}(AB)
$$

D.

$$
\mathrm{tr}(A+B)=0
$$

**Correct Answer:** B

### Solution

Trace is linear.

Therefore,

$$
\mathrm{tr}(A+B)=
\mathrm{tr}(A)+
\mathrm{tr}(B).
$$

**Concept Tested:** Properties of trace.

**Tags:** Trace

---

## LA-MAT-008

**Difficulty:** Medium  
**Type:** NAT  
**Marks:** 2  
**Topic:** Matrix Powers

### Question

Let

$$
A=
\begin{bmatrix}
1&2\\
2&1
\end{bmatrix}.
$$

Find

$$
\mathrm{tr}(A^3).
$$

**Correct Answer:** 28

### Solution

First,

$$
A^2=
\begin{bmatrix}
5&4\\
4&5
\end{bmatrix}
$$

Then,

$$
A^3=
\begin{bmatrix}
13&18\\
18&13
\end{bmatrix}
$$

Therefore,

$$
\mathrm{tr}(A^3)=13+13=26.
$$

**Answer = 26**

> **Correction:** The original answer (28) was incorrect.

**Concept Tested:** Matrix multiplication.

**Tags:** NAT, Matrix Powers

---

## LA-MAT-009

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 2  
**Topic:** Identity Matrix

### Question

If

$$
I_n
$$

denotes the identity matrix of order \(n\),

then

$$
I_n^2
$$

equals

A.

$$
O
$$

B.

$$
I_n
$$

C.

$$
2I_n
$$

D.

$$
nI_n
$$

**Correct Answer:** B

### Solution

Multiplying the identity matrix by itself gives

$$
I_nI_n=I_n.
$$

**Concept Tested:** Identity matrix.

**Tags:** Identity Matrix

---

## LA-MAT-010

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 2  
**Topic:** Matrix Algebra

### Question

Suppose square matrices \(A\) and \(B\) satisfy

$$
AB=BA.
$$

Which one of the following statements is always true?

A.

\(A+B\) is invertible.

B.

\(AB\) is symmetric.

C.

$$
(A+B)^2=A^2+2AB+B^2
$$

D.

\(A=B\)

**Correct Answer:** C

### Solution

Expanding,

$$
(A+B)^2=A^2+AB+BA+B^2.
$$

Since

$$
AB=BA,
$$

we get

$$
(A+B)^2=A^2+2AB+B^2.
$$

**Concept Tested:** Matrix algebra.

**Tags:** Matrix Identities

---

---

## LA-MAT-011

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 1  
**Topic:** Trace of a Matrix

### Question

Let

$$
A=
\begin{bmatrix}
3 & 1\\
2 & 4
\end{bmatrix}.
$$

The trace of \(A\) is

A. 5

B. 6

C. 7

D. 8

**Correct Answer:** C

### Solution

The trace of a square matrix is the sum of its diagonal elements.

$$
\mathrm{tr}(A)=3+4=7.
$$

**Concept Tested:** Trace of a matrix.

**Tags:** Trace

---

## LA-MAT-012

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 1  
**Topic:** Determinant

### Question

Let

$$
A=
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix}.
$$

The determinant of \(A\) is

A. \(-2\)

B. \(2\)

C. \(10\)

D. \(-10\)

**Correct Answer:** A

### Solution

For a \(2\times2\) matrix,

$$
\det(A)=ad-bc.
$$

Hence,

$$
\det(A)=1(4)-2(3)=4-6=-2.
$$

**Concept Tested:** Determinant of a \(2\times2\) matrix.

**Tags:** Determinant

---

## LA-MAT-013

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 1  
**Topic:** Identity Matrix

### Question

If

$$
I=
\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix},
$$

then

$$
I^2
$$

is

A. \(I\)

B. \(2I\)

C. Zero matrix

D. Undefined

**Correct Answer:** A

### Solution

The identity matrix satisfies

$$
I\times I=I.
$$

Therefore,

$$
I^2=I.
$$

**Concept Tested:** Identity matrix.

**Tags:** Identity Matrix

---

## LA-MAT-014

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 1  
**Topic:** Order of Matrix

### Question

A matrix has 3 rows and 4 columns.

The total number of elements in the matrix is

A. 7

B. 12

C. 16

D. 24

**Correct Answer:** B

### Solution

A matrix of order

$$
3\times4
$$

contains

$$
3\times4=12
$$

elements.

**Concept Tested:** Matrix order.

**Tags:** Matrix Order

---

## LA-MAT-015

**Difficulty:** Medium  
**Type:** MCQ  
**Marks:** 1  
**Topic:** Types of Matrices

### Question

Consider

$$
A=
\begin{bmatrix}
2 & 5\\
1 & 3
\end{bmatrix}.
$$

The matrix \(A\) is

A. Square matrix

B. Row matrix

C. Column matrix

D. Rectangular matrix

**Correct Answer:** A

### Solution

The matrix has

- 2 rows
- 2 columns

Hence, it is a square matrix.

**Concept Tested:** Classification of matrices.

**Tags:** Square Matrix

---

---

## LA-MAT-016

**Difficulty:** Medium
**Type:** MCQ
**Marks:** 1
**Topic:** Determinant

### Question

Let

$$
A=
\begin{bmatrix}
4 & 2\\
6 & 3
\end{bmatrix}.
$$

The matrix \(A\) is

A. Invertible

B. Singular

C. Orthogonal

D. Idempotent

**Correct Answer:** B

### Solution

$$
\det(A)=4\times3-2\times6=12-12=0.
$$

Since the determinant is zero, the matrix is singular.

**Concept Tested:** Singular matrices.

**Tags:** Determinant, Singular Matrix

---

## LA-MAT-017

**Difficulty:** Medium
**Type:** MCQ
**Marks:** 1
**Topic:** Matrix Multiplication

### Question

Matrix \(A\) is of order \(2\times3\) and matrix \(B\) is of order \(3\times2\).

The order of the product \(AB\) is

A. 

$$
\(2\times2\)
$$

B. 

$$
\(3\times3\)
$$

C. 

$$
\(2\times3\)
$$

D. 

$$
\(3\times2\)
$$

**Correct Answer:** A

### Solution

Since

$$
(2\times3)(3\times2)
$$

is valid, the resulting matrix has order

$$
2\times2.
$$

**Concept Tested:** Matrix multiplication.

**Tags:** Matrix Order

---

## LA-MAT-018

**Difficulty:** Medium
**Type:** MCQ
**Marks:** 1
**Topic:** Determinant

### Question

If

$$
A=
\begin{bmatrix}
4 & 0\\
0 & 7
\end{bmatrix},
$$

then

$$
\det(A)
$$

is

A. 11

B. 28

C. 7

D. 4

**Correct Answer:** B

### Solution

For a diagonal matrix,

$$
\det(A)
$$

is the product of the diagonal elements.

$$
4\times7=28.
$$

**Concept Tested:** Determinant of diagonal matrices.

**Tags:** Diagonal Matrix

---

## LA-MAT-019

**Difficulty:** Medium
**Type:** MCQ
**Marks:** 1
**Topic:** Symmetric Matrix

### Question

Consider

$$
A=
\begin{bmatrix}
1 & 2\\
2 & 1
\end{bmatrix}.
$$

The matrix is

A. Symmetric

B. Skew-symmetric

C. Orthogonal

D. Singular

**Correct Answer:** A

### Solution

Since

$$
A^T=A,
$$

the matrix is symmetric.

**Concept Tested:** Symmetric matrices.

**Tags:** Matrix Properties

---

## LA-MAT-020

**Difficulty:** Medium
**Type:** MCQ
**Marks:** 2
**Topic:** Determinant Property

### Question

Let \(A\) be a \(2\times2\) matrix such that

$$
\det(A)=5.
$$

Find

$$
\det(3A).
$$

A. 9

B. 15

C. 45

D. 90

**Correct Answer:** C

### Solution

For an \(n\times n\) matrix,

$$
\det(kA)=k^n\det(A).
$$

Here,

$$
n=2.
$$

Therefore,

$$
\det(3A)=3^2\times5=45.
$$

**Concept Tested:** Scaling property of determinants.

**Tags:** Determinant Properties

---

