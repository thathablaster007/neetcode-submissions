class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                ss = ''
                while stack and stack[-1] != '[':
                    ss = stack.pop() + ss
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*ss)
        return "".join(stack)
        