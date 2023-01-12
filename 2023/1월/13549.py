import sys
sys.stdin = open("./2023/1월/input.txt")
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
INF = 1000001

def Bfs():
  visited = [INF]*(INF+1)
  Q = deque()
  Q.append([N,0])  # node,count
  
  while Q:
    node,count = Q.popleft()
    if visited[node] >count:
      visited[node] = count
    double = node*2
    plus = node+1
    minus = node-1
    
    if 0<=double<INF :
      if visited[double] > count:
        Q.append([double,count])
    
    if 0<=plus < INF : 
      if visited[plus] > count+1:
        Q.append([plus,count+1])

    if 0<=minus < INF : 
      if visited[minus] > count+1:
        Q.append([minus,count+1])

  print(visited[K])
Bfs()

