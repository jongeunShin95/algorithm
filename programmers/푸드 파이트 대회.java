package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        ArrayList<Integer> food = new ArrayList<>();

        while (st.hasMoreTokens()) food.add(new Integer(st.nextToken()));
        solution(food.stream().mapToInt(i -> i).toArray());
    }

    public static String solution(int[] food) {
        String answer = "";
        StringBuilder sb = new StringBuilder();

        for (int i=1; i<food.length; ++i) for (int j=0; j<food[i]/2; ++j) sb.append(i);

        answer = sb.toString() + "0" + sb.reverse().toString();
        return answer;
    }
}