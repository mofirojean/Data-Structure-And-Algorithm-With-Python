package com.mofirojean;

public class Challenge17 {
    //@author: de-lia
    //code challenge 17: Calculate the sum of digits of a positive integer number.

    public static int allSum(int n) {
        int sum = 0;        // sum is initially zero.

        while(n!=0) {   // while n is not zero
            sum = sum + n % 10; // n modulo 10 is calculated and the modulo is what is added as 'sum' to the previous 'sum'
            n = n/10; // the whole number from the modulo operation becomes the new n.
            // as long as n is not zero, sum = sum + n % 10 is done. When n becomes zero,
            // the while loop stops.
        }

        return sum;
    }

    // driver code / main class

    public static void main(String args[]) {
        int n = 544;    // test case for the function
        System.out.println(allSum(n));
    }
}
