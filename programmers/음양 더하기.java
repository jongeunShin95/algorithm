package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        ArrayList<Integer> absolutes = new ArrayList<>();
        ArrayList<Boolean> T = new ArrayList<>();
        int idx = 0;

        while (st.hasMoreTokens()) absolutes.add(new Integer(st.nextToken()));
        st = new StringTokenizer(in.readLine());
        while (st.hasMoreTokens()) T.add(new Boolean(st.nextToken()));

        boolean[] signs = new boolean[T.size()];
        for (Boolean v: T) signs[idx++] = v;

        System.out.println(solution(absolutes.stream().mapToInt(i -> i).toArray(), signs));
    }

    public static int solution(int[] absolutes, boolean[] signs) {
        int answer = 123456789;
        for (int i=0; i<signs.length; ++i) if (!signs[i]) absolutes[i] *= -1;
        answer = Arrays.stream(absolutes).sum();
        return answer;
    }
}