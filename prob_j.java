// MCPC 2018 Problem J: Need for Speed

import java.util.Scanner ;

class prob_j {

    static double simulate(int num_sec, int[][] section, double offset) {
        double total = 0.0 ;
        for (int i=0; i<num_sec; i++) {
            total += section[i][0]/(section[i][1]+offset) ;
        }
        return total ;
    }


    static void solve(int num_sec, int [][] section, int total_time) {
        int min_dist= section[0][1] ;
        for (int i=0; i<num_sec; i++) {
            if (min_dist > section[i][1]) min_dist = section[i][1] ;
        }
        double low_bound = (double)(-min_dist) ;
        double high_bound = Math.abs(low_bound) + 1.0 ; // > low_bound, >0

        // find high_bound
        while (true) {
            double total = simulate(num_sec, section, high_bound) ;
            if (total < (double)total_time) break ;
            high_bound += high_bound ;
        }
        //System.out.printf("low: %.5f high: %.5f\n", low_bound, high_bound) ;

        // binary search
        final double max_err=0.001 ;
        while (high_bound-low_bound > max_err) {
            double mid = (high_bound+low_bound) / 2 ;
            double total = simulate(num_sec, section, mid) ;
            //System.out.printf("mid: %.5f total: %.5f\n", mid, total) ;
            if (total == (double)total_time) high_bound = low_bound = mid ;
            else if (total < (double)total_time) { // too big
                high_bound = mid ;
            }
            else low_bound = mid ;
        }

        System.out.printf("%.2f\n", (high_bound+low_bound)/2) ;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in) ;
        int num_tc = sc.nextInt() ;

        for (int tc=0; tc<num_tc; tc++) {
            int num_sec = sc.nextInt() ;
            int total_time = sc.nextInt() ;
            int section[][] = new int[num_sec][2] ;
            for (int i=0; i<num_sec; i++) {
                section[i][0] = sc.nextInt() ;  // Distance
                section[i][1] = sc.nextInt() ;  // SpeedMeter read
            }
            solve(num_sec, section, total_time) ;
        }
    }
}
