module vector_renderer(
    input wire clk,
    input wire [9:0] x_pos,
    input wire [9:0] y_pos,
    input wire [1:0] rotation,
    output reg pixel_out
);
    
    // Простой квадрат с вращением
    parameter CENTER_X = 320;
    parameter CENTER_Y = 240;
    parameter SIZE = 30;
    
    // Координаты вершин в зависимости от вращения
    reg [9:0] vx0, vy0, vx1, vy1, vx2, vy2, vx3, vy3;
    
    always @(*) begin
        case(rotation)
            2'b00: begin // 0°
                vx0 = CENTER_X - SIZE; vy0 = CENTER_Y - SIZE;
                vx1 = CENTER_X + SIZE; vy1 = CENTER_Y - SIZE; 
                vx2 = CENTER_X + SIZE; vy2 = CENTER_Y + SIZE;
                vx3 = CENTER_X - SIZE; vy3 = CENTER_Y + SIZE;
            end
            2'b01: begin // 90°
                vx0 = CENTER_X + SIZE; vy0 = CENTER_Y - SIZE;
                vx1 = CENTER_X + SIZE; vy1 = CENTER_Y + SIZE;
                vx2 = CENTER_X - SIZE; vy2 = CENTER_Y + SIZE;
                vx3 = CENTER_X - SIZE; vy3 = CENTER_Y - SIZE;
            end
            2'b10: begin // 180°
                vx0 = CENTER_X + SIZE; vy0 = CENTER_Y + SIZE;
                vx1 = CENTER_X - SIZE; vy1 = CENTER_Y + SIZE;
                vx2 = CENTER_X - SIZE; vy2 = CENTER_Y - SIZE;
                vx3 = CENTER_X + SIZE; vy3 = CENTER_Y - SIZE;
            end
            2'b11: begin // 270°
                vx0 = CENTER_X - SIZE; vy0 = CENTER_Y + SIZE;
                vx1 = CENTER_X - SIZE; vy1 = CENTER_Y - SIZE;
                vx2 = CENTER_X + SIZE; vy2 = CENTER_Y - SIZE;
                vx3 = CENTER_X + SIZE; vy3 = CENTER_Y + SIZE;
            end
        endcase
    end
    
    // Проверка нахождения на гранях квадрата
    wire on_top = (y_pos == vy0) && (x_pos >= vx0) && (x_pos <= vx1);
    wire on_right = (x_pos == vx1) && (y_pos >= vy1) && (y_pos <= vy2);
    wire on_bottom = (y_pos == vy2) && (x_pos >= vx3) && (x_pos <= vx2);
    wire on_left = (x_pos == vx0) && (y_pos >= vy0) && (y_pos <= vy3);
    
    always @(posedge clk) begin
        pixel_out <= on_top | on_right | on_bottom | on_left;
    end
    
endmodule