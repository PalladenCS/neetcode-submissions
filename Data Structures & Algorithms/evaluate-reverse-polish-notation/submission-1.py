class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        window = []

        for i in tokens:
            if i not in "+-*/":
                window.append(int(i))
            else:
                right = window.pop()
                left = window.pop()

                if i == "+":
                    window.append(left + right)
                elif i == "-":
                    window.append(left - right)
                elif i == "*":
                    window.append(left * right)
                elif i == "/":
                    window.append(int(left / right))

        return window[0]