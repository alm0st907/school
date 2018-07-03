/*
garrett rudisill
wsu id 11461816
the last homework
ballgame for java

*/
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;
import java.lang.String;


public class BallGame { 

    public static void main(String[] args) {
        
        if(args.length<3)
        {
            System.out.println("not enough arguments");
            return;
        }

        int numBalls;
        // number of bouncing balls
        try
        {
            numBalls = Integer.parseInt(args[0]);
        }catch(NumberFormatException e)
        {
            System.out.println("first argument must be number");
            return;
        }

    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
        double ballSizes[] = new double[numBalls];
        Player thisPlayer = new Player();
    	
    	//retrieve ball types
        int index =1;
        try
        {
            for (int i=0; i<numBalls; i++) {
                ballTypes[i] = args[index];
                index = index+2;
            }
        }catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.println("Arguments incomplete");
            return;
        }

    	//retrieve ball sizes, has error catch for mismatched arguments
        index = 2;
        try{
            for (int i=0; i<numBalls; i++) {
                ballSizes[i] = Double.parseDouble(args[index]);
                index = index+2;
            }
        }catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.println("Arguments incomplete");
            return;
        }
     
    	//TO DO: create a Player object and initialize the player game stats.  
    	

    	//number of active balls
    	int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);

        // create colored balls 
        //TO DO: Create "numBalls" balls (of types given in "ballTypes" with sizes given in "ballSizes") and store them in an Arraylist
        ArrayList<BasicBall> all_the_balls = new ArrayList<BasicBall>();
        for(int i = 0; i<numBalls;i++)
        {
            switch (ballTypes[i].toLowerCase())
            {
                case "basic":
                    all_the_balls.add(new BasicBall(ballSizes[i], Color.red));
                    break;
                case "bounce":
                    all_the_balls.add(new BounceBall(ballSizes[i], Color.BLUE));
                    break;
                case "split":
                    all_the_balls.add(new SplitBall(ballSizes[i], Color.green));
                    break;
                case "shrink":
                    all_the_balls.add(new ShrinkBall(ballSizes[i], Color.yellow));
                    break;
                
            }
        }
        
   		//TO DO: initialize the numBallsinGame

        numBallsinGame = all_the_balls.size();
        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {

        	// TODO: move all balls

            for(int i = 0;i<all_the_balls.size();i++)
            {
                all_the_balls.get(i).move();
            }

            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                //TODO: check whether a ball is hit. Check each ball.  

                for(int i = 0;i<all_the_balls.size();i++)
                {
                    if(all_the_balls.get(i).isHit(x, y))
                    {
  
                        thisPlayer.UpdateScore(all_the_balls.get(i).getScore());
                        thisPlayer.hits++;
                        thisPlayer.updateHits(all_the_balls.get(i).balltype);
    
                        all_the_balls.get(i).reset();
                        if(all_the_balls.get(i).balltype == "split")
                        {
                            all_the_balls.add(new SplitBall(all_the_balls.get(i).radius, all_the_balls.get(i).color));
                            //prevent trigger loop
                            x= -1.000000;
                            y = 1.000000;
                        }
                    }
                }
            }
            
                
            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            //TO DO: check each ball and see if they are still visible. numBallsinGame should hold the number of visible balls in the game.  

            for(int i = 0;i<all_the_balls.size();i++)
            {
                if(all_the_balls.get(i).isOut==false)
                {
                    all_the_balls.get(i).draw();
                    numBallsinGame++;
                }
            }
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.55, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            StdDraw.text(-0.82, 0.80, "Score: "+ String.valueOf(thisPlayer.score));
            StdDraw.text(-0.84, 0.70, "Hits: "+ String.valueOf(thisPlayer.hits));
            
            //TO DO: print the rest of the player statistics

            StdDraw.show();
            StdDraw.pause(20);
        }
    
        
        while (true) {
            StdDraw.clear(Color.gray);
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            //TO DO: print the rest of the player statistics
            StdDraw.text(0,.75,"Score: "+String.valueOf(thisPlayer.score));
            StdDraw.text(0,.5,"Hits: "+String.valueOf(thisPlayer.hits));
            
            Font font2 = new Font("Arial", Font.BOLD, 32);
            StdDraw.setFont(font2);
            
            
            StdDraw.text(0,.25,thisPlayer.typeMaxHit()+" with "+String.valueOf(thisPlayer.getMax())+" hits");
            
            
            StdDraw.show();
            StdDraw.pause(10);           
        }
        	
        
    }
}
