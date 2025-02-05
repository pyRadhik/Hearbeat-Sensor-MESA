import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class Window extends JFrame
{
    public Window()
    {
        super();
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setContentPane(new View());
        setTitle("Heartbeat");
        setSize(800, 800);
    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Window window = new Window();
            window.setVisible(true);
        });
    }
}