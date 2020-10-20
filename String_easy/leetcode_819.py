from collections import Counter
import collections
class Solution:
    #题解
    def mostCommonWord1(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans

    #{'x': 23, 'w': 23, 'z': 23, 'y': 23, 'v': 22, 'u': 20, 't': 20, 's': 18, 'r': 17, 'q': 17, 'o': 15, 'p': 13,'n': 13, 'l': 11, 'm': 11, 'k': 11, 'j': 10, 'i': 9, 'h': 8, 'g': 7, 'f': 6, 'e': 4, 'c': 3, 'd': 3,'b': 2, 'a': 1}
    #{'x': 21, 'v': 20, 'y': 19, 'w': 18, 't': 18, 'z': 17, 'u': 15, 'o': 15, 's': 14, 'r': 14, 'p': 13, 'q': 12,'n': 12, 'm': 10, 'l': 9, 'k': 9, 'i': 8, 'j': 8, 'g': 7, 'z;': 6, 'h': 6, 'f': 5, 'u;': 5, 'w;': 5,'q;': 5, 'e': 4, 'y;': 4, 's;': 4, 'r;': 3, 'd': 2, 'v;': 2, 'h;': 2, 'l;': 2, 'k;': 2, 't;': 2, 'b': 2,'j;': 2, 'c': 2, 'x;': 2, 'c;': 1, 'n;': 1, 'd;': 1, 'a': 1, 'm;': 1, 'f;': 1, 'i;': 1})
    #我
    def mostCommonWord(self, paragraph: str, banned) -> str:

        pun = ['!','?',"'",',','.',';']
        for i in pun:
            paragraph = paragraph.replace(i,' ')
        paragraph = paragraph.lower()
        temp = paragraph.split()
        temp1 = Counter(temp)
        ans, best = '', 0
        for i in temp1:
            if i not in banned and temp1[i] > best:
                ans, best = i, temp1[i]

        return ans
s = Solution()
a = "L, P! X! C; u! P? w! P. G, S? l? X? D. w? m? f? v, x? i. z; x' m! U' M! j? V; l. S! j? r, K. O? k? p? p, H! t! z' X! v. u; F, h; s? X? K. y, Y! L; q! y? j, o? D' y? F' Z; E? W; W' W! n! p' U. N; w? V' y! Q; J, o! T? g? o! N' M? X? w! V. w? o' k. W. y, k; o' m! r; i, n. k, w; U? S? t; O' g' z. V. N? z, W? j! m? W! h; t! V' T! Z? R' w, w? y? y; O' w; r? q. G, V. x? n, Y; Q. s? S. G. f, s! U? l. o! i. L; Z' X! u. y, Q. q; Q, D; V. m. q. s? Y, U; p? u! q? h? O. W' y? Z! x! r. E, R, r' X' V, b. z, x! Q; y, g' j; j. q; W; v' X! J' H? i' o? n, Y. X! x? h? u; T? l! o? z. K' z' s; L? p? V' r. L? Y; V! V' S. t? Z' T' Y. s? i? Y! G? r; Y; T! h! K; M. k. U; A! V? R? C' x! X. M; z' V! w. N. T? Y' w? n, Z, Z? Y' R; V' f; V' I; t? X? Z; l? R, Q! Z. R. R, O. S! w; p' T. u? U! n, V, M. p? Q, O? q' t. B, k. u. H' T; T? S; Y! S! i? q! K' z' S! v; L. x; q; W? m? y, Z! x. y. j? N' R' I? r? V! Z; s, O? s; V, I, e? U' w! T? T! u; U! e? w? z; t! C! z? U, p' p! r. x; U! Z; u! j; T! X! N' F? n! P' t, X. s; q'"
b = ["m","i","s","w","y","d","q","l","a","p","n","t","u","b","o","e","f","g","c","x"]
print(s.mostCommonWord(a,b))