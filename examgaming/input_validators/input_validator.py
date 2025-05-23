import sys
import string

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

    for line in lines:
        assert line != "\n"
        assert not line.startswith(" ")
        assert line.endswith("\n")
        assert not line.endswith("\r\n")
        
        K, M, P, T = line.split(" ")

        assert alpha.issuperset(K)
        assert alpha.issuperset(M)
        assert 1 <= int(P) <= 200
        assert 1 <= int(T) <= 100
except:
    exit(43)

exit(42)

