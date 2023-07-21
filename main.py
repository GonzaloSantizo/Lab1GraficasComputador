from gl import Renderer, V2, color

width = 1024
height = 1024

rend = Renderer(width, height)

# Define the vertices of the polygon
polygon_vertices = [
    (165, 380),
    (185, 360),
    (180, 330),
    (207, 345),
    (233, 330),
    (230, 360),
    (250, 380),
    (220, 385),
    (205, 410),
    (193, 383)
]

# Convert the polygon vertices to V2 objects and draw the polygon with the desired color
polygon_vertices_v2 = [V2(v[0], v[1]) for v in polygon_vertices]
rend.glPolygon(polygon_vertices_v2, color(1, 0, 0))  # Use red color (1, 0, 0)

# Render the scene (including the polygon)
rend.glRender()

# Save the result to a file
rend.glFinish("output.bmp")
