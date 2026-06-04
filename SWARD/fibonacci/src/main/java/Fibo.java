public class Fibo {

    public static void main (String [] args){


        System.out.println(fibonacci(0));

    }


    public static int fibonacci(int count) {

        if (count < 0) {
            throw new IllegalArgumentException();
        }

        if (count <= 1) {
            return count;
        }

        else{
            return fibonacci(count - 1) + fibonacci(count - 2);

        }



    }
}
