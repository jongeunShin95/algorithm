package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        ArrayList<String> survey = new ArrayList<>();
        ArrayList<Integer> choices = new ArrayList<>();

        while (st.hasMoreTokens()) survey.add(new String(st.nextToken()));
        st = new StringTokenizer(in.readLine());
        while (st.hasMoreTokens()) choices.add(new Integer(st.nextToken()));
        solution(survey.toArray(new String[survey.size()]), choices.stream().mapToInt(i -> i).toArray());
    }

    public static String solution(String[] survey, int[] choices) {
        String answer = "";
        HashMap<String, Integer> m = new HashMap<String, Integer>(){{
            put("R", 0);put("T", 0);put("C", 0);put("F", 0);put("J", 0);put("M", 0);put("A", 0);put("N", 0);
        }};
        int[] score = {3, 2, 1, 0, 1, 2, 3};

        for (int i=0; i<choices.length; ++i) {
            if (choices[i] < 4) m.replace(String.valueOf(survey[i].charAt(0)), m.get(String.valueOf(survey[i].charAt(0))) + score[choices[i] - 1]);
            else if (choices[i] > 4) m.replace(String.valueOf(survey[i].charAt(1)), m.get(String.valueOf(survey[i].charAt(1))) + score[choices[i] - 1]);
        }
        answer += (m.get("R") >= m.get("T")) ? "R" : "T";
        answer += (m.get("C") >= m.get("F")) ? "C" : "F";
        answer += (m.get("J") >= m.get("M")) ? "J" : "M";
        answer += (m.get("A") >= m.get("N")) ? "A" : "N";

        return answer;
    }
}