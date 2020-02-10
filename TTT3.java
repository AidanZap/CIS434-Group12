import java.util.*;

public class TTT3{
   static int[] board;
   static int[] scores = {0,0};
   static boolean win, quit, jarvis, friday = false;
   static Scanner input = new Scanner(System.in);
   static int player;
   static int jarvisDelay = 1; //in ms
   
   public static void main(String args[]){
       while(!quit){
         menu();
         if(quit)break;
         startGame();
         while(!win){
            displayBoard();
            playerInput();
            winCheck();
         }
    }// end normal loop
//        int iterations = 500;                //testing loop for jarvis v friday
//        int count = 0;
//        while(count < iterations){       
//          jarvis = true;
//          friday = true;
//          if(quit)break;
//          startGame();
//          while(!win){
//             displayBoard();
//             playerInput();
//             winCheck();
//          }
//          count++;
//      }//end test while
   System.out.println("Player 1:  " + scores[0] +" | "+ "Player 2:  " + scores[1]);   // end test
   }// end main
   static void menu(){
      friday = false;
      jarvis = false;
      System.out.println("Tic Tac Toe\n\nPlay[P]\nQuit[Q]\nHave Jarvis be Player 2[J]\nWar Games[F]\nCurrent Score:");
      System.out.println("Player 1:  " + scores[0] +" | "+ "Player 2:  " + scores[1]);
      String response = input.next().toLowerCase(); 
      if(response.equals("p"));//do nothing, any response will work
      if(response.equals("j")){
      jarvis = true;
      }
      if(response.equals("f")){
      jarvis = true;
      friday = true;
      }
      if(response.equals("q")){
      quit = true;
      }
   }//end menu
   
   static void startGame(){
      board = new int[9];
      for(int i = 0; i < board.length; i++){
         board[i] = 0;
      }
      player = (int)((Math.random() * 2) + 1);
      //player = 1;    //for testing p1 first
      //player = 2;    //for testing p2 first
      win = false;
   }// end startgame
   
   static void displayBoard(){
      for(int i = 1; i <= board.length; i++){
         if(board[i-1] == 0){
            System.out.print("[ ]");
         }
         if(board[i-1] == 1){
            System.out.print("[X]");
         }
         if(board[i-1] == 2){
            System.out.print("[O]");
         }
         if(i == 3){
            System.out.print("      1 2 3\n");
         }
         if(i == 6){
            System.out.print("      4 5 6\n");
         }
         if(i == 9){
            System.out.print("      7 8 9\n");
         }
      }
   }//end displayBoard
   static void playerInput(){
      System.out.println("Player " + player + "'s turn\n");
      while(true){
         int pos = 0;
         if(player == 1 && !friday)pos = input.nextInt();
         if(player == 2 && !jarvis)pos = input.nextInt();
         if(player == 1 && friday)pos = jarvis(1);
         if(player == 2 && jarvis)pos = jarvis(2);           
         if (board[pos-1] == 0){
            board[pos-1] = player;
            break;
         }else{
            System.out.println("Invalid selection, try again");
            displayBoard();
            continue;
         }  
      }//end while
      
      if(player == 1){
      player = 2;
      }else{
      player = 1;
      }
   }// end player input
   static void winCheck(){
      int winner = 0;
      int used = 0;
      int[][] winCombos = {{1,2,3},{4,5,6},{7,8,9},{7,4,1},{8,5,2},{9,6,3},{1,5,9},{7,5,3}};
      for(int i = 0; i < winCombos.length; i++){
         if((board[(winCombos[i][1])-1] != 0) && (board[(winCombos[i][1])-1] == board[(winCombos[i][0])-1]) && (board[(winCombos[i][1])-1] == board[(winCombos[i][2])-1])){
            winner = board[(winCombos[i][1]) - 1];
            break;
         }
      }//end winner for
      for(int i = 0; i < board.length; i++){
         if(board[i] != 0){
         used++;
         }
      }//end draw for
      if (winner !=0){
         scores[winner - 1]++;
         win = true;
         displayBoard();
         System.out.println("Player " + winner + " Wins!");
      }else if(used == 9){
         win = true;
         displayBoard();
         System.out.println("Draw!");
      }
      
   }//end winCheck
   
   static int jarvis(int p){// p is the player that jarvis is playing for
      int o = 2; // o is the opposite player
      if(p == 2) o = 1;
      int[][] winCombos = {{1,2,3},{4,5,6},{7,8,9},{7,4,1},{8,5,2},{9,6,3},{1,5,9},{7,5,3}};
      int play = 1;
      int move = 1;
      for(int i = 0; i < board.length; i++){//find current move
         if(board[i] != 0) move++;
      }
      if(move == 1){//first move strategy
         int temp = (int)((Math.random() * 6) + 1);
         if(temp == 1) play = 1;
         if(temp == 2) play = 3;
         if(temp == 3) play = 7;
         if(temp == 4) play = 9;
         if(temp > 4) play = 5;
      }else if(move == 2){//second move strategy
         if((board[1-1] == o)||(board[3-1] == o)||(board[7-1] == o)||(board[9-1] == o)) play = 5;//first move was a corner, take center
         if((board[2-1] == o)||(board[4-1] == o)||(board[6-1] == o)||(board[8-1] == o)){//first move was an edge, take center, was random changed to prevent double edge win
            play = 5;
         //  int temp = (int)((Math.random() * 6) + 1);
         //if(temp == 1) play = 1;
         //if(temp == 2) play = 3;
         //if(temp == 3) play = 7;
         //if(temp == 4) play = 9;
         //if(temp > 4) play = 5;
         }
         if(board[5-1] == o){
            int temp = (int)((Math.random() * 4) + 1);//first move was center
            if(temp == 1) play = 1;
            if(temp == 2) play = 3;
            if(temp == 3) play = 7;
            if(temp == 4) play = 9;
         }
      }else if(move == 3){//third move strategy,jarvis had 1st move

         if(board[5-1] == o){//jarvis took corner, p1 took center, form line
            if(board[1-1] == p) play = 9;
            if(board[3-1] == p) play = 7;
            if(board[7-1] == p) play = 3;
            if(board[9-1] == p) play = 1;
         }
         if(board[5-1] == p){//jarvis took center, p1 took corner, form line
            if(board[1-1] == o) play = 9;
            if(board[3-1] == o) play = 7;
            if(board[7-1] == o) play = 3;
            if(board[9-1] == o) play = 1;
         }
         //jarvis took corner, p1 took edge or corner, take same side corner
         if(board[5-1] == 0){
            if(board[1-1] == p){
             play = 3;
             if(board[3-1] == o || board[2-1] == o) play = 7;
            }
            if(board[3-1] == p){
             play = 9;
             if(board[9-1] == o || board[6-1] == o) play = 1;
            }
            if(board[7-1] == p){
             play = 1;
             if(board[1-1] == o || board[4-1] == o) play = 9;
            }
            if(board[9-1] == p){
             play = 7;
             if(board[7-1] == o || board[8-1] == o) play = 3;
            }

         }
         if(board[5-1] == p){//jarvis took center, p1 took edge, take far corners
            if(board[2-1] == o) play = 9;
            if(board[4-1] == o) play = 3;
            if(board[6-1] == o) play = 7;
            if(board[8-1] == o) play = 1;
         }
      }else if(move == 4){//4th move start, jarvis had 2nd move
         //p1 double edges, j corner, take center
         if(board[5-1] == 0){
            int edges = 0;
            if(board[2-1] == o) edges++;
            if(board[4-1] == o) edges++;
            if(board[6-1] == o) edges++;
            if(board[8-1] == o) edges++;
            if(edges > 1) play = 5;
         }
         //p1 corner, j center, p1 corner, take edge force draw, strat check default takes edge(8)j, randomize later
         if(board[5-1] == p){
            //use for to check for 2 corners
            int corners = 0;
            if(board[1-1] == o) corners++;
            if(board[3-1] == o) corners++;
            if(board[7-1] == o) corners++;
            if(board[9-1] == o) corners++;
            if(corners > 1){//take and edge
               int temp = (int)((Math.random() * 4) + 1);//first move was center
               if(temp == 1) play = 2;
               if(temp == 2) play = 4;
               if(temp == 3) play = 6;
               if(temp == 4) play = 8;
            }
         }
         //p1 center, j corner, p1 corner, take sameside corner force draw, if not diagonal blocked
         if(board[5-1] == o){
            if(board[1-1] == p && board[9-1] == o) play = 7;
            if(board[3-1] == p && board[7-1] == o) play = 1;
            if(board[7-1] == p && board[3-1] == o) play = 9;
            if(board[9-1] == p && board[1-1] == o) play = 3;
         }
         //p1 center, j corner, p1 edge, blocked
 
         //p1 edge, j center, p1 adj corner, blocked
         
         //p1 corner, j center, p1 edge,adj edge block, opposite edge, take corner adj edge     same as below
         //p1 edge, j center, p1 nonadj corner, draw game DO NOT TAKE edge opposite edge
         if(board[5-1] == p){
            if(board[2-1] == o && ((board[7-1] == o)||(board[9-1] == o))) play = 6;
            if(board[4-1] == o && ((board[3-1] == o)||(board[9-1] == o))) play = 2;
            if(board[6-1] == o && ((board[1-1] == o)||(board[7-1] == o))) play = 8;
            if(board[8-1] == o && ((board[1-1] == o)||(board[3-1] == o))) play = 4;
         }
         //p1 edge, j corner, p1 edge, strat check defaults
         //p1 edge, j corner, p1 center, block move
      }else if(move == 5){// j went first, finish traps RCR RRR
         if(board[5-1] == p){// RCR
            if(board[1-1] == p){
               if(board[3-1] != o && board[2-1] != o) play = 3;
               if(board[7-1] != o && board[4-1] != o) play = 7;
            }
            if(board[3-1] == p){
               if(board[1-1] != o && board[2-1] != o) play = 1;
               if(board[9-1] != o && board[6-1] != o) play = 9;
            }
            if(board[7-1] == p){
               if(board[1-1] != o && board[4-1] != o) play = 1;
               if(board[9-1] != o && board[8-1] != o) play = 9;
            }
            if(board[9-1] == p){
               if(board[3-1] != o && board[6-1] != o) play = 3;
               if(board[7-1] != o && board[8-1] != o) play = 7;
            }
         }//end RCR
         if(board[5-1] != p){//RRR
            if(board[1-1] == p && board[3-1] == p){
               if(board[9-1] != o && board[6-1] != o) play = 9;
               if(board[7-1] != o && board[4-1] != o) play = 7;
            }
            if(board[9-1] == p && board[3-1] == p){
               if(board[1-1] != o && board[2-1] != o) play = 1;
               if(board[7-1] != o && board[8-1] != o) play = 7;
            }
            if(board[7-1] == p && board[9-1] == p){
               if(board[1-1] != o && board[4-1] != o) play = 1;
               if(board[3-1] != o && board[6-1] != o) play = 3;
            }
            if(board[1-1] == p && board[7-1] == p){
               if(board[9-1] != o && board[8-1] != o) play = 9;
               if(board[3-1] != o && board[2-1] != o) play = 3;
            }
         }// end RRR
      }

      for(int i = 0; i < winCombos.length; i++){//block checker
         int row = 0;
         if(board[(winCombos[i][0])-1] == o) row++;
         if(board[(winCombos[i][1])-1] == o) row++;
         if(board[(winCombos[i][2])-1] == o) row++; 
         if(row == 2){
            if(board[(winCombos[i][0])-1] == 0) play = (winCombos[i][0]);
            if(board[(winCombos[i][1])-1] == 0) play = (winCombos[i][1]);
            if(board[(winCombos[i][2])-1] == 0) play = (winCombos[i][2]);
         }
      }//end block checker
      for(int i = 0; i < winCombos.length; i++){//win move checker
         int row = 0;
         if(board[(winCombos[i][0])-1] == p) row++;
         if(board[(winCombos[i][1])-1] == p) row++;
         if(board[(winCombos[i][2])-1] == p) row++; 
         if(row == 2){
            if(board[(winCombos[i][0])-1] == 0) play = (winCombos[i][0]);
            if(board[(winCombos[i][1])-1] == 0) play = (winCombos[i][1]);
            if(board[(winCombos[i][2])-1] == 0) play = (winCombos[i][2]);
         }
      }//end win move checker
      if((play == 1)&&(board[1-1] != 0)){//no strat applied pick next open spot
         for(int i = 0; i< board.length; i++){
            if(board[i] == 0) play = i + 1;
         }
      }
           
      try {
            Thread.sleep(jarvisDelay);
      }
      catch (InterruptedException ie) {
            
      }
      return play;
   }//end of jarvis the destoyer of worlds
}