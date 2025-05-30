class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        L = len(words[0])           # length of one word
        k = len(words)              # number of words
        total = L * k               # total length of a valid block
        n = len(s)
        need = Counter(words)       # target multiset
        res = []

        # There are L different starting offsets: 0,1,…,L-1
        for offset in range(L):
            left = offset           # left boundary of the sliding window
            seen = Counter()
            cnt  = 0               # how many words currently matched

            # Step through the string in jumps of L
            for right in range(offset, n - L + 1, L):
                word = s[right:right + L]

                # If the chunk is a needed word, update counters
                if word in need:
                    seen[word] += 1
                    cnt += 1

                    # If we have too many of that word, shrink from the left
                    while seen[word] > need[word]:
                        left_word = s[left:left + L]
                        seen[left_word] -= 1
                        left += L
                        cnt -= 1

                    # When we have k words, record the start index
                    if cnt == k:
                        res.append(left)
                        # Move left boundary forward by one word to look for the next
                        left_word = s[left:left + L]
                        seen[left_word] -= 1
                        left += L
                        cnt -= 1
                else:
                    # Reset the window if word not in need
                    seen.clear()
                    cnt = 0
                    left = right + L

        return res


'''
Mini-example:

s      = "barfoofoobarthe"
words  = ["bar", "foo"]
L = 3, k = 2, total = 6.

Valid concatenations are "barfoo" and "foobar".

Slide a 6-char window from left to right three characters at a time:

window start	6-char slice	2 little words	valid?
0	barfoo	bar · foo	✔ yes
3	foofoo	foo · foo	✘ no
6	foobar	foo · bar	✔ yes
9	barthe	bar · the	✘ no

So the answers are indices [0, 6].
'''
