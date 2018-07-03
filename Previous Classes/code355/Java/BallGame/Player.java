import java.util.*;

public class Player
{
    public int score;
    public int hits;
    public int shrinkHits;
    public int basicHits;
    public int bounceHits;
    public int splitHits;


    public Player()
    {
        score = 0;
        hits = 0;
        shrinkHits =0;
        basicHits = 0;
        splitHits = 0;
        bounceHits = 0;

                
    }
    public void UpdateScore(int points)
    {
        score+= points;
    }
    public void updateHits(String ballType)
    {
        switch(ballType)
        {
            case "basic":
                basicHits++;
                break;
            case "shrink":
                shrinkHits++;
            case "bounce":
                bounceHits++;
                break;
            case "split":
                splitHits++;
                break;
        }
    }
    public int getMax()
    {
        return Math.max(Math.max(shrinkHits, basicHits),Math.max(bounceHits, splitHits));
    }
    public String typeMaxHit()
    {
        int max = getMax();

            if(max == shrinkHits)
            {
                return "Shrink Balls hit most";
            }
            if(max == basicHits)
            {
                return "Basic Balls hit most";
            }
            if(max == bounceHits)
            {
                return "Bounce Balls hit most";
            }
            if(max == splitHits)
            {
                return "Split Balls hit most";                
            }
            else
            {
                return "Mutiple types";
            }
        
    }
}