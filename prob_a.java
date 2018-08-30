// MCPC 2018 Problem J: Need for Speed

import java.util.Scanner ;
import java.util.PriorityQueue ;

class prob_a {

    static final long INF = 1000000000000000000L ;  // 10**18
    static final int DEFAULT_EDGE = 10 ;

    static int [][][] init_edge(int min_x, int max_x, int min_y, int max_y, int num_jam, int [][] jams) {
        // Return edge[x][y][direction], which contains t value of jams
        int edge[][][] = new int [max_x-min_x+1][max_y-min_y+1][4] ;

        for (int x = min_x; x <= max_x; x++) {
            for (int y = min_y; y <= max_y; y++) {
                if (x == max_x) edge[x-min_x][y-min_y][0] = -1 ;  // right
                else edge[x-min_x][y-min_y][0] = DEFAULT_EDGE ;
                if (x == min_x) edge[x-min_x][y-min_y][1] = -1 ;  // left
                else edge[x-min_x][y-min_y][1] = DEFAULT_EDGE ;
                if (y == max_y) edge[x-min_x][y-min_y][2] = -1 ;  // up
                else edge[x-min_x][y-min_y][2] = DEFAULT_EDGE ;
                if (y == min_y) edge[x-min_x][y-min_y][3] = -1 ;  // down
                else edge[x-min_x][y-min_y][3] = DEFAULT_EDGE ;
            }
        }

        for (int jam=0; jam < num_jam; jam++) {
            // Horizontal edge: exclude y1, y2
            for (int y = jams[jam][1]+1; y < jams[jam][3]; y++) {
                // include x1, exclude x2
                for (int x = jams[jam][0]; x < jams[jam][2]; x++) {
                    edge[x-min_x][y-min_y][0] = jams[jam][4] ;
                    edge[x-min_x+1][y-min_y][1] = jams[jam][4] ;
                }
            }

            // Vertical edge: exclude x1, x2
            for (int x = jams[jam][0]+1; x < jams[jam][2]; x++) {
                // include y1, exclude y2
                for (int y = jams[jam][1]; y < jams[jam][3]; y++) {
                    edge[x-min_x][y-min_y][2] = jams[jam][4] ;
                    edge[x-min_x][y-min_y+1][3] = jams[jam][4] ;
                }
            }
        }

        return edge ;
    }


    static void update_pq(int add_weight, int x, int y, long weight, PriorityQueue<PQ_obj> pq, long [][]tmp_dist, int min_x, int min_y) {
        if (add_weight < 0) return ;
        long new_weight = add_weight + weight ;
        if (new_weight < tmp_dist[x-min_x][y-min_y]) {
            pq.add(new PQ_obj(x, y, new_weight)) ;
            tmp_dist[x-min_x][y-min_y] = new_weight ;
        }
    }

    static void eval_node(PQ_obj pq_obj, PriorityQueue<PQ_obj> pq, long [][]distance,
                long [][]tmp_dist, int [][][]edges, int min_x, int min_y) {

        distance[pq_obj.x-min_x][pq_obj.y-min_y] = pq_obj.weight ;
        tmp_dist[pq_obj.x-min_x][pq_obj.y-min_y] = pq_obj.weight ;

        int right = edges[pq_obj.x-min_x][pq_obj.y-min_y][0] ;
        int left = edges[pq_obj.x-min_x][pq_obj.y-min_y][1] ;
        int up = edges[pq_obj.x-min_x][pq_obj.y-min_y][2] ;
        int down = edges[pq_obj.x-min_x][pq_obj.y-min_y][3] ;

        update_pq(right, pq_obj.x+1, pq_obj.y, pq_obj.weight, pq, tmp_dist, min_x, min_y) ;
        update_pq(left, pq_obj.x-1, pq_obj.y, pq_obj.weight, pq, tmp_dist, min_x, min_y) ;
        update_pq(up, pq_obj.x, pq_obj.y+1, pq_obj.weight, pq, tmp_dist, min_x, min_y) ;
        update_pq(down, pq_obj.x, pq_obj.y-1, pq_obj.weight, pq, tmp_dist, min_x, min_y) ;

    }


    static void dijkstra(int src_x, int src_y, int dest_x, int dest_y,
           int min_x, int max_x, int min_y, int max_y, int [][][]edges) {

        long [][] distance = new long [max_x-min_x+1][max_y-min_y+1] ;
        long [][] tmp_dist = new long [max_x-min_x+1][max_y-min_y+1] ;

        for (int x = min_x; x <= max_x; x++) {
            for (int y = min_y; y <= max_y; y++) {
                distance[x-min_x][y-min_y] = INF ;
                tmp_dist[x-min_x][y-min_y] = INF ;
            }
        }

        distance[src_x-min_x][src_y-min_y] = 0 ;
        tmp_dist[src_x-min_x][src_y-min_y] = 0 ;

        PriorityQueue<PQ_obj> pq = new PriorityQueue<>() ;
        pq.add(new PQ_obj(src_x, src_y, 0L)) ;

        while (!pq.isEmpty()) {
            PQ_obj pq_obj = pq.remove() ;
            if (pq_obj.x == dest_x && pq_obj.y == dest_y) {
                System.out.println(pq_obj.weight) ;
                return ;
            }
            eval_node(pq_obj, pq, distance, tmp_dist, edges, min_x, min_y) ;
        }

        System.err.println("No path to destination") ;
        System.out.println(INF) ;
        return ;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in) ;
        int num_tc = sc.nextInt() ;

        for (int tc=0; tc<num_tc; tc++) {
            int src_x = sc.nextInt() ;
            int src_y = sc.nextInt() ;
            int dest_x = sc.nextInt() ;
            int dest_y = sc.nextInt() ;

            int min_x = Math.min(src_x, dest_x) ;
            int max_x = Math.max(src_x, dest_x) ;
            int min_y = Math.min(src_y, dest_y) ;
            int max_y = Math.max(src_y, dest_y) ;

            int num_jam = sc.nextInt() ;
            int jams[][] = new int [num_jam][5] ;

            for (int jam=0; jam<num_jam; jam++) {
                int x1 = sc.nextInt() ;
                int y1 = sc.nextInt() ;
                int x2 = sc.nextInt() ;
                int y2 = sc.nextInt() ;
                int t = sc.nextInt() ;
                
                jams[jam][0] = x1 ;
                jams[jam][1] = y1 ;
                jams[jam][2] = x2 ;
                jams[jam][3] = y2 ;
                jams[jam][4] = t ;
                min_x = Math.min(min_x, x1) ;
                min_y = Math.min(min_y, y1) ;
                max_x = Math.max(max_x, x2) ;
                max_y = Math.max(max_y, y2) ;
            }


            int [][][] edges = init_edge(min_x, max_x, min_y, max_y, num_jam, jams) ;
            dijkstra(src_x, src_y, dest_x, dest_y, min_x, max_x, min_y, max_y, edges) ;
        }
    }
}

class PQ_obj implements Comparable<PQ_obj> {
    int x, y ;
    long weight ;

    public PQ_obj(int x, int y, long weight) {
        this.x = x ;
        this.y = y ;
        this.weight = weight ;
    }

    public int compareTo(PQ_obj other) {
        if (this.weight > other.weight) return 1 ;
        else if (this.weight < other.weight) return -1 ;
        else return 0 ;
    }
}

