import java.awt.Color;
import java.awt.Font;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import javax.swing.JLabel;
import javax.swing.JPanel;

public class View extends JPanel
{
    private JLabel text;
    public View()
    {
        super();
        setBackground(Color.BLACK);

        text = new JLabel("HI");
        text.setFont(new Font("TimesRoman", Font.BOLD, 500));
        text.setForeground(Color.LIGHT_GRAY);

        addKeyListener(new KeyAdapter(){
            private boolean nextClear = false;
            @Override
            public void keyPressed(KeyEvent e) {

                if (nextClear)
                {
                    text.setText("");
                    nextClear = false;
                }
                switch(e.getKeyChar())
                {
                    case ' ':
                        nextClear = true;
                        break;
                    default:
                        text.setText(text.getText() + e.getKeyChar());
                }
            }
        });

        add(text);
        setFocusable(true);
        requestFocus();
    }
}
