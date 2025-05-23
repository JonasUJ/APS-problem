import sys
import string

digits = set(string.digits)
lines = list(sys.stdin)

try:
    ans = lines[0]

    assert ans != ""
    assert ans != "\n"
    assert ans != "\r\n"
    assert digits.issuperset(ans.strip("\n")), ans
    assert len(lines) == 1
except:
    exit(43)

exit(42)
