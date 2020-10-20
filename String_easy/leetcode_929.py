class Solution:
    def numUniqueEmails(self, emails) -> int:
        local_name = ""
        found_local = False
        domain_name = ""
        ans = []
        for j in range(len(emails)):
            for i in range(len(emails[j])):
                if (emails[j][i] == "+" or emails[j][i] == "@") and not found_local:

                    local_name = emails[j][:i]
                    local_name = local_name.replace(".","")
                    found_local = True
                if emails[j][i] == "@":
                    domain_name = emails[j][i + 1:]
                    ans.append(local_name +"@"+ domain_name)
                    found_local = False
                    break
        return len(set(ans))
s = Solution()
a = ["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"]
print(s.numUniqueEmails(a))


