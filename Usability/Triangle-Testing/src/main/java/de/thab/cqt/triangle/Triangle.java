package de.thab.cqt.triangle;

/*
The method should return the number of sides equal to one another:
1. For an equilateral triangle: 3
2. For an isosceles triangle: 2
3. For an unequal triangle: 1
4. Invalid inputs should cause the method to return -1

*/
public class Triangle {

    public static int numberOfEqualSides(int lengthA, int lengthB, int lengthC){

        if( lengthA <= 0 || lengthB <= 0 || lengthC <= 0 ){
            throw new IllegalArgumentException();
        }

        if(lengthA == lengthB && lengthB == lengthC){
            return 3;
        }
        else if(lengthA == lengthB || lengthA == lengthC || lengthB == lengthC){
            return 2;
        }
        else{
            return 1;
        }



    }


}
