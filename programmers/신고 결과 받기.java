package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine(), ",");
        ArrayList<String> id_list = new ArrayList<>();
        ArrayList<String> report = new ArrayList<>();
        int k;

        while (st.hasMoreTokens()) id_list.add(st.nextToken());
        st = new StringTokenizer(in.readLine(), ",");
        while (st.hasMoreTokens()) report.add(st.nextToken());
        st = new StringTokenizer(in.readLine());
        k = Integer.parseInt(st.nextToken());

        solution(id_list.toArray(new String[id_list.size()]), report.toArray(new String[report.size()]), k);
    }

    public static int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        HashMap<String, HashSet<String>> reporter = new HashMap<>();
        HashMap<String, HashSet<String>> reported = new HashMap<>();

        for (String str: id_list) {
            reporter.put(str, new HashSet<>()); // 신고 한 사람: 신고받은 사람
            reported.put(str, new HashSet<>()); // 신고받은 사람: 신고 한 사람
        }
        for (String str: report) {
            String[] re = str.split(" ");
            reporter.get(re[0]).add(re[1]);
            reported.get(re[1]).add(re[0]);
        }
        for (int i=0; i<id_list.length; ++i) {
            for (String str: reporter.get(id_list[i])) {
                if (reported.get(str).size() >= k) answer[i]++;
            }
        }

        return answer;
    }
}