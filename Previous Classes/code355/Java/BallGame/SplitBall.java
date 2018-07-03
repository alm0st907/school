import java.awt.Color;
import java.lang.String;

public class SplitBall extends BasicBall
{
    public SplitBall(double r, Color c)
    {
        super(r,c);
        balltype = "split";
    }
    
    public int getScore()
    {
        return 10;
    }
}