package org.example;

import java.io.IOException;
import java.util.*;

public class Main {
    static boolean[][] visited;
    static int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) throws IOException {
//        solution(new int[][]{{1,0,1,1,1},{1,0,1,0,1}, {1,0,1,1,1}, {1,1,1,0,1}, {0,0,0,0,1}});
        solution(new int[][]{{1,0,1,1,1}, {1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,0},{0,0,0,0,1}});
    }

    public static class Node {
        int y, x, c;
        Node(int y, int x, int c) {
            this.y = y;
            this.x = x;
            this.c = c;
        }
    }

    public static int bfs(int[][] maps) {
        Queue<Node> q = new LinkedList<>();
        visited = new boolean[maps.length][maps[0].length];
        q.add(new Node(0, 0, 1));
        visited[0][0] = true;

        while(!q.isEmpty()) {
            Node n = q.poll();
            int cy = n.y;
            int cx = n.x;
            int cc = n.c;

            for (int d = 0; d < 4; ++d) {
                int dy = cy + dir[d][0];
                int dx = cx + dir[d][1];

                if (dy == maps.length -1 && dx == maps[0].length - 1) return cc + 1;
                if (dy < 0 || dx < 0 || dy >= maps.length || dx >= maps[0].length) continue;
                if (visited[dy][dx] || maps[dy][dx] == 0) continue;
                visited[dy][dx] = true;
                q.add(new Node(dy, dx, cc + 1));
            }
        }
        return 0;
    }

    public static int solution(int[][] maps) {
        int answer = 0;
        answer = bfs(maps);
        answer = (answer == 0) ? -1 : answer;
        return answer;
    }
}