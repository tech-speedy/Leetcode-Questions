class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        st = []
        
        for ch in list(s):

            #Opening bracket
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            #Closing bracket    
            else:
                if len(st) == 0:
                    return False
                top = st.pop()
                if ch == ')' and top!= '(':
                    return False
                if ch == '}' and top!= '{':
                    return False
                if ch == ']' and top!= '[':
                    return False

        if len(st) == 0:
            return True
        else:
            return False