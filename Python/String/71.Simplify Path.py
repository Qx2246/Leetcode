class Solution(object):
    def simplifyPath(self, path):
        stack = []

        for dir in path.split("/"):
            if dir == "" or dir == ".":
                continue
            elif dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)

        return "/" + "/". join(stack)        
