# class Solution:
#     def solve(self, s):
#         stack = []
#         for ch in s:
#             if len(stack) == 0:
#                 stack.append(ch)
#             elif len(stack) > 0:
#                 if stack[-1] == ch:
#                     continue
#                 else:
#                     stack.append(ch)
#         s = "".join(stack)
#         return s
class Solution:
	def solve(self,x):
		i=0
		r=''
		l=len(x)
		while i<l:
			r+=x[i]
			i+=1
			while i<l and x[i]==x[i-1]:i+=1
		return r