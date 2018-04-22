import java.awt.Color;
public class BounceBall extends BasicBall
{
    private int bounces;
    public BounceBall(double r , Color c)
    {
        super(r, c);
        bounces = 0;
    }
    public void move()
    {
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) >= 1.0) || (Math.abs(ry) >= 1.0)) 
        {
            bounces +=1;
        }

    }
    public void draw() { 
    	if ((Math.abs(rx) <= 1.0) && (Math.abs(ry) <= 1.0)) {
    		StdDraw.setPenColor(color);
    		StdDraw.filledCircle(rx, ry, radius);
    	} else
        
        {
            if(bounces<4)
            {
                if(Math.abs(rx)>=1)
                {
                    vx = -vx;
                }
                else
                {
                    vy = -vy;
                }
            }
            else
            {
                isOut = true;
            }
        }
    }
        
    public int getScore() {
    	return 15;
    }
    
}