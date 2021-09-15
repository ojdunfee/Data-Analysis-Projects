import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    A = np.reshape(list, (3,3))
    calculations = {
        'mean': [[np.mean(A.transpose()[i]) for i in range(len(A))], [np.mean(A[i]) for i in range(len(A))], np.mean(list)],
        'variance': [[np.var(A.transpose()[i]) for i in range(len(A))], [np.var(A[i]) for i in range(len(A))], np.var(list)],
        'standard deviation': [[np.std(A.transpose()[i]) for i in range(len(A))], [np.std(A[i]) for i in range(len(A))], np.std(list)],
        'max': [[np.max(A.transpose()[i]) for i in range(len(A))], [np.max(A[i]) for i in range(len(A))], np.max(list)],
        'min': [[np.min(A.transpose()[i]) for i in range(len(A))], [np.min(A[i]) for i in range(len(A))], np.min(list)],
        'sum': [[np.sum(A.transpose()[i]) for i in range(len(A))], [np.sum(A[i]) for i in range(len(A))], np.sum(list)],
    }
    return calculations