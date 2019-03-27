# coding=utf-8

"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites,
for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0,
             and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


# class Solution(object):
#     def canFinish(self, N, prerequisites):
#         """
#         :type N,: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """
#         graph = collections.defaultdict(list)
#         for u, v in prerequisites:
#             graph[u].append(v)
#         # 0 = Unknown, 1 = visiting, 2 = visited
#         visited = [0] * N
#         for i in range(N):
#             if not self.dfs(graph, visited, i):
#                 return False
#         return True
#
#     # Can we add node i to visited successfully?
#     def dfs(self, graph, visited, i):
#         if visited[i] == 1: return False
#         if visited[i] == 2: return True
#         visited[i] = 1
#         for j in graph[i]:
#             if not self.dfs(graph, visited, j):
#                 return False
#         visited[i] = 2
#         return True


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        for i in range(numCourses):
            graph.setdefault(i, [])
        visit = [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
        for i in range(numCourses):
            if not self.canFinishDFS(graph, visit, i):
                return False
        return True

    def canFinishDFS(self, graph, visit, i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not self.canFinishDFS(graph, visit, j):
                return False
        visit[i] = 1
        return True


if __name__ == '__main__':
    a = Solution()
    numCourses = 3
    prerequisites = [[1, 0], [2, 1]]
    print(a.canFinish(numCourses, prerequisites))