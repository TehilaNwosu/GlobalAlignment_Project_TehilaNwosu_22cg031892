# algorithm/alignment_engine.py

def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-1):
    """
    Needleman-Wunsch Global Sequence Alignment Algorithm.
    Uses dynamic programming to find the optimal alignment score.
    """
    m = len(seq1)
    n = len(seq2)

    # Step 1: Initialize the (m+1) x (n+1) matrix with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill first row and column with cumulative gap penalties
    for i in range(m + 1):
        dp[i][0] = i * gap
    for j in range(n + 1):
        dp[0][j] = j * gap

    # Step 3: Fill the matrix using the recurrence relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Check if characters match or mismatch
            score = match if seq1[i - 1] == seq2[j - 1] else mismatch

            diag = dp[i - 1][j - 1] + score  # diagonal (match/mismatch)
            top  = dp[i - 1][j] + gap         # gap in seq2
            left = dp[i][j - 1] + gap         # gap in seq1

            dp[i][j] = max(diag, top, left)

    # Step 4: Return the final score and full matrix
    return dp[m][n], dp


def validate_sequences(seq1, seq2):
    """Validate that sequences only contain valid characters."""
    valid = set("ACGTUN-")
    seq1 = seq1.upper().strip().replace(" ", "")
    seq2 = seq2.upper().strip().replace(" ", "")

    invalid1 = set(seq1) - valid
    invalid2 = set(seq2) - valid

    if invalid1:
        raise ValueError(f"Sequence 1 contains invalid characters: {', '.join(invalid1)}")
    if invalid2:
        raise ValueError(f"Sequence 2 contains invalid characters: {', '.join(invalid2)}")
    if not seq1:
        raise ValueError("Sequence 1 cannot be empty.")
    if not seq2:
        raise ValueError("Sequence 2 cannot be empty.")

    return seq1, seq2
