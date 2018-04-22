/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments : 1  basic  0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;
import java.lang.String;

import com.sun.org.apache.bcel.internal.generic.INSTANCEOF;


public class BallGame { 

    public static void main(String[] args) {
  
        // number of bouncing balls
    	int numBalls = Integer.parseInt(args[0]);
    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
        double ballSizes[] = new double[numBalls];
        Player thisPlayer = new Player();
    	
    	//retrieve ball types
    	int index =1;
    	for (int i=0; i<numBalls; i++) {
    		ballTypes[i] = args[index];
    		index = index+2;
    	}
    	//retrieve ball sizes
    	index = 2;
    	for (int i=0; i<numBalls; i++) {
    		ballSizes[i] = Double.parseDouble(args[index]);
    		index = index+2;
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
        //BasicBall ball = new BounceBall(ballSizes[0],Color.RED);
        //BasicBall ball2 = new BasicBall(ballSizes[0], Color.CYAN);
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
   		//numBallsinGame++;
   		//numBallsinGame++;
        numBallsinGame = all_the_balls.size();
        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {

        	// TODO: move all balls
            //ball.move();
            //ball2.move();
            for(int i = 0;i<all_the_balls.size();i++)
            {
                all_the_balls.get(i).move();
            }

            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                //TODO: check whether a ball is hit. Check each ball.  
                // if (ball.isHit(x,y)) {
                //     	ball.reset();
                //     	//TO DO: Update player statistics
                // }
                // if (ball2.isHit(x,y)) {
                //     ball2.reset();
                //     //TO DO: Update player statistics
                for(int i = 0;i<all_the_balls.size();i++)
                {
                    if(all_the_balls.get(i).isHit(x, y))
                    {
                        if(all_the_balls.get(i).balltype == "split")
                        {
                            all_the_balls.add(new SplitBall(all_the_balls.get(i).radius, all_the_balls.get(i).color));
                        }
                        thisPlayer.UpdateScore(all_the_balls.get(i).getScore());
                        thisPlayer.hits++;
                        thisPlayer.updateHits(all_the_balls.get(i).balltype);
    
                        all_the_balls.get(i).reset();
                    }
                }
            }
            
                
            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            //TO DO: check each ball and see if they are still visible. numBallsinGame should hold the number of visible balls in the game.  
            // if (ball.isOut == false) { 
            //     ball.draw();
            //     numBallsinGame++;
            // }
            // if (ball2.isOut == false) { 
            //     ball2.draw();
            //     numBallsinGame++;
            // }

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
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            //TO DO: print the rest of the player statistics

            StdDraw.show();
            StdDraw.pause(20);
        }
    
        
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            //TO DO: print the rest of the player statistics
            StdDraw.text(0,.75,"Max Hits: "+String.valueOf(thisPlayer.getMax()));
            StdDraw.text(0,.5,"Score: "+String.valueOf(thisPlayer.score));
            StdDraw.text(0,.25,"Hits: "+String.valueOf(thisPlayer.hits));
            
            StdDraw.show();
            StdDraw.pause(10);           
        }
        	
        
    }
}
