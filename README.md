# Pyxel Button Example

This project demonstrates how to create interactive buttons with hover effects using the Pyxel library in Python. It includes examples of both rectangular and oval buttons, showcasing their interaction with mouse events.

## Getting Started

To run this project, you will need Python and Pyxel installed on your system.

### Prerequisites

- Python 3.6 or later
- Pyxel

### Installing Pyxel

Pyxel can be installed using pip. Run the following command in your terminal:

```bash
pip install pyxel
```

## Running the Application

To run the application, navigate to the directory containing `main.py` and execute it using Python. Ensure you have Pyxel installed as described in the installation section above.

```bash
python main.py
```

Upon running the application, a Pyxel window will open displaying a customizable button. This button demonstrates interactive behavior - changing appearance on hover and printing a message to the console on click.

# How It Works

## Main Application (`main.py`)

The main application sets up the Pyxel environment, creates a button instance, and controls the main loop where the button's update and draw methods are called. It handles initialization, input processing, and rendering.

## Button Class (`Button.py`)

The Button class encapsulates all functionality related to the button, including drawing itself with or without hover effects, detecting hover states, and responding to clicks. It supports both circular and rectangular buttons, as well as filled and bordered styles.

## Interaction

- **Hover:** The button changes color when the mouse hovers over it. This is visually indicated by a change in the button's border or fill color.
- **Click:** When clicked, the button performs an action. In this example, it prints "Button clicked" to the console. This can be customized to trigger any desired functionality.

## Customizing the Button

You can customize the button's appearance and behavior by adjusting its initialization parameters in `main.py`. This includes size, position, colors, and whether the button is circular or rectangular.

## Understanding the Code

### Drawing an Oval

For oval buttons, the `draw_oval` method in `Button.py` calculates points around an ellipse's perimeter and plots them. This method is used when the button is initialized with different width and height parameters to achieve an oval shape.

### Hover Detection

The `hovered` method calculates whether the mouse pointer is within the button's boundaries, adjusting its behavior based on the button's shape (circular or rectangular).

## Expanding the Project

This framework provides a foundation for creating interactive Pyxel applications. Potential expansions include:

- Implementing different button actions based on the context.
- Adding more interactive elements like sliders or checkboxes.
- Creating a menu system using the button class.

## Behind the Scenes: Text Size not defined

Pyxel has not any declaration about `pyxel.text` size, so i had to aproximately calculate it for each shape.
The approximate text size calculation is based on the length of the text string multiplied by an arbitrary value. This value is used as a rough estimate of the width of the text, assuming a fixed width for each character. While not precise, this estimation helps in horizontally centering the text within the button. Adjustments to this estimation may be necessary depending on the font size and style used.

## Conclusion

This project demonstrates the basics of creating interactive graphics with Pyxel. By exploring and extending this example, you can build more complex applications and games.

