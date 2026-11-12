import numpy as np

def jensen_shannon_divergence(P: list[float], Q: list[float]) -> float:
    """
    Compute the Jensen-Shannon Divergence between two probability distributions.
    
    Args:
        P: First probability distribution
        Q: Second probability distribution
    
    Returns:
        Jensen-Shannon Divergence value
    """
    # Your code here
    P = np.array(P)
    Q = np.array(Q)
    M = (P+Q)*0.5
    log_P_by_M = np.array([np.log(P[i]/M[i]) if P[i] != 0 else 0 for i in range(len(P))])
    log_Q_by_M = np.array([np.log(Q[i]/M[i]) if Q[i] != 0 else 0 for i in range(len(Q))])
    KL_PM = sum(P*log_P_by_M)
    KL_QM = sum(Q*log_Q_by_M)
    JSD = 0.5*(KL_PM + KL_QM)
    return JSD
