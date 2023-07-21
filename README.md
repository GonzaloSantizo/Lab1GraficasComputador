# glPolygon Function
The glPolygon function is an implementation of a basic scanline algorithm to fill a polygon with a specified color. 
It is typically used as part of a graphics library or module.


# Parameters
vertices (list): A list of (x, y) coordinate pairs that define the vertices of the polygon.
clr (tuple, optional): An optional parameter representing the color in the format (b, g, r), where b, g, and r are the color components for blue, green, and red, respectively. If this parameter is not provided (None), it uses the current color (self.currColor) as the default.

# Algorithm Description
Calculate the bounding box of the polygon by finding the minimum and maximum x and y coordinates of the vertices.

Convert the color to the expected format (b, g, r) if provided; otherwise, use the default current color.

Loop through each row within the bounding box and find the intersections of the polygon edges with that row.

Find Intersections: To find the intersections, iterate through each edge of the polygon. Check if the current row's y-coordinate lies between the y-coordinates of the edge's two vertices. If so, calculate the x-coordinate of the intersection point using linear interpolation and add it to the intersections list.

Sort the intersections list in ascending order.

Fill the pixels between pairs of intersections for each row. Determine the starting and ending x-coordinates for each row based on the sorted intersection points and call the glPoint function to fill the pixels along the current row with the specified color.
