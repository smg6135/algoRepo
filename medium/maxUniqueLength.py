def maxLength(A):
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)

arr = [{"a", "b"}, {"a", "b"}, {"a", "b"} ]
print(arr[:])
maxLength(["un","iq","ue"])