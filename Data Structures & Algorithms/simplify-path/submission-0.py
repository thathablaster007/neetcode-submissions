class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathnames = path.split('/')
        for n in pathnames:
            if n == "..":
                if stack:
                    stack.pop()
            elif n != '' and n != '.':
                stack.append(n)
        return "/" + "/".join(stack)
        