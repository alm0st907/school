
public class Player
{
    public int score;
    public int hits;
    public Player()
    {
        score = 0;
        hits = 0;
    }
    public void UpdateScore(int points)
    {
        score+= points;
    }
}