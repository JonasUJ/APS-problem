import sys
import string
from collections import Counter

try:
    alpha = set(string.ascii_lowercase)

    lines = [line for line in sys.stdin]
    n = lines[0]
    lines = lines[1:]
    assert not n.startswith(" ")
    assert not n.startswith("0")
    assert not n.startswith("+")
    n = int(n)
    assert 1 <= n <= 100_000

    assert len(lines) == n

    problems = []

    for line in lines:
        assert line != "\n"
        assert not line.startswith(" ")
        assert line.endswith("\n")
        assert not line.endswith("\r\n")
        
        K, M, P, T = line.split(" ")
        problems.append((K, M, P, T))

        assert alpha.issuperset(K)
        assert alpha.issuperset(M)
        assert 1 <= int(P) <= 200
        assert 1 <= int(T) <= 100

    name_counter = Counter([K for K, *_ in problems])
    method_counter = Counter([(K, M) for K, M, *_ in problems])

    assert name_counter.most_common(1)[0][1] <= 3 # Only up to three problems with same name
    assert method_counter.most_common(1)[0][1] == 1 # At most one way to solve a problem
    
except:
    exit(43)

exit(42)

