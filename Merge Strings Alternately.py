class Solution:
   def mergeAlternately(self, s: str, t: str) -> str:
       ans_string = ""
       if len(s) != len(t):
           smaller_string_length = min(len(s), len(t))
           if len(s) > len(t):
               larger_string = s
           else:
               larger_string = t


           for i in range(0, smaller_string_length):
               ans_string += s[i]+t[i]
           ans_string += larger_string[smaller_string_length:]


       if len(s) == len(t):
           smaller_string_length = len(s)
           for i in range(0, smaller_string_length):
               ans_string += s[i]+t[i]
          
      
       return ans_string