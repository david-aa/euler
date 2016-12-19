
public class EulerSqrtRev_3 {

    public static boolean isPrime(long number) {
        if (number == 2) return true;
        if (number < 2 || number % 2 == 0) return false;
        double max = Math.sqrt(number);
        for (long i = 3; i <= max; i +=2) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    public static void main(String args[]) {
        final long number =  600851475143L;
        long max = number/2;
        for (long i = 2; i < max; i++) {
            if (number % i == 0 && isPrime(i)) {
                System.out.println(i);
            }
        }
    }

}