from testbook import testbook
import numpy as np

def test_filling_matrix():
    with testbook('6_filling_matrix.ipynb', execute=True) as tb:
        A72 = np.array([[tb.value(f'float(A72[{row},{col}])') for col in range(3)] for row in range(3)])
        assert np.all(A72==1), f"A72 expected all elements to be 1, got {A72}"
        assert A72.shape==(3, 3), f"A72 expected shape (3,3), got {A72.shape}"

        A73 = np.array([[tb.value(f'float(A73[{row},{col}])') for col in range(3)] for row in range(3)])
        assert np.all(A73.diagonal()==3), f"A73 diagonal expected all 3, got {A73.diagonal()}"
        assert A73.sum()==9, f"A73 expected sum 9, got {A73.sum()}"
        assert A73.shape==(3, 3), f"A73 expected shape (3,3), got {A73.shape}"

        A74 = np.array([[tb.value(f'float(A74[{row},{col}])') for col in range(10)] for row in range(10)])
        assert A74.shape==(10, 10), f"A74 expected shape (10,10), got {A74.shape}"
        assert A74.sum()==5, f"A74 expected sum 5, got {A74.sum()}"
        assert np.sum(A74==1)==5, f"A74 expected 5 elements == 1, got {np.sum(A74==1)}"
        assert np.sum(A74==0)==95, f"A74 expected 95 elements == 0, got {np.sum(A74==0)}"

        A75 = np.array([[tb.value(f'float(A75[{row},{col}])') for col in range(5)] for row in range(5)])
        assert A75.shape==(5, 5), f"A75 expected shape (5,5), got {A75.shape}"
        assert A75.sum()==(5*5 + 2*4), f"A75 expected sum {(5*5 + 2*4)}, got {A75.sum()}"

        A76 = np.array([[tb.value(f'float(A76[{row},{col}])') for col in range(10)] for row in range(10)])
        assert A76.shape==(10, 10), f"A76 expected shape (10,10), got {A76.shape}"
        assert A76.sum()==25, f"A76 expected sum 25, got {A76.sum()}"
