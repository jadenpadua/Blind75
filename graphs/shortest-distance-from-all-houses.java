class Solution {
    private final int[] rowDir = {0,0,1,-1};
    private final int[] colDir = {1,-1,0,0};

    public int shortestDistance(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return -1;
        }

        int rows = grid.length, cols = grid[0].length;
        int[][] reach = new int[rows][cols];
        int[][] dist = new int[rows][cols];

        int totalBuildings = 0;
        for (int i = 0l; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    bfs(grid, i, j, reach, dist);
                    totalBuildings++;
                }
            }
        }

        int minDist = Integer.MAX_VALUE;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (reach[i][j] == totalBuildings && dist[i][j] < minDist) {
                    minDist = dist[i][j];
                }
            }
        }

        return minDist == Integer.MAX_VALUE ? -1 : minDist;
    }

    private void bfs(int[][] grid, int row, int col, int[][] reach, int[][] dist) {
        int rows = grid.length, col = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[rows][cols];

        q.offer(new int[]{row, col});
        visited[row][col] = true;

        int d = 0;
        while(!q.isEmpty()) {
            int size = q.size();
            d++;
            for (int i = 0; i < size; i++) {
                int[] curr = q.poll();
                for (int k = 0; k < 4; k++) {
                    int rr = curr[0] + rowDir[k];
                    int cc = curr[1] + colDir[k];

                    if (!isValid(grid, rr, cc, visited)) {
                        continue;
                    }

                    q.offer(new int[]{rr, cc});
                    visited[rr][cc] = true;
                    reach[rr][cc]++;
                    dist[rr][cc] += d;

                }
            }
        }
    } 
    
    private boolean isValid(int[][] grid, int rr, int cc, boolean[][] visited) {
        if (rr < 0 || c < 0 || rr > grid.length -1 || cc > grid[0].length - 1) {
            return false;
        }

        if (visited[rr][cc]) {
            return false;
        }

        if (grid[rr][cc] != 0) {
            return false;
        }

        return true;
    }

}
