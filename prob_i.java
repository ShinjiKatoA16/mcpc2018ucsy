// MCPC 2018 Problem I: Babylonian Numbers

import java.util.Scanner ;

class prob_i {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in) ;
        int num_tc = Integer.parseInt(sc.nextLine()) ;

        for (int tc=0; tc<num_tc; tc++) {
            String s = sc.nextLine() ;
            String[] babylon = s.split(",", -1) ; // 2nd parameter -1
            long total = 0L ;   // 60**8 is 15 digit
            for (String c : babylon) {  // python like syntax
                long c_val ;
                if (c.equals("")) c_val = 0L ;
                else c_val = Long.parseLong(c) ;
                
                total = total*60L + c_val ;
            }
            System.out.println(total) ;
        }
    }
}
