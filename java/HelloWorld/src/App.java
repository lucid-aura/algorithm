import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Stack;
import java.util.stream.IntStream;
import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        int n=9;
        int answer = 0;
        int[][] wires = {{1,3},{2,3},{3,4},{4,5},{4,6},{4,7},{7,8},{7,9}};
        //int[][] wires = {{1,2},{2,3},{3,4}};
        //int[][] wires = {{1,2},{2,7},{3,7},{3,4},{4,5},{6,7}};
        ArrayList<Integer> comp = new ArrayList<Integer>();
        ArrayList<Integer[]> wires_list = new ArrayList<Integer[]>();

        for (int i=0; i<wires.length; i++){ // wires arraylist로 만들기
            wires_list.add(new Integer[]{wires[i][0], wires[i][1]});
        }

        for (int i=0; i<wires_list.size(); i++){
            ArrayList<Integer[]> test = new ArrayList<Integer[]>();
            for (int j=0; j<wires_list.size(); j++){ // 간선을 하나씩 빼면서 노드 개수 확인
                if (i != j){ // 하나의 간선만 빼고 추가
                    test.add(wires_list.get(j));
                }
            }
            comp.add(search(test, n));
            //comp.add(search(test).size());
            // for (int j=0; j<test.size(); j++){
            //     System.out.println(test.get(j)[0] + " " + test.get(j)[1]);// + " " + test[1]);
            // }
            
        }
        for (int i=0; i<comp.size(); i++){
            comp.set(i, Math.abs(n-2*comp.get(i)));
            System.out.println("절대값 : " + Math.abs(n-2*comp.get(i)) + " " + answer);
        }
        int min = Collections.min(comp);
        System.out.println(min);

        // for (int i=0; i<comp.size(); i++){
        //     System.out.println(comp.get(i));
        // }

        //System.out.println(a);
    }

    //public static ArrayList<Integer> search(ArrayList<Integer[]> edge){
    public static int search(ArrayList<Integer[]> edge, int n){
        //int node[] = {};
        
        //ArrayList<Integer> contain_node = new ArrayList<Integer>();
        HashSet<Integer> cango = new HashSet<Integer>();
        cango.add(edge.get(0)[0]);
        cango.add(edge.get(0)[1]);
        for (Integer[] i:edge){
            //if (!IntStream.of(node).anyMatch(x -> x == i[0])){
            if (cango.contains(i[0]) || cango.contains(i[1])){
                cango.add(i[0]);
                cango.add(i[1]);
            }
            
            //node.add(i[1]);
            //     if (!node.contains(i[0])){
            //     node.add(i[0]);
            //     if (!node.contains(i[1])) {
            //         node.add(i[1]);
            //     }
            // }
        }

        System.out.println(cango.size() + "사이즈\n");
        return cango.size();
    }
}


    //     //입금 순서 통장 표시 (나누어서) 출금은 마지막부터 pop
    //     int[] answer = {};
    //     //int[] deposit = {500,1000,-300,200,-400,100,-100};
    //     int[] deposit = {500,1000,2000,-1000,-1500,500};
    //     Stack<Integer> bankbook = new Stack<>();
    //     for (int money:deposit){ // money는 0이 아닌 정수
    //         if (money > 0){ //입금
    //             bankbook.push(money);
    //         }
    //         else { // 출금
    //             int last = 0;
    //             int diff = last + money;
    //             //System.out.println(money);
    //             while(diff < 0){ //출금이 전부 갚아질때까지
    //                 last = bankbook.peek();
    //                 diff = last + diff;       
    //                 //System.out.println(diff);
    //                 bankbook.pop();
    //             }
    //             if (diff > 0){
    //                 bankbook.push(diff);
    //             }                
                
                
    //         }
    //         System.out.println(bankbook);
    //     }

    //     Object[] temp = bankbook.toArray();
    //     answer = new int[temp.length];
    //     for (int i = 0; i < temp.length; i++){
    //         answer[i] = Integer.parseInt(temp[i].toString());
    //     }
    //     //answer = Arrays.stream(a).mapToInt(Integer::intValue).toArray();
    //     System.out.println(answer);
    // }


        // //d = 적재량 m = 상자 수
        // int[] d = {1,3,2,5,4};
        // int m = 4;
        // int size = 1;
        // int answer = 0;
        // int i;
        // for (i=0; i<d.length; i++){
        //     if (size <= d[i]){
        //         m -= size;
        //         size *= 2;
        //         answer += 1;
        //     }
        //     else {
        //         size = 1;
        //     }
        //     if (m <= 0) {
        //         answer = i+1;
        //         System.out.println(answer);
        //     }
        // }
        // if (m > 0) answer = -1;
        // System.out.println(answer);


    //     int[] answer = {};
    //     answer = new int[2];
    //     int[][] a = {{1,1}, {2,2}, {1,2}};
    //     //int[][] a = {{1,4}, {3,4}, {3,10}};
    //     if (a[0][0] == a[1][0]){
    //         answer[0] = a[2][0];
    //     }
    //     else if (a[0][0] == a[2][0]){
    //         answer[0] = a[1][0];
    //     }
    //     else {
    //         answer[0] = a[0][0];
    //     }

    //     if (a[0][1] == a[1][1]){
    //         answer[1] = a[2][1];
    //     }
    //     else if (a[0][1] == a[2][1]){
    //         answer[1] = a[1][1];
    //     }
    //     else {
    //         answer[1] = a[0][1];
    //     }
    //     System.out.print(answer[0] + " " + answer[1]);
    //     for(int[] i:a) {
    //         for (int j:i){
    //             //System.out.print(j);
    //         }
            
    //     }
    // }

    //     String number = "775841";
    //     int k = 4;
    //     Integer[] num = new Integer[number.length()];
    //     String[] numbers = number.split("");
    //     int cnt = 0;
    //     for (String s : numbers){
    //         num[cnt] = Integer.parseInt(s);
    //         System.out.println(num[cnt]);
    //         cnt++;
    //     }
    //     Arrays.sort(num, Collections.reverseOrder());
    //     String answer = "";
    //     for (int i=0; i<k; i++){
    //         answer += Integer.toString(num[i]);
    //     }
    //     System.out.println(answer);
    // }
//}
