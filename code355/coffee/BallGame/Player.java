import java.util.*;
public class Player
{
    public int score;
    public int hits;
    public Dictionary stats;

    public Player()
    {
        score = 0;
        hits = 0;
        //dictionary of hits
        stats.put("basic", 0);
        stats.put("shrink", 0);
        stats.put("bounce", 0);
        stats.put("split", 0);
                
    }
    public void UpdateScore(int points)
    {
        score+= points;
    }
}