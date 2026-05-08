package de.thab.cqt.triangle;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

class TriangleTest {

  @ParameterizedTest
    @CsvSource({
            "3,3,3,3",
            "2,2,2,3",
            "6,6,6,3",
            "5,5,6,2",
            "8,8,9,2",
            "10,11,11,2",
            "5,6,7,1",
            "3,4,6,1",
            "8,2,5,1"
    })
    void validInputTest(int a, int b, int c, int expectedResult) {
      assertEquals(expectedResult, Triangle.numberOfEqualSides(a, b, c));

  }



    @ParameterizedTest
    @CsvSource({
            "0,2,3",
            "-1,2,4",
            "1,-2,0",
            "3,4,0",
            "5,8,0",
            "-1,0,-1",
            "0,0,0",
            "-1,-2,-3",
            "0,-1,4"

    })
    void invalidInputTest(int a, int b, int c) {

      assertThrows(IllegalArgumentException.class, () -> Triangle.numberOfEqualSides(a, b, c));
    }




}