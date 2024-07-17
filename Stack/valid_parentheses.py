class Solution:
    def isValid(self, s: str) -> bool:
        st = list()
        for br in s:
            if br in ['{','(','[']:
                st.append(br)
                continue
            else:
                if st and st[-1]=='{' and br=='}':
                    st.pop()
                elif st and st[-1]=='(' and br==')':
                    st.pop()
                elif st and st[-1]=='[' and br==']':
                    st.pop()
                else: # if st is empty or top of st doesn't match with current bracket(ie,br) in s
                    return False
        if not st:
            return True
        else:
            return False

Solution().isValid("{[()]}")

#alternatively, using dict
class Solution:
    def isValid(self, s: str) -> bool:
        st = list()
        matching_dict = {'}':'{',')':'(',']':'['}
        for br in s:
            if br in ['{','(','[']:
                st.append(br)
            else:
                if st and st[-1]== matching_dict[br]:
                    st.pop()
                else:# if st is empty or top of st doesn't match with current bracket(ie,br) in s
                    return False
        return not st


Solution().isValid("{[()]}")