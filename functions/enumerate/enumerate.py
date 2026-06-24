# ## 7. A Problem Well-Stated Is Half Solved
#
# Read this problem:
#
# > *"Given a list, find the two numbers that add up to a target."*
#
# Now read it with precision:
#
# > *"Given a list of integers `nums` and an integer `target`,*
# > *return the **indices** (not the values) of the two numbers*
# > *such that they add up to `target`.*
# > *Assume exactly one solution exists.*
# > *You may not use the same element twice."*
#
# **The second version already tells you:**
# - Return indices → I need to track positions
# - Exactly one solution → I can stop at first find
# - Same element not twice → I need to check `i ≠ j`
# - These constraints point directly toward a hash-map solution
#
# ```python
# def two_sum(nums, target):
#     # What do I know?
#     #   nums   — list of integers
#     #   target — the sum I seek
#     # What must I return?
#     #   [index_1, index_2] — the positions, not the values
#     # Shape?
#     #   Search — for each number, I need its complement
#     #   Build  — I can REMEMBER what I've seen (hash map!)
#
#     seen = {}                         # number → its index
#     for i, num in enumerate(nums):
#         complement = target - num     # what do I NEED?
#         if complement in seen:        # have I SEEN it before?
#             return [seen[complement], i]
#         seen[num] = i                 # remember this number
#     return []
#
# # nums = [2, 7, 11, 15], target = 9
# # i=0: need 7, not seen yet. Remember: {2:0}
# # i=1: need 2, YES seen at index 0! → return [0, 1] ✨
# ```
#
# **This solution emerged naturally — not from cleverness, but from reading carefully.**
#
# ---



fruits = ["mango", "apple", "pear"]
def enumerate_old_way():
    i = 0
    for fruit in fruits:
        print(i, fruit)
        i = i + 1

enumerate_old_way()

def enumerate_new_way():
    for i, fruit in enumerate(fruits):
        print(i, fruit)

enumerate_new_way()


























