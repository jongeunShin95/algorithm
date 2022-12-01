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
        solution(in.readLine());
    }

    public static String solution(String new_id) {
        String answer = "";

        // 1
        answer = new_id.toLowerCase();
        // 2
        answer = answer.replaceAll("[^a-z\\d\\-_.]*", "");
        // 3
        answer = answer.replaceAll("\\.{2,}", ".");
        // 4
        answer = answer.replaceAll("^\\.|\\.$", "");
        // 5
        if (answer.isEmpty()) answer = "a";
        // 6
        if (answer.length() >= 16) answer = answer.substring(0, 15);
        answer = answer.replaceAll("\\.$", "");
        // 7
        if (answer.length() <= 2) while (answer.length() < 3) answer += answer.charAt(answer.length() - 1);

        return answer;
    }
}